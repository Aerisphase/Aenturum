import telebot

bot = telebot.TeleBot('1677027173:AAFIw2tcEPAPZV5vqV-Zk5Aom0s1WOGebbQ')


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Иди к черту, {message.from_user.first_name}!</b>\nСоси"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


bot.polling(none_stop=True)
