#!/usr/bin/python3
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import tracker
import random

telegram_bot_token = ""

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def hello(update, context):
    chat_id = update.effective_chat.id

    message = tracker.hello()
    context.bot.send_message(chat_id=chat_id, text=message)

dispatcher.add_handler(CommandHandler("hello", hello))
updater.start_polling()

def karoldance(update, context):
    chat_id = update.effective_chat.id
    frases = ["lavarte las rendijas", "visitar la porongologa", "masturbarte con cuchillos", "ponete a hervir la tetera", "Son las 420?"]
    frase = random.choice(frases)
    message = f"Karol te recomienda {frase}"
    context.bot.send_message(chat_id=chat_id, text=message)

dispatcher.add_handler(CommandHandler("karoldance", karoldance))
updater.start_polling()


def prices(update, context):
    chat_id = update.effective_chat.id
    message = ""
    response = tracker.prices()
    #message += response
    for i in response:
        message += f"#{response[i]['coin']}\nPrice: ${response[i]['price']}\nDay change: {response[i]['change_day']}\nHour Change: {response[i]['change_hour']}\n"
        #message = response
    
    context.bot.send_message(chat_id=chat_id, text=message)

dispatcher.add_handler(CommandHandler("prices", prices))
updater.start_polling()

def price(update, context):
    chat_id = update.effective_chat.id
    #if len(context.args) > 1:
    message = tracker.price(str(context.args[0]))
    context.bot.send_message(chat_id=chat_id, text=message)

dispatcher.add_handler(CommandHandler("price", price))
updater.start_polling()

def low(update, context):
    chat_id = update.effective_chat.id
    #if len(context.args) > 1:
    message = tracker.low(str(context.args[0]))
    context.bot.send_message(chat_id=chat_id, text=message)

dispatcher.add_handler(CommandHandler("low", low))
updater.start_polling()

def high(update, context):
    chat_id = update.effective_chat.id
    #if len(context.args) > 1:
    message = tracker.high(str(context.args[0]))
    context.bot.send_message(chat_id=chat_id, text=message)

dispatcher.add_handler(CommandHandler("high", high))
updater.start_polling()

def mktcap(update, context):
    chat_id = update.effective_chat.id
    #if len(context.args) > 1:
    message = tracker.mktcap(str(context.args[0]))
    context.bot.send_message(chat_id=chat_id, text=message)

dispatcher.add_handler(CommandHandler("mktcap", mktcap))
updater.start_polling()


def commands(update, context):
    chat_id = update.effective_chat.id
    message = "Commands:\n/prices\n/hello\n/price <COIN>\n/high <COIN>\n/low <COIN>\n/mktcap <COIN>\n/karoldance\n"
    context.bot.send_message(chat_id=chat_id, text=message)

dispatcher.add_handler(CommandHandler("help", commands))
updater.start_polling()
