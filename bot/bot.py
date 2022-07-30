import logging

from aiogram import Bot, Dispatcher, executor, types
import environ
import os
import psycopg2


env = environ.Env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

TOKEN = os.environ.get('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    user_id = message['from']['id']
    username = message['from']['username']

    conn = psycopg2.connect(dbname=os.environ.get('DB_NAME'),
                            user=os.environ.get('DB_USER'),
                            password=os.environ.get('DB_PASSWORD'),
                            # host='localhost', # for local
                            # port=os.environ.get('5444'), # for local
                            host='db',  # for docker
                            port='5432'  # for docker
                            )
    cursor = conn.cursor()

    try:
        cursor.execute(f"""INSERT INTO app_subscriber (user_id, username) VALUES (%s, %s);""",
                       (user_id, username))
        conn.commit()
        await message.reply('You subscribed')
    except psycopg2.errors.IntegrityError:
        await message.reply('You are already is subscriber')
    cursor.close()
    conn.close()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
