from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Configuração do banco de dados
# Suporta SQLite (desenvolvimento) e PostgreSQL (produção)
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = os.environ.get('DATABASE_URL', f'sqlite:///{os.path.join(basedir, "emissoes.db")}')

# Fix para Railway/Heroku (postgres:// → postgresql://)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo do banco de dados
class EmissaoRegistro(db.Model):
    __tablename__ = 'emissao_registros'
    
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(50), nullable=False)
    endereco_origem = db.Column(db.Text, nullable=False)
    endereco_destino = db.Column(db.Text, nullable=False)
    distancia = db.Column(db.Float, nullable=False)
    meio_transporte = db.Column(db.String(50), nullable=False)
    combustivel = db.Column(db.String(30), nullable=False)
    fator_emissao = db.Column(db.Integer, nullable=False)
    emissao_total = db.Column(db.Float, nullable=False)
    categoria_emissao = db.Column(db.String(30), nullable=False)
    dica_sustentabilidade = db.Column(db.Text)
    data_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'matricula': self.matricula,
            'endereco_origem': self.endereco_origem,
            'endereco_destino': self.endereco_destino,
            'distancia': self.distancia,
            'meio_transporte': self.meio_transporte,
            'combustivel': self.combustivel,
            'fator_emissao': self.fator_emissao,
            'emissao_total': self.emissao_total,
            'categoria_emissao': self.categoria_emissao,
            'dica_sustentabilidade': self.dica_sustentabilidade,
            'data_registro': self.data_registro.isoformat() if self.data_registro else None
        }

# fatores de emissão por tipo de veículo e combustível (g CO₂/km)
FATORES_EMISSAO = {
    "veiculo_proprio": {
        "gasolina": 165,
        "etanol": 95,
        "diesel": 180,
        "gnv": 120,
        "eletrico": 50
    },
    "carro_aplicativo": {
        "gasolina": 165,
        "etanol": 95,
        "diesel": 180,
        "gnv": 120,
        "eletrico": 50
    },
    "motocicleta": {
        "gasolina": 90,
        "etanol": 65,
        "eletrico": 30
    },
    "onibus": {
        "diesel": 80,  # Por passageiro
        "gnv": 60,
        "eletrico": 25
    },
    "bicicleta": {
        "nao_se_aplica": 0
    },
    "caminhando": {
        "nao_se_aplica": 0
    }
}

@app.route("/api/calcular", methods=["POST"])
def calcular_emissao():
    try:
        data = request.get_json()
        
        # Dados do formulário
        matricula = data.get("matricula", "")
        endereco_origem = data.get("endereco_origem", "")
        endereco_destino = data.get("endereco_destino", "")
        distancia = float(data.get("distancia", 0))
        meio_transporte = data.get("meio_transporte", "")
        combustivel = data.get("combustivel", "nao_se_aplica")
        autorizacao = data.get("autorizacao", False)
        
        # Validações básicas
        if not matricula or len(matricula) < 3:
            return jsonify({"error": "Matrícula deve ter pelo menos 3 caracteres"}), 400
            
        if not endereco_origem or not endereco_destino:
            return jsonify({"error": "Endereços de origem e destino são obrigatórios"}), 400
            
        if distancia <= 0:
            return jsonify({"error": "Distância deve ser maior que zero"}), 400
            
        if not meio_transporte:
            return jsonify({"error": "Meio de transporte é obrigatório"}), 400
            
        if not autorizacao:
            return jsonify({"error": "Autorização para uso dos dados é obrigatória"}), 400
        
        # Calcular emissão
        fator_emissao = 0
        if meio_transporte in FATORES_EMISSAO:
            if combustivel in FATORES_EMISSAO[meio_transporte]:
                fator_emissao = FATORES_EMISSAO[meio_transporte][combustivel]
            else:
                # Se combustível não especificado, usar gasolina como padrão
                fator_emissao = FATORES_EMISSAO[meio_transporte].get("gasolina", 0)
        
        # Calcular emissão total em kg
        emissao_total_kg = round((distancia * fator_emissao) / 1000, 2)
        
        # Obter categoria e dica
        categoria = get_categoria_emissao(emissao_total_kg)
        dica = get_dica_sustentabilidade(meio_transporte, emissao_total_kg)
        
        # Salvar no banco de dados
        novo_registro = EmissaoRegistro(
            matricula=matricula,
            endereco_origem=endereco_origem,
            endereco_destino=endereco_destino,
            distancia=distancia,
            meio_transporte=meio_transporte,
            combustivel=combustivel,
            fator_emissao=fator_emissao,
            emissao_total=emissao_total_kg,
            categoria_emissao=categoria,
            dica_sustentabilidade=dica
        )
        
        db.session.add(novo_registro)
        db.session.commit()
        
        # Preparar resposta detalhada
        response = {
            "emissao": emissao_total_kg,
            "registro_id": novo_registro.id,
            "dados": {
                "matricula": matricula,
                "origem": endereco_origem,
                "destino": endereco_destino,
                "distancia": distancia,
                "meio_transporte": meio_transporte,
                "combustivel": combustivel,
                "fator_emissao": fator_emissao
            },
            "analise": {
                "categoria": categoria,
                "dica": dica
            }
        }
        
        return jsonify(response)
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500

