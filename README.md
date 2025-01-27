# AI Chatbot - Bot conversacional
Esse projeto foi desenvolvido através de uma trilha de Python na [Asimov Academy](https://asimov.academy/curso-gratuito-ia/).

Inicie o projeto instalando as bibliotecas:
```python
%pip install langchain==0.3.0
%pip install langchain-groq==0.2.0
%pip install langchain-community==0.3.0
%pip install youtube_transcript_api==0.6.2
%pip install pypdf==5.0.0
```

Obtenha um modelo de LLM e uma chave de API para usar modelos gratuítos da Groq: [https://console.groq.com/keys](https://console.groq.com/keys) 

Altere os valores dos campos abaixo:
```python
api_key = 'YOUR_GROQ_API_KEY'
chat = ChatGroq(model='GROQ_MODEL')
```

Acesse `index.ipynb` para rodar o projeto sem instalar o Python.

## Certificado de conclusão
[Acesso ao certificado](https://hub.asimov.academy/validar-certificado/a297be1a-88a9-4381-9a42-9d93f2e94c2e/)