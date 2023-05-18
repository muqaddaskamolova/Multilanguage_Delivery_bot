from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def generate_send_contact_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_send_contact = KeyboardButton(text="Send Contact 📲", request_contact=True)
    markup.add(btn_send_contact)
    return markup


def generate_submitting_user_data():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_yes = KeyboardButton(text="Yes ✅")
    btn_no = KeyboardButton(text="No ❌")
    markup.add(btn_yes, btn_no)
    return markup


def generate_languages():
    markup = InlineKeyboardMarkup(row_width=1)
    btn_ru = InlineKeyboardButton(text='Russian 🇷🇺', callback_data='ru')
    btn_uz = InlineKeyboardButton(text='Uzbek 🇺🇿', callback_data='uz')
    btn_en = InlineKeyboardButton(text='English 🇬🇧', callback_data='en')
    btn_tr = InlineKeyboardButton(text='Turkish 🇹🇷', callback_data='tr')
    markup.add(btn_ru,btn_uz,btn_en, btn_tr)
    return markup

