Telegram Bot de Liguangem Natural (trainner);

Código em andamento;


questão: falta integrar o bot de linguagem natual juntamente ao bot de linguagem programada, não sei ainda se coloco junto ao código ou num programa separado e importá - lo.


primeira situação: 
os testes que foram feitos com o código de linguagem natural foram diferentemente ao do código de linguagem programada(que fiz no meu windows), pois ambos os códigos estão separados e, fiz por opção em ambiente controlado em uma máquina virtual Linux, mas os comandos para corrigir erro inicial do código podem ser feitos também no windows.

para corrigir dependência e reconhecer os modos de apredizado ou comandos para o bot:
comandos iniciais no shell linux:

[sudo] pip3 install telepot chatterbot

teste para o comando telepot: no próprio shell digite python3 para entrar no shell pythonv3, em seguida import telepot, se não vir nenhum erro, então a instalação dessa biblioteca esta feita.
por final, exit() e enter que sairá do shell py.

[sudo] pip3 install -U spacy
[sudo] python3 -m spacy download en
[sudo] python3 -m spacy download pt

isso para que seja reconhecida no código o módulo de aprendizado chatterbot para as linhas:
import telebot
from chatterbot import ChatBot #name_bot
from chatterbot.trainers import ListTrainer

dúvidas relacionadas a comandos e passos de programação de bot: https://chatterbot.readthedocs.io/en/stable/

