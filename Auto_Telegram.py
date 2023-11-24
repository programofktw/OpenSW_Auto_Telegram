import schedule
import time
import pytz
import datetime
import telegram
import asyncio

token = "6833983891:AAGQNZuPAmYgRU4beRzTq-mE2hoMKvG13io"
public_chat_name = '@OpenSw_2_chatbot'
bot = telegram.Bot(token = token)
def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return
    asyncio.get_event_loop().run_until_complete(send(str(now)))


async def send(time):
    await bot.sendMessage(chat_id=public_chat_name, text='현재 서울의 시각은 = '+time)
    print(f"Sent message: ", time)
    print("send complete")



schedule.every(30).seconds.do(job)

while True : 
	schedule.run_pending()
	time.sleep(1)

