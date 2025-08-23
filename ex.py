from config import TOKEN
import telebot
from telebot import types

bot = telebot.TeleBot(TOKEN)


@bot.callback_query_handler(func=lambda call: call.data == 'button1')
def back_to_start(call):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)
@bot.message_handler(commands=["start"])
def start_bot(message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.first_name}! Кто я такой? Я ТГ бот, созданный @KingAMR35, который помогает людям выбирать профессию и полностью рассказать о ней. Этот бот поможет найти себя в будущем!")
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Вернуться", callback_data="button1")
    keyboard.add(button1)
    bot.send_message(message.chat.id, "Выберите поиск, чтобы начать", reply_markup=keyboard)
    






bot.infinity_polling()