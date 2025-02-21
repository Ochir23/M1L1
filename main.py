import telebot
    
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("tOkEn")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

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

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)




# Запуск бота
bot.polling()
