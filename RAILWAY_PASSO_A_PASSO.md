# 🚂 **DEPLOY NO RAILWAY - GUIA VISUAL**

## **📋 Pré-requisitos:**
- ✅ Conta no GitHub (gratuita)
- ✅ Projeto já preparado (feito!)

---

## **🎯 PASSO 1: Subir código para GitHub**

### **Opção A: Usando Git (Recomendado)**
```bash
# No terminal do seu projeto:
cd "C:\Users\joaog\Desktop\fomulario_emissao\emissao_app (3)"

# Inicializar Git
git init

# Adicionar arquivos
git add .

# Commit
git commit -m "Projeto limpo pronto para deploy"

# Conectar ao GitHub (crie repo primeiro)
git remote add origin https://github.com/SEU_USUARIO/emissao-co2.git
git push -u origin main
```

### **Opção B: Upload Manual**
1. Acesse: https://github.com
2. Clique "New repository"
3. Nome: `emissao-co2`
4. Clique "Create repository"
5. "uploading an existing file" → Arraste a pasta backend

---

## **🎯 PASSO 2: Deploy no Railway**

### **2.1 - Criar conta:**
1. 🌐 Acesse: **https://railway.app**
2. 🔑 Clique "Login with GitHub"
3. ✅ Autorize Railway acessar seus repos

### **2.2 - Criar projeto:**
1. 📁 Clique "New Project"
2. 📂 Selecione "Deploy from GitHub repo"
3. 🎯 Escolha `emissao-co2` (ou nome do seu repo)
4. 📂 Railway detecta automaticamente:
   ```
   ✅ Python project detected
   ✅ requirements.txt found
   ✅ Flask app detected
   ```

### **2.3 - Configurar banco (AUTOMÁTICO):**
Railway detecta que você precisa de banco e:
1. 🗄️ Cria PostgreSQL automaticamente
2. 🔗 Conecta via variável `DATABASE_URL`  
3. 💾 Seu app.py já está preparado para isso!

### **2.4 - Deploy automático:**
```
🔄 Railway instala dependências...
📦 pip install -r requirements.txt
🚀 Inicia aplicação...
✅ Deploy concluído em ~2 minutos!
```

---

## **🎯 PASSO 3: Configuração Final**

### **3.1 - Ver sua URL:**
Após o deploy, Railway mostra:
```
🌐 Seu app: https://emissao-co2-production.up.railway.app
📊 API: https://emissao-co2-production.up.railway.app/api/estatisticas
```

### **3.2 - Testar API:**
```bash
# No terminal:
curl https://sua-url.railway.app/api/estatisticas
```

### **3.3 - Ver logs (se necessário):**
No painel Railway:
1. 📋 Clique na aba "Logs"
2. 👀 Veja se há erros
3. ✅ Deve mostrar "Banco de dados inicializado!"

---

## **🎯 PASSO 4: Conectar Frontend**

### **4.1 - Atualizar URL no frontend:**
No arquivo `frontend/public/index.js`, procure por:
```javascript
// Encontre algo como:
const API_URL = 'http://localhost:5000';

// Substitua por:
const API_URL = 'https://sua-url.railway.app';
```

### **4.2 - Deploy frontend no Netlify:**
1. 🌐 Acesse: https://netlify.com
2. Arraste pasta `frontend/public`
3. ✅ Pronto! Frontend conectado ao backend

---

## **🔧 Estrutura Final no Railway:**

```
📁 Seu repositório:
├── backend/
│   ├── app.py ✅
│   ├── requirements.txt ✅
│   ├── Procfile ✅ (novo)
│   └── emissoes.db (ignorado)
└── README.md
```

### **Railway irá:**
1. 📦 `pip install -r requirements.txt`
2. 🗄️ Criar PostgreSQL automaticamente
3. 🔗 Definir `DATABASE_URL` automaticamente
4. 🚀 Executar `gunicorn app:app`
5. ✅ App online 24/7!

---

## **💡 Dicas importantes:**

### **✅ O que funciona automaticamente:**
- PostgreSQL database (criado automaticamente)
- Variáveis de ambiente (`DATABASE_URL`)
- HTTPS (certificado automático)
- Logs e monitoring
- Backup automático do banco

### **⚠️ Pontos de atenção:**
- Primeira request pode ser lenta (~30s wake up)
- Plano gratuito: $5/mês créditos (suficiente para projeto pequeno)
- Dados SQLite locais não migram automaticamente

---

## **🚀 Comandos Resumidos:**

### **Se já tem Git:**
```bash
git add . && git commit -m "Deploy ready"
git push
# Depois: Railway → Deploy from GitHub
```

### **Se não tem Git:**
1. GitHub → New repo → Upload files
2. Railway → Deploy from GitHub

---

## **📞 Suporte:**
- 📚 Docs: https://docs.railway.app
- 💬 Discord: Railway community
- 🎯 Status: https://status.railway.app

**⏱️ Tempo total: 5-10 minutos para app online!**