def get_categoria_emissao(emissao):
    if emissao == 0:
        return "Zero Emissão"
    elif emissao < 2:
        return "Muito Baixa"
    elif emissao < 5:
        return "Baixa"
    elif emissao < 15:
        return "Moderada"
    elif emissao < 30:
        return "Alta"
    else:
        return "Muito Alta"

def get_dica_sustentabilidade(meio_transporte, emissao):
    if meio_transporte in ["bicicleta", "caminhando"]:
        return "Parabéns! Você escolheu um meio de transporte sustentável e saudável!"
    elif emissao == 0:
        return "Excelente escolha! Transporte com zero emissão de carbono."
    elif emissao < 5:
        return "Boa escolha! Baixa emissão de carbono."
    elif emissao < 15:
        return "Considere usar transporte público ou compartilhar a viagem."
    else:
        return "Alta emissão! Considere alternativas mais sustentáveis como transporte público, bicicleta ou carona."

@app.route("/api/salvar-dados", methods=["POST"])
def salvar_dados():
    """Endpoint para apenas salvar os dados sem retornar cálculos"""
    try:
        data = request.get_json()
        
        # Dados do formulário
        matricula = data.get("matricula", "")
        endereco_origem = data.get("endereco_origem", "")
        endereco_destino = data.get("endereco_destino", "")
        distancia = float(data.get("distancia", 0))
        meio_transporte = data.get("meio_transporte", "")
        combustivel = data.get("combustivel", "nao_se_aplica")
        autorizacao = data.get("autorizacao", False)
        
        # Validações básicas
        if not matricula or len(matricula) < 3:
            return jsonify({"error": "Matrícula deve ter pelo menos 3 caracteres"}), 400
            
        if not endereco_origem or not endereco_destino:
            return jsonify({"error": "Endereços de origem e destino são obrigatórios"}), 400
            
        if distancia <= 0:
            return jsonify({"error": "Distância deve ser maior que zero"}), 400
            
        if not meio_transporte:
            return jsonify({"error": "Meio de transporte é obrigatório"}), 400
            
        if not autorizacao:
            return jsonify({"error": "Autorização para uso dos dados é obrigatória"}), 400
        
        # Calcular emissão (para salvar no banco, mas não retornar)
        fator_emissao = 0
        if meio_transporte in FATORES_EMISSAO:
            if combustivel in FATORES_EMISSAO[meio_transporte]:
                fator_emissao = FATORES_EMISSAO[meio_transporte][combustivel]
            else:
                # Se combustível não especificado, usar gasolina como padrão
                fator_emissao = FATORES_EMISSAO[meio_transporte].get("gasolina", 0)
        
        # Calcular emissão total em kg
        emissao_total_kg = round((distancia * fator_emissao) / 1000, 2)
        
        # Obter categoria e dica
        categoria = get_categoria_emissao(emissao_total_kg)
        dica = get_dica_sustentabilidade(meio_transporte, emissao_total_kg)
        
        # Salvar no banco de dados
        novo_registro = EmissaoRegistro(
            matricula=matricula,
            endereco_origem=endereco_origem,
            endereco_destino=endereco_destino,
            distancia=distancia,
            meio_transporte=meio_transporte,
            combustivel=combustivel,
            fator_emissao=fator_emissao,
            emissao_total=emissao_total_kg,
            categoria_emissao=categoria,
            dica_sustentabilidade=dica
        )
        
        db.session.add(novo_registro)
        db.session.commit()
        
        # Retornar apenas confirmação de sucesso
        return jsonify({
            "sucesso": True,
            "mensagem": "Dados salvos com sucesso!",
            "registro_id": novo_registro.id
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500

@app.route("/api/fatores-emissao", methods=["GET"])
def get_fatores_emissao():
    return jsonify(FATORES_EMISSAO)

@app.route("/api/registros", methods=["GET"])
def get_registros():
    """Endpoint para consultar todos os registros"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        # Limitar per_page para evitar sobrecarga
        per_page = min(per_page, 100)
        
        registros = EmissaoRegistro.query.order_by(EmissaoRegistro.data_registro.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            "registros": [registro.to_dict() for registro in registros.items],
            "total": registros.total,
            "pages": registros.pages,
            "current_page": registros.page,
            "per_page": per_page
        })
        
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar registros: {str(e)}"}), 500

@app.route("/api/registros/<int:registro_id>", methods=["GET"])
def get_registro(registro_id):
    """Endpoint para consultar um registro específico"""
    try:
        registro = EmissaoRegistro.query.get_or_404(registro_id)
        return jsonify(registro.to_dict())
        
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar registro: {str(e)}"}), 500

@app.route("/api/estatisticas", methods=["GET"])
def get_estatisticas():
    """Endpoint para estatísticas gerais"""
    try:
        total_registros = EmissaoRegistro.query.count()
        
        if total_registros == 0:
            return jsonify({
                "total_registros": 0,
                "emissao_total": 0,
                "emissao_media": 0,
                "meio_transporte_mais_usado": None,
                "categoria_mais_comum": None
            })
        
        # Emissão total e média
        emissao_total = db.session.query(db.func.sum(EmissaoRegistro.emissao_total)).scalar() or 0
        emissao_media = db.session.query(db.func.avg(EmissaoRegistro.emissao_total)).scalar() or 0
        
        # Meio de transporte mais usado
        meio_mais_usado = db.session.query(
            EmissaoRegistro.meio_transporte,
            db.func.count(EmissaoRegistro.meio_transporte).label('count')
        ).group_by(EmissaoRegistro.meio_transporte).order_by(db.text('count DESC')).first()
        
        # Categoria mais comum
        categoria_mais_comum = db.session.query(
            EmissaoRegistro.categoria_emissao,
            db.func.count(EmissaoRegistro.categoria_emissao).label('count')
        ).group_by(EmissaoRegistro.categoria_emissao).order_by(db.text('count DESC')).first()
        
        return jsonify({
            "total_registros": total_registros,
            "emissao_total": round(float(emissao_total), 2),
            "emissao_media": round(float(emissao_media), 2),
            "meio_transporte_mais_usado": meio_mais_usado[0] if meio_mais_usado else None,
            "categoria_mais_comum": categoria_mais_comum[0] if categoria_mais_comum else None
        })
        
    except Exception as e:
        return jsonify({"error": f"Erro ao gerar estatísticas: {str(e)}"}), 500

@app.route("/api/registros/matricula/<matricula>", methods=["GET"])
def get_registros_por_matricula(matricula):
    """Endpoint para consultar registros de uma matrícula específica"""
    try:
        registros = EmissaoRegistro.query.filter_by(matricula=matricula).order_by(
            EmissaoRegistro.data_registro.desc()
        ).all()
        
        return jsonify({
            "matricula": matricula,
            "total_registros": len(registros),
            "registros": [registro.to_dict() for registro in registros]
        })
        
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar registros da matrícula: {str(e)}"}), 500

if __name__ == "__main__":
    # Criar tabelas se não existirem
    with app.app_context():
        db.create_all()
        print("Banco de dados inicializado!")
        print("Servidor Flask iniciando...")
    
    # Para desenvolvimento local
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
else:
    # Para produção - criar tabelas quando importado
    with app.app_context():
        db.create_all()
