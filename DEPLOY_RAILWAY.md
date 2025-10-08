# 🚂 Deploy no Railway (Recomendado)

## Por que Railway?
- ✅ **Gratuito**: $5/mês de créditos grátis
- ✅ **Simples**: Deploy automático via GitHub
- ✅ **Banco incluído**: PostgreSQL gratuito
- ✅ **Zero configuração**: Detecta Flask automaticamente

## Passo a Passo:

### 1. Preparar o projeto
```bash
# Criar arquivo railway.json (opcional)
{
  "build": {
    "command": "pip install -r requirements.txt"
  },
  "start": {
    "command": "python app.py"
  }
}
```

### 2. Deploy
1. Acesse: https://railway.app
2. Login com GitHub
3. "New Project" > "Deploy from GitHub repo"
4. Selecione seu repositório
5. Railway detecta Flask automaticamente
6. Deploy acontece em ~2 minutos

### 3. Configurar banco
- Railway cria PostgreSQL automaticamente
- Variáveis de ambiente são injetadas
- Banco persiste entre deploys

### 4. Resultado
- Backend: https://seu-app.railway.app
- API: https://seu-app.railway.app/api/estatisticas
- Banco: Gerenciado automaticamente

## Custo:
- **Gratuito**: Até $5/mês de uso
- **Suficiente para**: ~500 usuários/mês