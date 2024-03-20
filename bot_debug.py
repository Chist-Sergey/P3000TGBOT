from telegram.ext import ContextTypes
from telegram import Update
from bot_functions import birthday_yell
from datetime import datetime
from options import job_time_zone

# a function similar to 'birthday_loop'
async def birthday_force(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.job_queue.run_once(
        callback=birthday_yell,
        when=datetime.now(tz=job_time_zone()).second+5,
        chat_id=update.effective_chat.id,
        name='Instant Check',
    )
