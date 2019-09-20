# -*- coding: utf-8 -*-
import random
import time
from threading import Thread

eng_list = {
    'Hello!',
    'What is your name?',
    'How old are you?',
    'Where are you from?',
    'What is your favorite moovie?',
    'I dont understand you. I should have talk with someone else.'
}

rus_list = {
    'Привет',
    'Я понимаю тебя, но не умею писать по-английски',
    'Попробуй использовать гугл-переводчик!',
    'Ну давай пообщаемся, я хочу улучшить английский',
    'Я читал, что общаться с носителем языка полезно для изучения английского',
    'Я как собака, все понимаю, но не могу ответить',
    'Похоже, мы не сможем пообщаться. Пока!'
}

STOP_PHRASES = ['I dont understand you. I should have talk with someone else.', 'Похоже, мы не сможем пообщаться. Пока!']
STOP_FLAG = False

class MyThread(Thread):

    def __init__(self, name, phrases):
        Thread.__init__(self)
        self.name = name
        self.phrases = phrases
    
    def run(self):
        global STOP_FLAG
        global STOP_PHRASES
        while not STOP_FLAG:
            amount = random.randint(1,3)
            time.sleep(amount)
            msg = random.choice(tuple(self.phrases))
            print(msg)
            self.phrases.discard(msg)
            if msg in STOP_PHRASES:
                STOP_FLAG = True
                break


def dialog():
    eng_thread = MyThread('eng', eng_list)
    rus_thread = MyThread('rus', rus_list)
    eng_thread.start()
    rus_thread.start()
 
 
if __name__ == "__main__":
    dialog()