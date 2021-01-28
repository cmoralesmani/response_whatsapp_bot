from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from selenium import webdriver

import chromedriver_binary
import re
import time 
import os


class WppBot:

    def __init__(self):
        self.nombre_contacto = "Celeste"
        # options = webdriver.ChromeOptions()
        # options.add_argument("lang=pt-br")
        self.browser = webdriver.Chrome()
        self.ultimo_texto = ''
        
    
    def whatsapp(self):
        self.browser.get('https://web.whatsapp.com/')
        time.sleep(20)

        target = self.browser.find_element_by_xpath(f"//span[@title='{self.nombre_contacto}']")
        time.sleep(3)
        target.click()

    def escucha(self):
        # Obtenemos todos los mensajes del contacto seleccionado.
        post = self.browser.find_elements_by_class_name('_1RAno')
        # Se obtiene el indice de la ultima conversación.
        ultimo = len(post) - 1
        # De esa ultima conversacion se obtiene el texto.
        # import ipdb; ipdb.set_trace()
        texto = post[ultimo].find_elements_by_css_selector('span.selectable-text') if ultimo >= 0 else ''
        self.texto = texto[len(texto)-1].text if len(texto) > 0 else ''
        return self.texto
    
    def bot(self):
        chatbot = ChatBot("Zoe")

        trainer = ChatterBotCorpusTrainer(chatbot)
        # trainer = ListTrainer(chatbot)

        trainer.train('chatterbot.corpus.spanish')
        # trainer.train('chatterbot.corpus.portuguese.conversations')
        # trainer.train([
        #     "Hola, Que tal?",
        #     "I love you.",
        #     ":)"
        # ])

        while True:
            texto = self.escucha()
            texto = str(texto)

            # if not texto: continue
            if len(texto)==0: texto = 'y entonces que onda?'
            
            if texto != self.ultimo_texto and texto[0] != ':':
                self.ultimo_texto = texto
                user_input = texto

                self.bot_response = chatbot.get_response(user_input)

                chatBox = self.browser.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')

                time.sleep(3)
                chatBox.click()
                chatBox.send_keys(":" + str(self.bot_response))

                boton_enviar = self.browser.find_element_by_xpath("//span[@data-icon='send']")
                time.sleep(3)

                boton_enviar.click()
                time.sleep(5)


bot = WppBot()
bot.whatsapp()
time.sleep(30)
bot.bot()
