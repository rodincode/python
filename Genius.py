# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:43:59 2019

@author: LENOVO
"""
x
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot= ChatBot("Genius")
trainer=ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
while True:
    userinput= input("Enter Your Query: ")
    bot_response= bot.get_response(userinput)
    print("Genius:", bot_response)