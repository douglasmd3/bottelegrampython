# a ideia de trazer os resultados do menu por um arquivo externo (txt) é evitar o excesso de strigs no código e, conseguentemente sua extensão L48/49 e L60/61.
# Bot de linguagem programada - (menu)

import requests
import time
import json
import os
 
class TelBot:
  
  def __init__(self):
    token = '1461971673:AAFCplUD52RZEU2tM47b0Mr1Xf8AmKxjZts'
    self.url_telegram = f'https://api.telegram.org/bot{token}/'

  def StartBot(self):
    update_id = None
    while True:
      start = self.GetMessage(update_id)
      result = start['result']
      if result:
        for posts in result:
          update_id = posts['update_id']
          chat_id = posts['message']['from']['id']
          FirstMessage = posts['message']['message_id'] == 1
          Answer = self.GetAnswer(posts, FirstMessage)
          self.response(Answer, chat_id)

  def GetMessage(self, update_id):
    request = f'{self.url_telegram}getUpdates?timeout=100'
    if update_id:
      request = f'{request}&offset={update_id + 1}'
    result_request = requests.get(request)
    return json.loads(result_request.content)

  def GetAnswer(self, posts, FirstMessage):
    posts = posts['message']['text']

    if FirstMessage == True:
      return f'''Olá, digite "menu" e veja as opções de atendimento'''

# em menu não coloquei opções de número e sim strings para não ter conflito com um submenu já existente numérico(linha 60/61) que responde a opção -> fones e o número retorna a linha do arquivo contatos.txt;     
    if posts.lower() == 'menu':
      return f'''digite os seguintes comandos:{os.linesep}"fones" - para visualizar os contatos institucionais{os.linesep}"chat" - para visualizar/conversar com pessoal atendente no telegram{os.linesep}"outros" - para sugestão de criação de outros comandos de atendimento'''

    if posts.lower() == 'fones':
      return f'''Segue a lista de Contatos dos Setores Institucionais{os.linesep}Por Favor insira o dígito correspondente ao contato do setor desejado.{os.linesep}\n0 - Coordenação de Administração Escolar|COADES/SGA{os.linesep}\n1 - Coordenação de Atividades Estudantis|COAES/SGA{os.linesep}\n2 - Coordenação de Apoio Acadêmico|COAPAC/SGA{os.linesep}\n3 - Coordenação de Comunicação Social e Eventos|COCSEV/SGA{os.linesep}\n4 - Coordenação de Extensão|COEX/SGA{os.linesep}\n5 - Coordenação de Finanças e Contratos|COFINC/SGA{os.linesep}\n6 - Coordenação de Gestão de Pessoas|COGPE/SGA{os.linesep}\n7 - Coordenação de Laboratórios|COLAB/SGA{os.linesep}\n8 - Coordenação de Material e Patrimônio|COMPAT/SGA{os.linesep}\n9 - Coordenação de Multimeios|COMULT/SGA{os.linesep}\n10 - CONSELHO ESCOLAR DO CAMPUS SÃO GONÇALO DO AMARANTE|CONSESC/SGA{os.linesep}\n11 - Coordenação de Pesquisa e Inovação|COPEIN/SGA{os.linesep}\n12 - Coordenação de Serviços Gerais e Manutenção|COSGEM/SGA{os.linesep}\n13 - Coordenação de Tecnologia da Informação|CTI/SGA{os.linesep}\n14 - DIREÇÃO-GERAL DO CAMPUS SÃO GONÇALO DO AMARANTE|DG/SGA{os.linesep}\n15 - Diretoria Acadêmica|DIAC/SGA{os.linesep}\n16 - Diretoria de Administração|DIAD/SGA{os.linesep}\n17 - Gabinete|GABIN/SGA{os.linesep}\n18 - Secretaria Acadêmica|SEAC/SGA'''

# ok está quase do jeito desejado - imprimir todas as opções sem formato de discionário - corrigir essa bagaça - intenção é trazer do arquivo chat.txt todo o conteúdo, não conseguir ainda no formato desejado;
# o arquivo chat.txt tem um única linha, não conseguir colocar de forma organizada as linhas como o arquivo contato.txt, pois irá imprimir a primeira linha e não retornará todas elas que é a intenção.

    if posts.lower() == 'chat':
      arquivo = open("chat.txt", "r", encoding='utf-8')
      for i in arquivo.readlines()[0:2]:
        A = i.split(";")
        return  str(A)
        
    if posts.lower() == 'outros':
      return f'''outros para sugestão de criação de outros comandos de atendimento - comando sem código programado...'''# outras opções de menu;

# problema no posts, se posts for string(é uma string no código, mas nessa parte precisa retornar como int - numero da linha do arquivo para retornar o resultado - acha que é uma gambiarra não sei se é problema) como passar por aki...(essa parte do programa) ou numero fora do intervalo de linhas do arquivo contatos.txt dará erro...a linha não existe que resultado trazer?
#(RESOLVIDO - coloquei as opções separadamente como string e convertento na parte do código um int), estava pondo um intervalo (posts >= 0 or posts <= 18), mas não conseguir converter isso como int;
    if posts == '0' or posts == '1' or posts == '2' or posts == '3' or posts == '4' or posts == '5' or posts == '6' or posts == '7' or posts == '8' or posts == '9' or posts == '10' or posts == '11' or posts == '12' or posts == '13' or posts == '14' or posts == '15' or posts == '16' or posts == '17' or posts == '18' or posts == '19' :
      arquivo = open("contatos.txt", "r", encoding='utf-8')
      A = arquivo.readlines()[int(posts)]
      m = A.split(";")
      primeiro = str(m[0])
      segundo = str(m[1])
      terceiro = ("{}\n{}".format(primeiro,segundo))
      return terceiro
      arquivo.close()

    else:
      return f'''Olá, seja bem-vindo(a) ao atendimento digital da instituição IFRN, São Gonçalo do Amarante.{os.linesep}\nConsulte as  opçções de atendimento digitando "menu"'''
  
# para o else inser   else:
#      return f'''Olá, seja bem-vindo(a) ao atendimento digital da instituição IFRN, São Gonçalo do Amarante.{os.linesep}\nConsulte os contatos dos setores da instituição à qual desejas.{os.linesep}\nDigite "menu" para visualizar os contatos.'''
# Sugestão dentro do else posso colocar o codigo de linguagem natural - tudo que não for por comandos não programados passa por esse caminho...
# Situação: mesmo que a pessoa diga algo tem - se que apresentar ao usuário os comando para se chegar no menu de opção ou código de linguagem programada.

  print ("Código em execução - Teste - o no Telegram....")
    
  def response(self, Answer, chat_id):
    SendLink = f'{self.url_telegram}sendMessage?chat_id={chat_id}&text={Answer}'
    requests.get(SendLink)
    
Bot = TelBot()
Bot.StartBot()
