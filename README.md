# Auto Web Click
## 背景
单位电脑一段时间后（基本都是长时间不操作，但也有在使用的时候），会被踢下线从而断网。主要妨碍下载任务无法持续进行

## 实现
通过python的selenium实现在主页添加用户名和密码，然后点击登录，实现断线后重新登陆连接到互联网的功能

## 安装
1. 需要一个 python3 的环境
2. 下载 edge（chrome 同理）浏览器驱动到**根目录** [Microsoft Edge WebDriver - Microsoft Edge Developer](!https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) 
3. 新建一个secret文件，初始化USERNAME，PASSWORD，HOME_PAGE
4. 安装 selenium4 及以上的 package
```shell
pip install -r requirements.txt
```
5. main.py 脚本后台运行
```shell
# Windows( powershell )
pythonw.exe main.py
# Linux
nohup python main.py & 
```