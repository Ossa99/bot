import requests
import json
from telebot import TeleBot


def mix(bot: TeleBot, api: str) -> None:
    """

    @rtype: object
    """
    @bot.message_handler(content_types=['text'])
    def get_wether(message):
        city = message.text.strip().lower()
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
        data = json.loads(res.text)
        print(data)
        if data['cod'] == '404':
            bot.reply_to(message, 'Город не найден!')
        else:
            bot.reply_to(message, f'Температура сейчас: {data["main"]["temp"]}')
