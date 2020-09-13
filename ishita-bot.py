from Adafruit_IO import (Client, Feed, Data)

from telegram.ext import(Updater, CommandHandler, MessageHandler, Filters)

# importing operating system library
import os 

# Getting the data from the cloud
import requests  

x = os.getenv('x')  #ADAFRUIT_IO_USERNAME
y = os.getenv('y')  #ADAFRUIT_IO_KEY
TOKEN = os.getenv('TOKEN')  # Telegarm Token

aio = Client(x,y)

# Create a feed and give a name to your feed
new = Feed(name='bot123') 

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def start(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id, text = 'Hi I am Taffy Bot. I will help you further.\nSend /on to turn on light.\nSend /off to turn it off.\nSend /cancel to exit.\n')

def on(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id,photo=url,caption = 'Turning Lights On. A cute picture for u to see while we execute your command.')
    value = Data(value=1)
    value_send = aio.create_data('bot123',value)

def off(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id,photo=url,caption = 'Turning Lights off. A cute picture for u to see while we execute your command.')
    value = Data(value=0)
    value_send = aio.create_data('bot123',value)

def cancel(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id, text = 'It was great to be able to execute your commands. Bye!')

def unknown(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id, text = 'Sorry, I do not understand your command. Try some other command.')

def main():
    u = Updater('TOKEN')
    dp = u.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('on',on))
    dp.add_handler(CommandHandler('off',off))
    dp.add_handler(CommandHandler('cancel', cancel))
    dp.add_handler(MessageHandler(Filters.command, unknown))
    u.start_polling()
    u.idle()

if __name__ == '__main__':
    main()
