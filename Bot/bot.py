import telebot

bot = telebot.TeleBot("5649299652:AAEcU8j4sLRxMhvxNInVev9y7nPpovf5M70")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, "Tanykeev Zhyldyzbek ")

bot.infinity_polling()