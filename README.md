# Vlun-Finder-bot

<div align=center>![vlun_finder_bot](https://raw.githubusercontent.com/resinprotein2333/Vlun-Finder-bot/main/vlun_finder_bot_icon.png)

![](https://badgen.net/github/license/resinprotein2333/Vlun-Finder-bot) ![](https://badgen.net/github/stars/resinprotein2333/Vlun-Finder-bot)

# 简介
这是一个用于帮助你查找相关CVE漏洞的Telegram Bot。

使用[pyTelegramBotApi](https://github.com/eternnoir/pyTelegramBotAPI)制作，所有漏洞查询结果将来自[微软应急响应中心](https://microsoft.com/msrc)。

# 语言支持
* 中文🇨🇳 (现已支持)
* 俄语🇷🇺 (下一个版本)
* 德语🇩🇪 (下一个版本)

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
