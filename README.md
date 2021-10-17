# Vlun-Finder-bot

# 简介
这是一个用于帮助你查找相关CVE漏洞的Telegram Bot。

使用pyTelegramBotApi制作。

所有漏洞查询结果将来自微软应急响应中心[传送门](https://microsoft.com/msrc)

# 使用方法
## 指令
* /help            显示帮助信息
* /search [CVE ID] 搜索一个CVE漏洞的信息(示例：/search CVE-2020-0796)

## 如何部署
```shell
pip install -r requirements.txt
python Start-Bot.py
```

# 更新日志
2020.10.17 完成漏洞搜索的功能
