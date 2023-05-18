from telebot import TeleBot
from telebot.types import Message, CallbackQuery, ReplyKeyboardRemove
from configs import *
from queries import *
from keyboards import *
from utils import *

bot = TeleBot(TOKEN, parse_mode='HTML')
users_data = {}


@bot.message_handler(commands=['start'])
def command_start(message: Message) -> None:
    chat_id = message.chat.id
    insert_users_lang(chat_id)
    bot.send_message(chat_id, f"""Welcome to our online delivery Fast Food bot!""",
                     reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id, f"""Choose the language:""",
                     reply_markup=generate_languages())


@bot.callback_query_handler(lambda call: call.data in ['ru', 'uz', 'en', 'tr'])
def welcome(call: CallbackQuery):
    chat_id = call.message.chat.id
    language = call.data
    update_users_lang(telegram_id=chat_id,
                      language=language)
    user_language = get_user_lang(chat_id)
    #print(user_language)
    bot.delete_message(chat_id, message_id=call.message.id)
    bot.send_message(chat_id, text=WELCOME_MESSAGES[user_language]['message'],
                     reply_markup=ReplyKeyboardRemove())

                
# ask_full_name(message)


# registeration part
def ask_full_name(message: Message):
    chat_id = message.chat.id

    msg = bot.send_message(chat_id, f"""<b>Please, Enter your name and surname</b>""")

    bot.register_next_step_handler(msg, ask_contact)


def ask_contact(message: Message):
    chat_id = message.chat.id
    full_name = message.text
    msg = bot.send_message(chat_id, f"""<b>Please, Enter your phone number</b>""",
                           reply_markup=generate_send_contact_btn())

    bot.register_next_step_handler(msg, show_user_data, full_name)


def show_user_data(message: Message, full_name) -> None:
    chat_id = message.chat.id

    if message.content_type == 'contact':
        contact = message.contact.phone_number
    elif message.content_type == 'text':
        contact = message.text
    bot.send_message(chat_id, f"""<b> Do you confirm your information?</b>""")
    msg = bot.send_message(chat_id, f"""<b>Name and Surname:{full_name}
        Phone number:{contact}</b>""", reply_markup=generate_submitting_user_data())
    bot.register_next_step_handler(msg, submit_cancel, full_name, contact)


def submit_cancel(message: Message, full_name, contact):
    # global users_data
    chat_id = message.chat.id
    if message.text == "Yes ✅":
        insert_user(telegram_id=chat_id,
                    full_name=full_name,
                    contact=contact)
        bot.send_message(chat_id, """You have successfully submitted! 🥳🥳🥳""",
                         reply_markup=ReplyKeyboardRemove())
    elif message.text == "No ❌":
        command_start(message)


bot.polling(none_stop=True)
