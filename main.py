import telebot
import random 
import os


# Инициализация бота с использованием его токена
bot = telebot.TeleBot("token")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я просто бот! Вот доступные команды:/mem, /rickrol, /animals, /how are you, /heh')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)


@bot.message_handler(commands=['rickroll'])
def send_welcome(message):
    bot.reply_to(message, 'https://youtu.be/Cxmvq1MCR3c?si=Ekv_xd7X6YW_6ulJ')

bot.message_handler(commands=['how are you?'])
def send_welcome(message):
    bot.reply_to(message, 'i am fine,thanks.')

@bot.message_handler(commands=['mem'])
def send_mem(message):
    file_list = os.listdir("images")
    img_name = random.choice(file_list)
    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['animals'])
def send_animals(message):
    file_list = os.listdir("animals")
    img_name = random.choice(file_list)
    with open(f'animals/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)


 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)




# Запуск бота
bot.polling()
