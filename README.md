# 🌱 EcoCalc - Calculadora de Emissão de CO₂# 📊 Formulário de Pesquisa de Emissões CO₂ - Univates



## 📋 Descrição## 🎯 Sobre o Sistema

Sistema web para cálculo de emissões de CO₂ baseado em diferentes tipos de transporte e atividades. Desenvolvido para análise do impacto ambiental de deslocamentos.

Este sistema coleta dados sobre os hábitos de transporte dos participantes da Semana Acadêmica dos Cursos Técnicos da Univates, calculando automaticamente as emissões de CO₂ para análise do impacto ambiental.

## 🚀 Tecnologias

- **Backend**: Flask + SQLAlchemy + SQLite## 📍 Localização dos Dados

- **Frontend**: HTML + CSS + JavaScript (Vanilla)

- **Banco de Dados**: SQLite### 🗄️ Banco de Dados SQLite

- **Deploy**: Netlify (Frontend) + Railway/Render (Backend)- **Arquivo**: `backend/emissoes.db`

- **Localização completa**: `C:\Users\joaog\Desktop\fomulario_emissao\emissao_app (3)\backend\emissoes.db`

## 📁 Estrutura do Projeto (Limpa)- **Tabela**: `emissao_registros`

```

emissao_app/### 📋 Campos Armazenados

├── backend/- `id` - ID único do registro

│   ├── app.py              # Aplicação Flask principal- `matricula` - Matrícula do estudante

│   ├── requirements.txt    # Dependências Python- `endereco_origem` - Endereço de origem completo

│   └── emissoes.db        # Banco de dados SQLite- `endereco_destino` - Endereço de destino (Univates)

├── frontend/- `distancia` - Distância em quilômetros

│   └── public/- `meio_transporte` - Tipo de transporte utilizado

│       ├── index.html     # Interface principal- `combustivel` - Tipo de combustível (quando aplicável)

│       └── index.js       # Lógica do frontend- `fator_emissao` - Fator de emissão usado no cálculo (g CO₂/km)

├── netlify-frontend/       # Versão standalone para deploy- `emissao_total` - Emissão total calculada (kg CO₂)

│   └── index.html         # Frontend completo para Netlify- `categoria_emissao` - Categoria da emissão (Zero, Baixa, Moderada, etc.)

├── .gitignore             # Arquivos ignorados pelo Git- `dica_sustentabilidade` - Dica personalizada

└── README.md              # Documentação do projeto- `data_registro` - Data e hora do preenchimento

```

## 🚀 Como Acessar os Dados

## 🛠️ Como Executar

### 1. 📊 **Extração Automática (RECOMENDADO)**

### Pré-requisitos

- Python 3.8+Execute o script de extração que gera relatórios completos:

- pip (gerenciador de pacotes Python)

```bash

### Backendpython extrair_dados.py

1. Navegue até a pasta backend:```

   ```bash

   cd backend**Arquivos gerados:**

   ```- `dados_formulario_AAAAMMDD_HHMMSS.csv` - Dados completos formatados (todos os campos)

- `resumo_dados_AAAAMMDD_HHMMSS.csv` - **Resumo limpo para Excel/Sheets** ⭐

2. Crie um ambiente virtual (recomendado):- `dados_visualizacao_AAAAMMDD_HHMMSS.csv` - Otimizado para dashboards/gráficos

   ```bash- `dados_para_analise_AAAAMMDD_HHMMSS.csv` - Dados numéricos para análise estatística

   python -m venv venv- `relatorio_emissoes_AAAAMMDD_HHMMSS.txt` - Relatório detalhado

   venv\Scripts\activate  # Windows- `resumo_executivo_AAAAMMDD_HHMMSS.txt` - Resumo executivo

   # source venv/bin/activate  # Linux/Mac

   ```### 2. 🌐 **Via API REST**



3. Instale as dependências:Com o servidor Flask rodando (`python backend/app.py`):

   ```bash

   pip install -r requirements.txt#### Endpoints Disponíveis:

   ```

- **Estatísticas Gerais**: `GET http://localhost:5000/api/estatisticas`

4. Execute o servidor:- **Todos os registros**: `GET http://localhost:5000/api/registros`

   ```bash- **Registro específico**: `GET http://localhost:5000/api/registros/{id}`

   python app.py- **Por matrícula**: `GET http://localhost:5000/api/registros/matricula/{matricula}`

   ```- **Fatores de emissão**: `GET http://localhost:5000/api/fatores-emissao`

   O servidor estará disponível em `http://localhost:5000`

