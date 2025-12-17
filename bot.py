from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)
import random
from config import BOT_TOKEN, GROUP_ID
from messages import compliments, mood_messages
import scheduler



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == GROUP_ID:
        await update.message.reply_text("From Gargi 💕 is active.")

async def compliment(update: Update, context):
    if update.effective_chat.id == GROUP_ID:
        msg = random.choice(compliments)
        await context.bot.send_message(GROUP_ID, msg)

async def mood(update: Update, context):
    if update.effective_chat.id != GROUP_ID:
        return

    if not context.args:
        await update.message.reply_text("Use: /mood happy|sad|stressed|love")
        return

    mood = context.args[0].lower()
    if mood in mood_messages:
        msg = random.choice(mood_messages[mood])
        await context.bot.send_message(GROUP_ID, msg)
    else:
        await update.message.reply_text("Mood not found 💭")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("compliment", compliment))
    app.add_handler(CommandHandler("mood", mood))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
