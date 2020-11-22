# Teste
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
