from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def help(bot, update):
    update.message.reply_text("""
Commands:
/newrig = ~something interactive here
/myrig  = display complete content
/my$part  = display only $part
/rig @$user = view rig of user $user
/rigpic = ~something interactive that waits for picture input
""")

updater = Updater('token')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
updater.idle()
