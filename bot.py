{\rtf1\ansi\ansicpg1251\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import telebot\
from telebot import types\
\
API_TOKEN = '7363983862:AAFfBDYx3AhPTJ0_f3hzkfIFUuTDYPb8IJY'\
bot = telebot.TeleBot(API_TOKEN)\
\
# Dictionary to store anonymous pairs\
anonymous_pairs = \{\}\
\
# Start command\
@bot.message_handler(commands=['start'])\
def start(message):\
    markup = types.ReplyKeyboardMarkup(row_width=1)\
    join_btn = types.KeyboardButton('\uc0\u55357 \u56589  Join Anonymous Chat')\
    markup.add(join_btn)\
    bot.send_message(message.chat.id, "Welcome! Click the button to join an anonymous chat.", reply_markup=markup)\
\
# Handle text messages\
@bot.message_handler(func=lambda message: True)\
def handle_message(message):\
    if message.text == '\uc0\u55357 \u56589  Join Anonymous Chat':\
        bot.send_message(message.chat.id, "Looking for a chat partner...")\
        # Logic to pair users anonymously\
        for user_id, partner_id in anonymous_pairs.items():\
            if partner_id is None:\
                anonymous_pairs[user_id] = message.chat.id\
                anonymous_pairs[message.chat.id] = user_id\
                bot.send_message(user_id, "You have been paired with an anonymous user. Start chatting!")\
                bot.send_message(message.chat.id, "You have been paired with an anonymous user. Start chatting!")\
                return\
        anonymous_pairs[message.chat.id] = None\
    else:\
        partner_id = anonymous_pairs.get(message.chat.id)\
        if partner_id:\
            bot.send_message(partner_id, message.text)\
        else:\
            bot.send_message(message.chat.id, "You are not paired with anyone yet. Please wait.")\
\
bot.polling()}