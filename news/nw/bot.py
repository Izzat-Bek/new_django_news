from telegram import Bot
from telegram.constants import ParseMode
import logging


async def send_news(news):
    bot = Bot(token='6634816062:AAGjshTkVrQ7tMtMNfqCBg-SprNKjh6SGfA')
    channel_id = '@izzat_ansajfsnafis'
    url = f'http://127.0.0.1:8000/article/{news.id}'
    
    url_ad = url.replace('_', r'\_').replace('*', r'\*').replace('[', r'\[').replace(']', r'\]')

    message = f'{news.title} podrobno [URL]({url_ad})'
    try:
        await bot.send_message(chat_id=channel_id, text=message, parse_mode=ParseMode.MARKDOWN_V2)
    except Exception as e:
        logging.error(e)
