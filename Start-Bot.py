import telebot
import time
import requests
import re

#You's bot API key
API_KEY = ''
#Create an instance for this bot
bot = telebot.TeleBot(API_KEY)

#Some fuction
def extract_arg(arg):
    return arg.split()[1:]

#Bot commands
## '/help' Command
@bot.message_handler(commands=['help'])
def send_help(message):
    help_info ='''使用说明：
    - CVE漏洞查询机器人，用于查询相关CVE漏洞信息和可利用的EXP

    命令列表：
    /help    查看帮助
    /evepost 获取每日最新更新的CVE漏洞

    更新日志：
    完成'/help'命令的相关信息
    '''
    bot.send_message(message.chat.id, help_info)

## '/cvetoday' Command
@bot.message_handler(commands=['cvetoday'])
def post_new_cve_info(message):
    bot.send_message(message.chat.id, 'please wait.....')

##'/search' Command
@bot.message_handler(commands=['search'])
def yourCommand(message):
    parameter = extract_arg(message.text)
    user_input = "".join(parameter)
    URL = 'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword='+ user_input
    r = requests.get(URL)
    web_get = r.text
    ### Massage to send to user
    CVE_info = '''

    '''
    bot.send_message(message.chat.id, CVE_info)




#Use a while loop to slove Telegram server kick Bot in an hour
bot.polling()
