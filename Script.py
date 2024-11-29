class script(object):
    START_TXT = """<b>𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈</b>"""
    
    HELP_TXT = """<b>𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂.</b>"""


# ⚠️ Please don't change our source code 👇🏻

    ABOUT_TXT = """<b>✯ Mʏ Nᴀᴍᴇ: {}
✯ Cʀᴇᴀᴛᴏʀ: <a href='tg://settings'>Tʜɪs ᴘᴇʀsᴏɴ</a>
✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
✯ Dᴇᴠᴏʟᴏᴘᴇʀ: <a href='https://t.me/wudixh13'>Goutham S E R</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
✯ DᴀᴛᴀBᴀsᴇ: <a href='https://www.mongodb.com/'>MᴏɴɢᴏDB</a>
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='https://t.me/quickfastt'>Qᴜɪᴄᴋ Fᴀsᴛ</a>
✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v2.0.3 [ Sᴛᴀʙʟᴇ ]</b>"""

    SOURCE_TXT = """<b>ɴᴏᴛᴇ:
- ꜱᴏᴜʀᴄᴇ - ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɴᴏᴛ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ
Dᴇᴠᴇʟᴏᴘᴇʀ:
- <a href="https://t.me/wudixh13">Gᴏᴜᴛʜᴀᴍ ᠰSᴇʀ</a></b>"""

    MANUELFILTER_TXT = """ʜᴇʟᴘ: <b>ꜰɪʟᴛᴇʀꜱ</b>
- ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ
<b>ɴᴏᴛᴇ:</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""

    BUTTON_TXT = """ʜᴇʟᴘ: <b>ʙᴜᴛᴛᴏɴꜱ</b>
- ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ
<b>ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonurl:https://t.me/DQ_The_File_Donor_Updates)</code>
<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""
    
    AUTOFILTER_TXT ="""Help: <b>Auto Filter</b>

<b>NOTE:</b>

<b>𝟷. 𝙼𝙰𝙺𝙴 𝙼𝙴 𝚃𝙷𝙴 𝙰𝙳𝙼𝙸𝙽 𝙾𝙵 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙸𝙵 𝙸𝚃'𝚂 𝙿𝚁𝙸𝚅𝙰𝚃𝙴.
𝟸. 𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙳𝙾𝙴𝚂 𝙽𝙾𝚃 𝙲𝙾𝙽𝚃𝙰𝙸𝙽𝚂 𝙲𝙰𝙼𝚁𝙸𝙿𝚂, 𝙿𝙾𝚁𝙽 𝙰𝙽𝙳 𝙵𝙰𝙺𝙴 𝙵𝙸𝙻𝙴𝚂.
𝟹. 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝚃𝙷𝙴 𝙻𝙰𝚂𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙼𝙴 𝚆𝙸𝚃𝙷 𝚀𝚄𝙾𝚃𝙴𝚂.
𝙸'𝙻𝙻 𝙰𝙳𝙳 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙼𝚈 𝙳𝙱.</b>

<b>★ /set_template - 𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙵𝙾𝚁 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>
<b>★ /get_template - 𝙶𝙴𝚃 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙾𝙵 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>
<b>★ /autofilter on - 𝙴𝙽𝙰𝙱𝙻𝙴 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>
<b>★ /autofilter off - 𝙳𝙸𝚂𝙰𝙱𝙻𝙴𝙳 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>"""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Elsa

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /grp_broadcast - <code>to broadcast a message to all groups</code>
• /gfilter - <code>group filter</code>
• /setskip - <code>skip no of files before indexing</code>"""
    
    STATUS_TXT = """<b>★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱</b>"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    FILE_MSG = """
<b>Hai 👋 {} </b>😍

<b>📫 Your File is Ready</b>

<b>📂 Fɪʟᴇ Nᴀᴍᴇ</b> : <code>{}</code>              
                       
<b>⚙️ Fɪʟᴇ Sɪᴢᴇ</b> : <b>{}</b>
"""
    CHANNEL_CAP = """
<b>Hai 👋 {}</b> 😍

<code>{}</code>

⚠️ <b>This file will be deleted from here within 10 minute as it has copyright ... !!!</b>

<b>കോപ്പിറൈറ്റ് ഉള്ളതുകൊണ്ട് ഫയൽ 10 മിനിറ്റിനുള്ളിൽ ഇവിടെനിന്നും ഡിലീറ്റ് ആകുന്നതാണ് അതുകൊണ്ട് ഇവിടെ നിന്നും മറ്റെവിടെക്കെങ്കിലും മാറ്റിയതിന് ശേഷം ഡൗൺലോഡ് ചെയ്യുക!</b>

<b>© Powered by {}</b>
"""
    SUR_TXT = """
<b>
𝙷𝙴𝙻𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 
</b>
"""

    IMDB_TEMPLATE_TXT = """
<b>🔖 ᴛɪᴛʟᴇ :<a href={url}>{title}</a>

🎭 ɢᴇɴʀᴇs : {genres}
🎖 ʀᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10 (ʙᴀsᴇᴅ ᴏɴ {votes} ᴜsᴇʀ ʀᴀᴛɪɴɢ.)

📆 ʏᴇᴀʀ : {release_date}
🗞 ʟᴀɴɢᴜᴀɢᴇ : {languages}
🌎 ᴄᴏᴜɴᴛʀʏ : {countries}
📖 sᴛᴏʀʏ : {plot} 

