#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

from logging import getLogger
from telegram import Bot, Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from reply_buttons import BUTTON_LAST_RECORD, BUTTON_HELP, get_base_reply_keyboard
from msg_buttons import CALLBACK_BUTTON_GOOD, CALLBACK_BUTTON_OK, CALLBACK_BUTTON_BAD, CALLBACK_BUTTON_SEND, CALLBACK_BUTTON_DISCARD, get_inline_keyboard_health, get_inline_keyboard_confirm
from msg_texts import msg_start, msg_help, msg_echo, msg_feel, msg_feel_GOOD, msg_feel_OK, msg_feel_BAD, msg_feel_SEND, msg_feel_DISCARD, msg_temp_threshold_high, msg_hum_threshold_high, msg_hum_threshold_low, msg_gas_threshold_high 

from config import load_config
from utils import logger_factory
from server_requests import get_data, send_health_status

config = load_config()
logger = getLogger(__name__)    
debug_requests = logger_factory(logger=logger)

@debug_requests
def keyboard_callback_handler(bot, update, chat_data = None, **kwargs):
    health_status = None
    query = update.callback_query
    data = query.data

    chat_id = update.effective_message.chat_id

    if data == CALLBACK_BUTTON_GOOD:
        bot.send_message(
            chat_id = chat_id,
            text = msg_feel_GOOD,
            reply_markup = get_inline_keyboard_confirm(),
        )
        health_status = 1
    elif data == CALLBACK_BUTTON_OK:
        bot.send_message(
            chat_id = chat_id,
            text = msg_feel_OK,
            reply_markup = get_inline_keyboard_confirm(),   
        )
        health_status = 2
    elif data == CALLBACK_BUTTON_BAD:
        bot.send_message(
            chat_id = chat_id,
            text = msg_feel_BAD,
            reply_markup = get_inline_keyboard_confirm(),   
        )
        health_status = 3
    elif data == CALLBACK_BUTTON_SEND:
        bot.send_message(
            chat_id = chat_id,
            text = msg_feel_SEND,
            reply_markup = get_base_reply_keyboard(),   
        )
        status = None
        response_post_request = None
        while status != 200:
            status, data = get_data()
        while response_post_request != 200:
            response_post_request = send_health_status(health_status = health_status)

    elif data == CALLBACK_BUTTON_DISCARD:
        bot.send_message(
            chat_id = chat_id,
            text = msg_feel_DISCARD,  
        )
        do_feel(bot, update, chat_id)

@debug_requests
def do_start(bot, update, job_queue):
    chat_id = update.effective_message.chat_id
    bot.send_message(
        chat_id = chat_id,
        text = msg_start,
        parse_mode = ParseMode.HTML,
        reply_markup = get_base_reply_keyboard(),
    )
    job_queue.run_repeating(check_periodically, 300, context = update.message.chat_id)

@debug_requests
def check_periodically(bot, job):
    #we have to check is we dont have data about health for this particular inregistration yet - get it

    status = None
    while status != 200:
        status, data = get_data()
    if data["temperature"] >= 30:
        bot.send_message(
            chat_id = job.context,
            text = msg_temp_threshold_high,
        )
    if data["humidity"] >= 60:
        bot.send_message(
            chat_id = job.context,
            text = msg_hum_threshold_high,
        )
    if data["humidity"] < 40:
        bot.send_message(
            chat_id = job.context,
            text = msg_hum_threshold_low,
        )
    if data["gas"] > 300:
        bot.send_message(
            chat_id = job.context,
            text = msg_gas_threshold_high,
        )
    if data["health_status"] == 0:
        bot.send_message(
            chat_id = job.context,
            text = msg_feel,
            reply_markup = get_inline_keyboard_health(),
        )

@debug_requests
def get_last_record(bot, update, chat_id):
    status = None
    while status != 200:
        status, data = get_data()

    #and we will have to check these values on thresholds
    reply = 'Datetime of measurements - {},\nTemperature - {} °C,\nHumidity - {} %\nGas - {}'.format(data["timestamp"], data["temperature"], data["humidity"], data["gas"])
    bot.send_message(
        chat_id = chat_id,
        text = reply,
        reply_markup = get_base_reply_keyboard(),
    )

@debug_requests
def do_help(bot, update, chat_id):
    bot.send_message(
        chat_id = chat_id,
        text = msg_help,
        parse_mode = ParseMode.HTML,
        reply_markup = get_base_reply_keyboard(),
    )

@debug_requests
def do_feel(bot, update, chat_id):
    bot.send_message(
        chat_id = chat_id,
        text = msg_feel,
        reply_markup = get_inline_keyboard_health(),
    )

@debug_requests
def do_echo(bot, update):
    chat_id = update.effective_message.chat_id
    text = update.message.text

    if text == BUTTON_LAST_RECORD:
        get_last_record(bot, update, chat_id)
    elif text == BUTTON_HELP:
        do_help(bot, update, chat_id)
    else:
        reply = msg_echo
        bot.send_message(
            chat_id = chat_id,
            text = reply,
            reply_markup = get_base_reply_keyboard(),
        )

def main():
    logger.info("The bot is starting...")
    bot = Bot(
        token = config.TG_TOKEN,   
    )
    updater = Updater(
        bot = bot,
    )

    #Check if bot found TG API
    info = bot.get_me()
    logger.info(f'Bot info: {info}')

    start_handler = CommandHandler("start", do_start, pass_job_queue=True)
    message_handler = MessageHandler(Filters.text, do_echo)
    buttons_handler = CallbackQueryHandler(callback = keyboard_callback_handler, pass_chat_data = True)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(buttons_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()