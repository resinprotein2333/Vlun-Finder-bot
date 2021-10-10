import telebot
import time
import requests

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

##
@bot.message_handler(commands=['search'])
def yourCommand(message):
    user_parameter = extract_arg(message.text)
    str(user_parameter)
    bot.send_message(message.chat.id, 'Searching please wait.....')
    URL = 'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=', user_parameter
    r = requests.get(URL)
    bot.send_massage(massage.chat.id, r.text)




#Use a while loop to slove Telegram server kick Bot in an hour
bot.polling()
