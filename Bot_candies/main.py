from distutils.command.config import config
import logging

import config
import model


from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters

logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.DEBUG
)
logger = logging.getLogger(__name__)

candy = 0



play_handler = ConversationHandler(
    entry_points = [CommandHandler('play', model.play)],

    states = {
        1:[MessageHandler(Filters.text & ~Filters.command, model.play_get_candy)],
        2:[MessageHandler(Filters.text & ~Filters.command, model.player_1)],
    },

    fallbacks = [CommandHandler('stop', model.stop)]

)

def main():
    updater = Updater(config.TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", model.start))
    dp.add_handler(play_handler)
    dp.add_handler(CommandHandler("info", model.info))
    dp.add_handler(CommandHandler("close", model.close))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
