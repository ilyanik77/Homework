from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

reply_keyboard = [['/play', '/info', '/close']]
stop_keyboard = [['/stop']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = False)
stop_markup = ReplyKeyboardMarkup(stop_keyboard, one_time_keyboard = False)
