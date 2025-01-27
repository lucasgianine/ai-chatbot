import os

from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader, PyPDFLoader

api_key = 'YOUR_GROQ_API_KEY'
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='GROQ_MODEL')

def response_bot(messages, documents):
  system_prompt = '''Você é um assistente amigável que vai responder o usuário baseado nos dados que receber.
  Você utiliza as seguintes informações para formular as suas respostas:
  {documents}'''

  model_message = [('system', system_prompt)]
  model_message += messages

  template = ChatPromptTemplate.from_messages(model_message)

  chain = template | chat
  return chain.invoke({'documents': documents}).content

def load_website_content():
  url = input('🔗 Insira a URL do website: ')

  loader = WebBaseLoader(url)
  pages_content = loader.load()

  all_content = ''
  for doc in pages_content:
    all_content += doc.page_content

  return all_content

def load_pdf_content():
  path = 'PDF_PATH'
  loader = PyPDFLoader(path)
  pages_content = loader.load()

  all_content = ''
  for doc in pages_content:
    all_content += doc.page_content
  
  return all_content

def load_youtube_content():
  url = input('🔗 Insira a URL de um vídeo (Youtube): ')

  loader = YoutubeLoader.from_youtube_url(url, language=['pt'])
  pages_content = loader.load()

  all_content = ''
  for doc in pages_content:
    all_content += doc.page_content
  
  return all_content

username = input('Digite o seu nome: ')

init_text = f'''Olá, {username}! Vamos começar a conversar?

Escolha uma das opções abaixo:
1. Conversar com contexto de um site
2. Conversar com contexto de um PDF
3. Conversar com contexto de um vídeo de Youtube
x. Sair

👤 {username}: '''

while True:
  user_choice = input(init_text)

  try:
    if user_choice == '1':
        document = load_website_content()
        break
    elif user_choice == '2':
        document = load_pdf_content()
        break
    elif user_choice == '3':
        document = load_youtube_content()
        break
    elif user_choice == 'x':
        break
    else:
        print('Valor incorretor. Tente novamente.') 
  except:
    print(f'Houve um erro, tente novamente.\n')
  else:
     print('Conteúdo do site carregado com sucesso!\nPronto para conversar com o chatbot.\n')  

messages = []
while True:
  question = input(f'👤 {username}: ')
  if question.lower() == 'x':
    break
  messages.append(('user', question))
  response = response_bot(messages, document)
  messages.append(('assistant', response))
  print(f'🤖 Bot: {response}')

print('Espero conversar com você novamente!\nMuito obrigado por usar o chat!\n')
