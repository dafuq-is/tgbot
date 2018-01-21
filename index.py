from telegram.ext import Updater, CommandHandler, Dispatcher
import telegram, logging, requests
bot = telegram.Bot(token='your_bot_token')
updater = Updater(token='your_bot_token')
dispatcher = updater.dispatcher

def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="I'm a fucking bot, please talk to me!")

def start_callback(bot, update, args):
    user_says = " ".join(args)
    response = requests.get("https://dafuq.is/" + user_says)
    answer = response.text
    update.message.reply_text(answer)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    

dispatcher.add_handler(CommandHandler("dafuqis", start_callback, pass_args=True))
updater.start_polling()
