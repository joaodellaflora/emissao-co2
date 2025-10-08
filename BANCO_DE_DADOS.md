# 💾 **Como Funciona o Banco de Dados**

## **Banco Atual: SQLite**

### **Estrutura da Tabela `emissao_registros`:**
```sql
CREATE TABLE emissao_registros (
    id INTEGER PRIMARY KEY,                    -- ID único automático
    matricula VARCHAR(50) NOT NULL,            -- Matrícula do estudante
    endereco_origem TEXT NOT NULL,             -- Endereço de partida
    endereco_destino TEXT NOT NULL,            -- Endereço de chegada  
    distancia FLOAT NOT NULL,                  -- Distância em km
    meio_transporte VARCHAR(50) NOT NULL,      -- Tipo de transporte
    combustivel VARCHAR(30) NOT NULL,          -- Tipo de combustível
    fator_emissao INTEGER NOT NULL,            -- Fator em g CO₂/km
    emissao_total FLOAT NOT NULL,              -- Total em kg CO₂
    categoria_emissao VARCHAR(30) NOT NULL,    -- Zero/Baixa/Moderada/Alta
    dica_sustentabilidade TEXT,                -- Dica personalizada
    data_registro DATETIME                     -- Timestamp
);
```

## **Localização e Tamanho:**
- **Arquivo**: `backend/emissoes.db`
- **Tamanho**: ~8 KB (muito leve!)
- **Registros atuais**: 5 entradas

## **Como Funciona:**

### **1. Desenvolvimento Local (Atual)**
```
┌─────────────────┐    ┌──────────────┐    ┌─────────────┐
│   Frontend      │───▶│   Flask API  │───▶│ SQLite.db   │
│ (HTML/JS)       │    │ (Python)     │    │ (8 KB)      │
│ localhost:8000  │    │ localhost:5000│   │ Local file  │
└─────────────────┘    └──────────────┘    └─────────────┘
```

### **2. Deploy em Produção (Railway/Render)**
```
┌─────────────────┐    ┌──────────────┐    ┌─────────────┐
│   Netlify       │───▶│   Railway    │───▶│ PostgreSQL  │
│ (Static site)   │    │ (Flask API)  │    │ (Cloud DB)  │
│ seu-site.netlify│    │ app.railway  │    │ Managed     │
└─────────────────┘    └──────────────┘    └─────────────┘
```

## **Migração SQLite → PostgreSQL**

### **Por que migrar?**
- ✅ **Concurrent users**: SQLite = 1 usuário, PostgreSQL = milhares
- ✅ **Backup automático**: Railway/Render fazem backup
- ✅ **Escalabilidade**: Cresce com seu projeto
- ✅ **Confiabilidade**: Não perde dados no deploy

### **Como migrar automaticamente:**

1. **Railway detecta e converte automaticamente**
2. **Render oferece PostgreSQL gratuito**
3. **Código Python funciona igual** (SQLAlchemy abstrai)

### **Modificação necessária no app.py:**
```python
# Antes (SQLite local):
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emissoes.db'

# Depois (PostgreSQL produção):
import os
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///emissoes.db')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
```

## **Backup e Recuperação:**

### **SQLite (Local):**
```bash
# Backup
cp backend/emissoes.db backup_emissoes_$(date +%Y%m%d).db

# Restaurar
cp backup_emissoes_20251007.db backend/emissoes.db
```

### **PostgreSQL (Produção):**
- **Backup automático**: Railway/Render fazem diariamente
- **Point-in-time recovery**: Restaurar qualquer momento
- **Zero configuração**: Tudo automático

## **Consultas Úteis:**

### **Ver todos os dados:**
```sql
SELECT * FROM emissao_registros ORDER BY data_registro DESC;
```

### **Estatísticas por transporte:**
```sql
SELECT 
    meio_transporte,
    COUNT(*) as quantidade,
    AVG(emissao_total) as media_emissao,
    SUM(emissao_total) as total_emissao
FROM emissao_registros 
GROUP BY meio_transporte;
```

### **Ranking de emissões:**
```sql
SELECT 
    matricula,
    meio_transporte,
    emissao_total,
    categoria_emissao
FROM emissao_registros 
ORDER BY emissao_total DESC;
```

## **Capacidade e Performance:**

### **SQLite (Atual):**
- **Usuários simultâneos**: 1 (desenvolvimento)
- **Tamanho máximo**: ~280 TB (mais que suficiente)
- **Performance**: Excelente para <1000 registros

### **PostgreSQL (Produção):**
- **Usuários simultâneos**: Ilimitados
- **Tamanho**: Conforme plano (Railway: 1GB grátis)
- **Performance**: Otimizada para web

## **Segurança:**

### **SQLite**: 
- ⚠️ Arquivo local (pode ser perdido)
- ⚠️ Sem backup automático
- ✅ Simples para desenvolvimento

### **PostgreSQL**:
- ✅ Backup automático
- ✅ Criptografia em trânsito
- ✅ Controle de acesso
- ✅ Logs de auditoria

---

**Resumo**: SQLite perfeito para desenvolvimento, PostgreSQL essencial para produção! 🚀