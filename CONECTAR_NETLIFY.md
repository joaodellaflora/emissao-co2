# 🔗 **CONECTAR NETLIFY → RAILWAY**

## 🎯 **PASSO A PASSO COMPLETO:**

### **1. Copie a URL do Railway:**
No painel do Railway, copie sua URL (algo como):
```
https://emissao-co2-production.up.railway.app
```

### **2. Atualize o frontend:**
No arquivo `frontend/public/index.js`, na **linha 3**, substitua:
```javascript
// ANTES:
const API_BASE_URL = "https://SEU-APP.railway.app";

// DEPOIS (cole sua URL):
const API_BASE_URL = "https://SUA-URL-REAL.railway.app";
```

### **3. Deploy no Netlify:**

#### **Opção A - Arrastar e soltar (MAIS FÁCIL):**
1. 🌐 Acesse: https://netlify.com
2. 📁 Faça login
3. 📂 "Add new site" → "Deploy manually" 
4. 🔸 **Arraste a pasta `frontend/public`**
5. ✅ Deploy automático!

#### **Opção B - Conectar ao GitHub:**
1. 🌐 Netlify → "Add new site" → "Import from Git"
2. 📂 Conecte ao GitHub
3. 🎯 Selecione `joaodellaflora/emissao-co2`
4. ⚙️ **Build settings:**
   - Build command: `# (deixe vazio)`
   - Publish directory: `frontend/public`
5. ✅ Deploy!

---

## 🧪 **TESTE A CONEXÃO:**

### **1. Teste o backend primeiro:**
```bash
# Substitua pela sua URL:
curl https://sua-url.railway.app/api/estatisticas
```
**Resposta esperada:**
```json
{
  "total_registros": 5,
  "emissao_total": 6.18,
  "status": "ok"
}
```

### **2. Teste o frontend:**
1. 📝 Acesse seu site no Netlify
2. 📋 Preencha o formulário
3. ✅ Clique em "Calcular Emissões"
4. 🎉 Deve salvar no Railway!

---

## 🔧 **ESTRUTURA FINAL:**

```
🌐 NETLIFY (Frontend)
├── https://seu-site.netlify.app
└── Chama API → 

🚂 RAILWAY (Backend + DB)
├── https://seu-app.railway.app
├── PostgreSQL Database
└── Dados salvos automaticamente
```

---

## ⚠️ **PROBLEMAS COMUNS:**

### **CORS Error:**
Se aparecer erro de CORS, é normal. Seu app.py já tem Flask-CORS configurado.

### **API não encontrada:**
- ✅ Verifique se a URL do Railway está correta
- ✅ Teste a API diretamente no navegador
- ✅ Confira se o Railway está rodando

### **Formulário não salva:**
- 🔍 Abra DevTools (F12) no navegador
- 👀 Veja a aba "Network" ao enviar formulário
- 📊 Verifique se a requisição está sendo feita

---

## 🎯 **RESUMO DOS PRÓXIMOS PASSOS:**

1. ✅ **Agora**: Copie URL do Railway
2. ✅ **2 min**: Atualize frontend/public/index.js 
3. ✅ **3 min**: Deploy no Netlify
4. ✅ **1 min**: Teste conexão
5. 🎉 **Sistema completo funcionando!**

**Total: ~6 minutos para ter frontend + backend conectados!**