#### Script de Consulta:

### Frontend```bash

1. Abra o arquivo `frontend/public/index.html` em um navegadorpython consultar_api.py

   - Ou sirva através de um servidor web local:```

   ```bash

   cd frontend/public### 3. 💾 **Acesso Direto ao Banco SQLite**

   python -m http.server 8000

   ``````python

import sqlite3

## ✨ Funcionalidades

- ✅ Cálculo de emissões para diferentes modais de transporte# Conectar ao banco

- ✅ Armazenamento de dados em SQLite  conn = sqlite3.connect('backend/emissoes.db')

- ✅ Interface responsiva e modernacursor = conn.cursor()

- ✅ API REST para integração

- ✅ Formulário completo com validação# Consultar todos os dados

- ✅ Categorização automática de emissõescursor.execute("SELECT * FROM emissao_registros ORDER BY data_registro DESC")

- ✅ Dicas de sustentabilidade personalizadasregistros = cursor.fetchall()

- ✅ Persistência local (localStorage) para ambiente offline

for registro in registros:

## 🌐 Deploy    print(registro)



### Frontend (Netlify)conn.close()

A pasta `netlify-frontend/` contém uma versão standalone pronta para deploy:```

1. Faça upload da pasta no Netlify

2. Configure domínio personalizado se necessário### 4. 📈 **Ferramentas de Análise**



### Backend (Railway/Render)  #### Excel/Google Sheets:

Para hospedar o backend, use plataformas como:1. **Use `resumo_dados_AAAAMMDD_HHMMSS.csv`** - Formatação limpa e organizada

- **Railway** (recomendado)2. Cabeçalhos em português

- **Render**  3. Dados formatados para fácil leitura

- **PythonAnywhere**4. Campos essenciais sem informações técnicas desnecessárias

- **Heroku**

#### Power BI / Tableau:

## 📊 Banco de Dados1. **Use `dados_visualizacao_AAAAMMDD_HHMMSS.csv`** - Otimizado para gráficos

2. Inclui colunas "Sustentável" (Sim/Não), separação de data/hora

### Tabela: `emissao_registros`3. Nomes participantes anônimos (Participante 1, 2, etc.)

Campos armazenados:4. Ou conecte diretamente ao SQLite `backend/emissoes.db`

- `id` - ID único do registro

- `matricula` - Matrícula/identificação do usuário#### Análise Estatística (Python/R):

- `endereco_origem` - Endereço de origem1. **Use `dados_para_analise_AAAAMMDD_HHMMSS.csv`** - Dados numéricos

- `endereco_destino` - Endereço de destino2. Códigos numéricos para transportes e categorias

- `distancia` - Distância em quilômetros3. Variáveis binárias (sustentável = 1/0)

- `meio_transporte` - Tipo de transporte4. Timestamps completos para análise temporal

- `combustivel` - Tipo de combustível

- `fator_emissao` - Fator de emissão (g CO₂/km)#### Python/Pandas:

- `emissao_total` - Emissão total (kg CO₂)```python

- `categoria_emissao` - Categoria da emissãoimport pandas as pd

- `dica_sustentabilidade` - Dica personalizadaimport sqlite3

- `data_registro` - Timestamp do registro

# Ler dados do SQLite

## 🔧 API Endpointsconn = sqlite3.connect('backend/emissoes.db')

df = pd.read_sql_query("SELECT * FROM emissao_registros", conn)

Base URL: `http://localhost:5000/api`

# Análises básicas

- `GET /estatisticas` - Estatísticas geraisprint(df.describe())

- `GET /registros` - Todos os registrosprint(df['meio_transporte'].value_counts())

- `GET /registros/{id}` - Registro específicoprint(df.groupby('categoria_emissao')['emissao_total'].sum())

- `GET /fatores-emissao` - Fatores de emissão```

- `POST /registros` - Criar novo registro

## 🌐 COLOCAR FORMULÁRIO ONLINE

## 🧹 Limpeza Realizada

### 🚀 **Opção Mais Fácil (15 minutos):**

Este projeto foi limpo removendo:```bash

- ❌ Ambiente virtual (`venv/`, `.venv/`)# 1. Leia o guia simples

