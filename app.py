from telebot import types
import telebot
import re
from YTSaver import Downloader

import os
from AutoLog import log 
import json  
config={}
with open('config.json') as file: 
    config = json.load(file) 
bot = telebot.TeleBot(config["token"], parse_mode='Markdown')

def is_valid_youtube_url(link: str) -> bool:
    pattern = re.compile(
        r'^(https?://)?(www\.)?'
        r'(youtube\.com/(watch\?v=|embed/|shorts/)'
        r'|youtu\.be/)'
        r'([a-zA-Z0-9_-]{11})(\S*)$'
    )
    
    return bool(pattern.match(link))

def IsHaveAccess(userId:int):
    if config["allow_for_all"]==True:
        return True
    elif userId in config["accept_ids"]:
        return True
    else:
        return False

@bot.message_handler(content_types=['text', 'document', 'audio', 'photo'])
def get_text_messages(message):
    if not IsHaveAccess(message.from_user.id):
        bot.send_message(message.from_user.id, "Извините, вы не имеете доступ к этому боту. Чтобы получить доступ свяжитесь с @redabyq, и пришлите ему свой  Telegram ID ")
        log("r",f"Попытка доступа к боту \nID ={message.from_user.id}")
    elif is_valid_youtube_url(message.text):
        log("g","URL подходит")
        video = Downloader(message.text)
        if video.getlength()>config["videolimit"]:
            bot.send_message(message.from_user.id, "Видео слишком долгое!")
        else:
            qMarkup= types.ReplyKeyboardMarkup(row_width=2)
            quarr = video.getqualities()
            for quality in quarr:  
                btn= types.KeyboardButton(quality)
                qMarkup.add(btn)
            qMarkup.add("🎵Аудио")
            photo = open(video.downloadpreview(), 'rb')
            last=bot.send_photo(message.from_user.id, photo, caption=video.getname(),reply_markup=qMarkup)
            photo.close()
            os.remove(photo.name)
            bot.register_next_step_handler(last, lambda m: choose_quality(m, video))

    else:
        log("r","URL подходит")
        bot.send_message(message.from_user.id, "Сообщение не является ссылкой ютуб")

def choose_quality(message,video):
    quarr = video.getqualities()
    if message.text in quarr:
        videosend = open(video.downloadmp4(message.text), 'rb')
        bot.send_video(message.from_user.id, videosend,reply_markup=types.ReplyKeyboardRemove())
        videosend.close()
        os.remove(videosend.name)
    elif message.text=="🎵Аудио":
        audioosend = open(video.downloadmp3(), 'rb')
        bot.send_audio(message.from_user.id, audioosend,reply_markup=types.ReplyKeyboardRemove())
        audioosend.close()
        os.remove(audioosend.name)
    else:
        get_text_messages(message) 
bot.polling(none_stop=True)
