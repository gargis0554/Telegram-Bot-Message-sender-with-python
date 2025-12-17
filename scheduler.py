from apscheduler.schedulers.background import BackgroundScheduler
from telegram import Bot
import random
from config import BOT_TOKEN, GROUP_ID
from messages import compliments

bot = Bot(token=BOT_TOKEN)

def daily_message():
    msg = random.choice(compliments)
    bot.send_message(chat_id=GROUP_ID, text=msg)

scheduler = BackgroundScheduler()
scheduler.add_job(daily_message, 'cron', hour=23, min=0)  # 9 AM
scheduler.start()
