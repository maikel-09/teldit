import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler,MessageHandler, filters
from redvid import Downloader
import re

logging.basicConfig(
    format='[%(levelname)s]  %(asctime)s - %(name)s -  %(message)s',
    level=logging.INFO
)

TELEGRAMTOKEN=os.getenv('TELEGRAMTOKEN',None)


async def redvid_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f'Received messsage: "{update.message.text}"')
    # extract url
    try:
        url = re.search("(?P<url>https?://[^\s]+)", update.message.text).group("url")
    except Exception as ex:
        logging.error(f'{ex}')
        url = None
    if not url:
        logging.warning(f'No valid url found: {url}')
        await update.message.reply_text(f'Not a valid reddit url: "{update.message.text}"',reply_to_message_id=update.message.message_id)
        return False
    reddit = Downloader(url=url,path='/media',max_q=True,log=False)
    reddit.download()
    logging.info('File downloaded')
    await update.message.reply_text('Finished downloading',reply_to_message_id=update.message.message_id)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAMTOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, redvid_download))
    application.run_polling()