©{message.chat.title}</b>
"""

    CUSTOM_FILE_CAPTION = """<b>📂Fɪʟᴇɴᴀᴍᴇ : {file_name}

╔════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
▫️<a href=https://t.me/wudixh> ᴍᴏᴠɪᴇ ʜᴜʙ </a>
▫️<a href=https://t.me/wudixh13> Kuttu Bot Update </a>
╚════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝</b>""" 

    RESTART_TXT = """
    Kuttu Bot 2 ✅
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !
📅 Dᴀᴛᴇ : <code>{}</code>
⏰Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""

    ALRT_TXT = """Tʜɪs ɪs ɴᴏᴛ ғᴏʀ ᴜ sᴇʀ😊"""

    OLD_ALRT_TXT = """𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧 @im_kuttu_bot"""

    TOP_ALRT_MSG = """♻️ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"""

    MVE_NT_FND = """<b>Tʜɪs Mᴏᴠɪᴇ Is Nᴏᴛ Yᴇᴛ Rᴇᴀʟᴇsᴇᴅ Oʀ Aᴅᴅᴇᴅ Tᴏ DB</b> """

    NORSLTS = """★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★
𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>
"""
    


    MINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ
ᴇxᴀᴍᴘʟᴇ : Uncharted
🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ
ᴇxᴀᴍᴘʟᴇ : Loki S01E01
🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""
    
    

    I_CUDNT = """𝑯𝑬𝑳𝑳𝑶 {} 𝑰 𝑪𝑶𝑼𝑳𝑫𝑵'𝑻 𝑭𝑰𝑵𝑫 𝑨𝑵𝒀 𝑴𝑶𝑽𝑰𝑬 𝑰𝑵 𝑻𝑯𝑨𝑻 𝑵𝑨𝑴𝑬 ."""

    I_CUD_NT = """𝑯𝑬𝑳𝑳𝑶 {} 𝑰 𝑪𝑶𝑼𝑳𝑫𝑵'𝑻 𝑭𝑰𝑵𝑫 𝑨𝑵𝒀𝑻𝑯𝑰𝑵𝑮 𝑹𝑬𝑳𝑨𝑻𝑬𝑫 𝑻𝑶 𝑻𝑯𝑨𝑻 . 𝑪𝑯𝑬𝑪𝑲 𝒀𝑶𝑼𝑹 𝑺𝑷𝑬𝑳𝑳𝑰𝑵𝑮."""
    
    CUDNT_FND = """𝑯𝑬𝑳𝑳𝑶 {} 𝑰 𝑪𝑶𝑼𝑳𝑫𝑵'𝑻 𝑭𝑰𝑵𝑫 𝑨𝑵𝒀𝑻𝑯𝑰𝑵𝑮 𝑹𝑬𝑳𝑨𝑻𝑬𝑫 𝑻𝑶 𝑻𝑯𝑨𝑻 𝑫𝑰𝑫 𝒀𝑶𝑼 𝑴𝑬𝑨𝑵 𝑨𝑵𝒀 𝑶𝑵𝑬 𝑶𝑭 𝑻𝑯𝑬𝑺𝑬?"""
    
    REPRT_MSG = """ Reported To Admin"""
    
    
    LOGO = """
    
                  
██╗░░██╗██╗░░░██╗████████╗████████╗██╗░░░██╗██████╗░░█████╗░████████╗
██║░██╔╝██║░░░██║╚══██╔══╝╚══██╔══╝██║░░░██║██╔══██╗██╔══██╗╚══██╔══╝
█████═╝░██║░░░██║░░░██║░░░░░░██║░░░██║░░░██║██████╦╝██║░░██║░░░██║░░░
██╔═██╗░██║░░░██║░░░██║░░░░░░██║░░░██║░░░██║██╔══██╗██║░░██║░░░██║░░░
██║░╚██╗╚██████╔╝░░░██║░░░░░░██║░░░╚██████╔╝██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░░╚═════╝░╚═════╝░░╚════╝░░░░╚═╝░░░




▒█▀▄▀█ ░█▀▀█ ▒█▀▀▄ ▒█▀▀▀ 　 ▒█▀▀█ ▒█░░▒█ 　 ▒█▀▀█ ▒█▀▀▀█ ▒█░▒█ ▀▀█▀▀ ▒█░▒█ ░█▀▀█ ▒█▀▄▀█ 　 ▒█▀▀▀█ 　 ▒█▀▀▀ 　 ▒█▀▀█ 
▒█▒█▒█ ▒█▄▄█ ▒█░▒█ ▒█▀▀▀ 　 ▒█▀▀▄ ▒█▄▄▄█ 　 ▒█░▄▄ ▒█░░▒█ ▒█░▒█ ░▒█░░ ▒█▀▀█ ▒█▄▄█ ▒█▒█▒█ 　 ░▀▀▀▄▄ 　 ▒█▀▀▀ 　 ▒█▄▄▀ 
▒█░░▒█ ▒█░▒█ ▒█▄▄▀ ▒█▄▄▄ 　 ▒█▄▄█ ░░▒█░░ 　 ▒█▄▄█ ▒█▄▄▄█ ░▀▄▄▀ ░▒█░░ ▒█░▒█ ▒█░▒█ ▒█░░▒█ 　 ▒█▄▄▄█ 　 ▒█▄▄▄ 　 ▒█░▒█"""
