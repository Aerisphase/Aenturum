import Aenturum as keys
from telegram.ext import *
import Responses as R

print("ЭВМ \"Иван\" начал работу на благо пролетариата...")


def start_command(update, context):
    update.message.reply_text("Напишите что-либо, чтобы восславить пролетариат")


def help_command(update, context):
    update.message.reply_text("Если нужна помощь, спроси у главы партии")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()

# @bot.message_handler(commands=['start'])
# def start(message):
#    send_mess = f"<b>Привет, {message.from_user.first_name}!</b>"
#    bot.send_message(message.chat.id, send_mess, parse_mode='html')