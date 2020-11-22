# -*- coding: utf-8 -*-
# [sudo] pip3 install telepot chatterbot
# [sudo] pip3 install -U spacy
# [sudo] python3 -m spacy download en 
# [sudo] python3 -m spacy download pt

import telepot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot = ChatBot("IFRN/SGA")
trainer = ListTrainer(bot)

Arquivo = open("Treinamento.txt","r").readlines()
trainer.train(Arquivo)


token = telepot.Bot("1461971673:AAFCplUD52RZEU2tM47b0Mr1Xf8AmKxjZts")

print ("\nExecutando o Código...Good Luck\n")


def receber_mensagem(self):
    text = self['text']
    _id = self['from']['id']
    nome = self['from']['first_name']
    A = token.sendMessage(_id, str(bot.get_response(text)))
    
    print('id: {} \n{} > {} \nRespostaBot > {}'.format(_id,nome,text,A['text']))
    print("\n", "-" * 50)

token.message_loop(receber_mensagem)


while True:
    pass
