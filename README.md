<div align="center">
<img src=https://raw.githubusercontent.com/resinprotein2333/Vlun-Finder-bot/main/icon/vlun_finder_bot_icon.png width=300 height=300 />
</div>


<div align="center">
<font size="50"> 
<p>
<b> Vlun-Finder-bot </b>
</p>
</font>
</div>

<div align="center">
<img alt="Static Badge" src="https://img.shields.io/badge/python-%233776AB?style=for-the-badge&logo=python&logoColor=white">
<img alt="Static Badge" src="https://img.shields.io/badge/telegram%20bot-%2326A5E4?style=for-the-badge&logo=telegram&logoColor=white">
<img alt="Static Badge" src="https://img.shields.io/badge/License-GPL%20v3.0-black?style=for-the-badge&logoColor=white">
</div>

## 简介

对于安全人员来说,迅速了解漏洞和其相关信息可以帮助安全人员进行及时响应,这是一个用于帮助安全人员即使查找相关CVE漏洞的信息Telegram Bot。

使用 [pyTelegramBotApi](https://github.com/resinprotein2333/pyTelegramBotAPI) 制作,所有漏洞查询数据均来自 [微软应急响应中心](https://microsoft.com/msrc)。

## 使用方法:

### 机器人指令

* /help                          显示帮助信息
* /search [CVE ID]       搜索一个CVE漏洞的信息

## 如何部署:

### 在本地部署

```shell
# 安装脚本所需的依赖
pip install -r requirements.txt

# 启动脚本
python Start-Bot.py
```

## 更新日志

2020.10.17 完成漏洞搜索的功能.

2023.10.26 因学业和无法获取新的 Bot API 的原因,此项目暂时封停.
