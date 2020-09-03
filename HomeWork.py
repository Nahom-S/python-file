
# -*- coding: UTF8 -*-
import requests
from homeworks_list import *
import datetime
import time
import random
import pickle

sec = 30


valid_student = []


def isnumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

idlist = ['11', '12']
update = []



class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update

# j1126444202:AAFEocip8xeq2e4dPBe5z-RGu_32fxgKu4K  ----- Dollar my biir bot
# randid = random.randint(1, 100000000000)
# '1308190534:AAEujx7L21ozfTnNOYS10D4Mc1USArcVvRk'

token =''#Token of your bot
homework_bot = BotHandler(token) #Your bot's name


def main():
    new_offset = 0
    print('Homework is online...')


    while True:
        all_updates=homework_bot.get_updates(new_offset)
        valid = False

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text == "/start":
                    homework_bot.send_message(first_chat_id, "Hello " + first_chat_name + " Please enter your id.")
                    homework_bot.send_message(first_chat_id,"Use the command /help if you have any questions.")
                    new_offset = first_update_id + 1
                elif first_chat_text in idlist and first_chat_id not in valid_student:
                    homework_bot.send_message(first_chat_id, "Succesfully logged in.Use the command /check to check your homeworks")
                    homework_bot.send_message(first_chat_id,"Use the command /help if you have any questions.")
                    new_offset = first_update_id + 1
                    valid_student.append(first_chat_id)
                elif first_chat_text.lower() == "/help" or first_chat_text.lower() == "help":
                    homework_bot.send_message(first_chat_id, "-->To start the service you must enter in your  special code that is valid for a month"
                                                             "\n-->You can Buy your code from represenatatives in your class Just for 15 birr per month!"
                                                              "\n-->This bot will help you do your homeworks efficiently"
                                                             "\n-->This is the official Bot for Social Science Students @SocialGotHomeworkbot")
                    new_offset = first_update_id + 1
                elif first_chat_id in valid_student:
                    if first_chat_text.lower() == "check" or first_chat_text.lower() == "/check":
                        homework_bot.send_message(first_chat_id,"Here are today's homeworks")
                        homework_bot.send_message(first_chat_id, maths_homework)
                        homework_bot.send_message(first_chat_id, phy_homework)
                        new_offset = first_update_id + 1
                        homework_bot.send_message(first_chat_id, "To set a 1 hour reminder use the command /remindme")
                    elif first_chat_text.lower() == "/remindme":
                        homework_bot.send_message(first_chat_id, "Reminder set for 1 hour from now")
                        if True:
                            for i in range(sec):
                                time.sleep(1)
                        for x in range(3):
                            homework_bot.send_message(first_chat_id, "Do your homework!!..")
                        new_offset = first_update_id + 1
                    elif first_chat_text in idlist:
                        homework_bot.send_message(first_chat_id,"You are already logged in.")
                        new_offset = first_update_id + 1
                    else:
                        homework_bot.send_message(first_chat_id, "Sorry, Unknown command.")
                        new_offset = first_update_id + 1

                else:
                    homework_bot.send_message(first_chat_id, "Sorry, Unknown command."
                                                             "Seems like you are not logged in try logging in with your code!!"
                                              )
                    new_offset = first_update_id + 1



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