- ❌ Arquivos CSV temporários com timestampsDEPLOY_FACIL.md

- ❌ Scripts de extração desnecessários

- ❌ Documentação redundante (5 arquivos MD)# 2. Plataformas gratuitas recomendadas:

- ❌ Versões duplicadas de arquivos- Backend: railway.app ou render.com

- ❌ Pastas vazias (`data/`, `exports/`)- Frontend: netlify.com ou vercel.com

- ❌ Cache Python (`__pycache__/`)

# 3. Resultado: Link público para compartilhar!

## 📝 .gitignore```



Configurado para ignorar automaticamente:### 📋 **Guias Disponíveis:**

- Ambientes virtuais- 📖 `DEPLOY_FACIL.md` - **Versão simples para iniciantes** ⭐

- Arquivos Python temporários- 📖 `GUIA_DEPLOY.md` - Instruções detalhadas completas

- Banco de dados SQLite- 📖 `GUIA_EXCEL.md` - Como usar os CSVs gerados

- Arquivos CSV com timestamp

- Configurações de IDE### 🎯 **Após Deploy:**

- Arquivos do sistema operacional✅ **Custo**: Totalmente gratuito  

✅ **Acesso**: 24/7 na internet  

## 🤝 Contribuição✅ **Compatibilidade**: Todos os dispositivos  

1. Fork o projeto✅ **Capacidade**: ~500 respostas/mês  

2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)

3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)## 📊 Exemplo de Dados Extraídos

4. Push para a branch (`git push origin feature/AmazingFeature`)

5. Abra um Pull Request### Resumo dos Dados Atuais:

- **4 participantes** responderam ao formulário

## 📄 Licença- **Emissão total**: 6.18 kg CO₂ 

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.- **Emissão média**: 1.54 kg CO₂ por pessoa

- **Distância média**: 16.05 km por viagem

---- **50% usam transporte sustentável** (bicicleta)

- **50% usam transporte motorizado**

🌱 **Sistema pronto para produção e totalmente limpo!**
### Distribuição por Transporte:
- Bicicleta: 2 pessoas (50%) - 0 kg CO₂
- Ônibus: 1 pessoa (25%) - 2.8 kg CO₂  
- Veículo próprio: 1 pessoa (25%) - 3.38 kg CO₂

## 🔄 Atualizações em Tempo Real

Os dados são salvos automaticamente sempre que alguém preenche o formulário em `http://localhost:8000`. Para ver os dados mais recentes:

1. **Via script**: Execute `python extrair_dados.py` novamente
2. **Via API**: Faça uma nova consulta aos endpoints
3. **Via banco**: Reconecte ao SQLite e consulte

## 🛠️ Comandos Úteis

```bash
# Iniciar o sistema completo
python backend/app.py          # Terminal 1: API Flask
python -m http.server 8000     # Terminal 2: Frontend (na pasta frontend/public)

# Extrair dados
python extrair_dados.py

# Consultar via API
python consultar_api.py

# Ver estrutura do banco
sqlite3 backend/emissoes.db ".schema"

# Contar registros
sqlite3 backend/emissoes.db "SELECT COUNT(*) FROM emissao_registros;"
```

## 📁 Estrutura de Arquivos

```
emissao_app (3)/
├── backend/
│   ├── app.py              # Servidor Flask com API
│   ├── emissoes.db         # ⭐ BANCO DE DADOS COM OS DADOS
│   └── requirements.txt
├── frontend/
│   └── public/
│       ├── index.html      # Interface do formulário
│       └── index.js        # Lógica do frontend
├── extrair_dados.py        # ⭐ SCRIPT DE EXTRAÇÃO
├── consultar_api.py        # Script de consulta API
└── dados_*.csv             # ⭐ ARQUIVOS CSV GERADOS
└── relatorio_*.txt         # ⭐ RELATÓRIOS GERADOS
```

## 🎯 Próximos Passos

1. **Para continuar coletando**: Mantenha ambos os servidores rodando
2. **Para análise**: Use os arquivos CSV/TXT gerados ou conecte ferramentas de BI
3. **Para backup**: Copie o arquivo `backend/emissoes.db` para local seguro
4. **Para relatórios**: Execute `extrair_dados.py` periodicamente

---

✅ **Sistema totalmente funcional e pronto para uso acadêmico!**