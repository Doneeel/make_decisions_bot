from config import bot
import random

@bot.message_handler(commands=['start'])
def start(message):
    bot.delete_message(message.chat.id, message.id)

    msg_txt = """🎲 <b>Добро пожаловать в бот для принятия решений!</b>

📝 Если вас давно что-то гложет и вы никак не можете определиться: да или нет, этот бот способен вам помочь.

🤓 Подробнее о боте по команде /help

⚠️ <i>Внимание! Не доверяйте боту слишком важные решения, он для такого еще маленький.</i>
    """

    bot.send_message(message.chat.id, msg_txt, parse_mode="HTML")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.delete_message(message.chat.id, message.id)

    msg_txt = """🎲 <b>Этот бот способен помочь принять решение</b>

📝 Просто отправьте боту любой вопрос, на который можно ответить "да" или "нет". Он подумает и подскажет как действовать.

⚠️ <i>Внимание! Не доверяйте боту слишком важные решения, он для такого еще маленький.</i>
    """

    bot.send_message(message.chat.id, msg_txt, parse_mode="HTML")


@bot.message_handler(content_types=["text"])
def generate_answer(message):
    answer_options = ["да", "нет"]

    answer = random.choice(answer_options)
    answer_text = f"И... Я думаю... ответ... {answer}!"

    bot.reply_to(message, answer_text)
