import telebot
import time
import requests
import json
import requests
from bs4 import BeautifulSoup

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
    /help               查看帮助
    /search [CVE ID]    
    /cvetoday                   '''
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
    url = ("https://api.msrc.microsoft.com/sug/v2.0/zh-cn/vulnerability/" + user_input)
    data = requests.get(url).json()
    ###
    vlun_number = data["cveNumber"]

    vlun_info = BeautifulSoup(data["description"], "html.parser").get_text(strip=True)

    #print(BeautifulSoup(data["description"], "html.parser").get_text(strip=True))
    vlun_type = data["cveTitle"]
    ### Massage to send to user
    CVE_info = f"""
    CVE Number:{vlun_number}
    --------------------------------
    CVE Type:
    {vlun_type}
    --------------------------------
    CVE Info:
    {vlun_info}"""
    bot.send_message(message.chat.id, CVE_info)



if __name__ == '__main__':
#Use a while loop to slove Telegram server kick Bot in an hour
    print("[*] Bot is running now...")
    bot.polling()
