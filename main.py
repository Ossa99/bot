import telebot
import coma
import contet



def main():
    bot = telebot.TeleBot(token='')
    API: str = ''

    coma.min(bot=bot)
    contet.mix(bot=bot, api=API)


    print('start')
    bot.polling(none_stop=True)



if __name__ == '__main__':
    main()
