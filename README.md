![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=Welcome+To+kuTTu-boT!;Created+by+GouthamSER!;A+simple+and+powerful+Bot!;Indexes+Files+above+2GB;A+Bot+with+double+button!;Start+message+with+pic!;And+more+features!)
</p>
<p align="center">
  <img src="logo.jpg" alt="kuTTu">
</p>
<h1 align="center">
  <b>kuTTu boT</b>
</h1>

<a href="https://t.me/wudixh1">
  <img src="https://img.shields.io/badge/Join-blue?logo=telegram" width="70">
 
 

[![Stars](https://img.shields.io/github/stars/GouthamSER/TelegramBot?style=flat-square&color=yellow)](https://github.com/GouthamSER/TelegramBot/stargazers)
[![Forks](https://img.shields.io/github/forks/GouthamSER/TelegramBot?style=flat-square&color=orange)](https://github.com/GouthamSER/TelegramBot/fork)
[![Size](https://img.shields.io/github/repo-size/GouthamSER/TelegramBot?style=flat-square&color=green)](https://github.com/GouthamSER/TelegramBot)   
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/GouthamSER/TelegramBot)   
[![Contributors](https://img.shields.io/github/contributors/CrazyDeveloperTG/Doctor-Strange?style=flat-square&color=green)](https://github.com/GouthamSER/TelegramBot/graphs/contributors)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/GouthamSER/TelegramBot/blob/main/LICENSE)
[![Sparkline](https://stars.medv.io/GouthamSER/TelegramBot.svg)](https://stars.medv.io/GouthamSER/TelegramBot)
## Features

- [x] Auto Filter
- [x] Manual Filter
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB search
- [x] Inline Search
- [x] Random pics
- [x] ids and User info 
- [x] Stats, Users, Chats
- [x] Spelling Check Feature
- [x] File Store
- [x] PM & Channel 
- [x] Auto delete
- [x] 2GB+File Support
- [x] song video download
- [x] gfilter
- [x] group broadcast
- [x] telegraph
- [x] games
- [x] ping
- [x] pdf convert to voice
- [x] font
- [x] translate
- [x] PreDVD and CamRip Delete Mode
- [x] Multiple File Deletion

## Variables

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com).
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this 
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
* `SUPPORT_CHAT` : @czdbotz_support
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used seperated by space )
* `FILE_CHANNEL` : File redirect to channel
* `DELETE_CHANNELS` : you can delete multiple files by forwarding those files into a private channel. Firstly make a private channel, add your bot as admin, add that channel's ID as a variable named DELETE_CHANNELS and forward the files to that private channel and the bot will delete those files from its database. You can check logs to confirm whether the file is deleted from the bot's database or not.
### Optional Variables

## Credits
<details>

 Thanks To [Mahesh](https://github.com/Mahesh0253/Media-Search-bot) MediaSearch

 Thanks To [Subinps](https://github.com/subinps/Media-Search-bot) AutoFilter & Base repo
 
 Thanks To [Joelkb](https://github.com/Joelkb) Collaborator [Add Redirect feature,Error fixed, Add new features]


</details>

## Deploy
You can deploy this bot anywhere.


<details><summary>Deploy To Heroku</summary>
<br>
<p>
<a href="https://heroku.com/deploy?template=https://github.com/GouthamSER/TelegramBot">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p></details>

<details><summary>Deploy To Koyeb</summary>
<br>
<p>
<a href="https://app.koyeb.com/deploy?type=git&repository=github.com/GouthamSER/TelegramBot&env[BOT_TOKEN]&env[API_ID]&env[API_HASH]&env[CHANNELS]&env[ADMINS]&env[PICS]&env[LOG_CHANNEL]&env[AUTH_CHANNEL]&env[CUSTOM_FILE_CAPTION]&env[DATABASE_URI]&env[DATABASE_NAME]&env[COLLECTION_NAME]=Telegram_files&env[FILE_CHANNEL]=-1001832732995&env[SUPPORT_CHAT]&env[IMDB]=True&env[IMDB_TEMPLATE]&env[SINGLE_BUTTON]=True&env[AUTH_GROUPS]&env[P_TTI_SHOW_OFF]=True&run_command=python%20bot.py&branch=main&name=telegrambot">
 <img src="https://www.koyeb.com/static/images/deploy/button.svg">
</p>
</details>
<details><summary> Deploy To Okteto </summary>
<br>
<p>
<a href="https://cloud.okteto.com/deploy?repository=https://github.com/GouthamSER/TelegramBot&branch=main">
  <img src="https://okteto.com/develop-okteto.svg" alt="Develop on Okteto">
</a>
</p>
</details>
<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone https://github.com/GouthamSER/TelegramBot
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>

## Commands

```
* /logs - to get the rescent errors
* /stats - to get status of files in db.
* /filter - add manual filters
* /filters - view filters
* /connect - connect to PM.
* /disconnect - disconnect from PM
* /del - delete a filter
* /delall - delete all filters
* /deleteall - delete all index(autofilter)
* /delete - delete a specific file from index.
* /info - get user info
* /id - get tg ids.* /imdb - fetch info from imdb.
* /users - to get list of my users and ids.
* /chats - to get list of the my chats and ids* /broadcast - to broadcast a message to all Elsa users
* /gfilter - group filter
* /grp_broadcast - broadcast to all group
* /song - get song
* /video - get video
* /setskip - used in index where indexing a specific number
* /font - fonts for your text
```
