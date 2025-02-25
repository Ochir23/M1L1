import telebot
    
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("token")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!Вот доступные команды:/you /do /color /mood /health')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)


@bot.message_handler(commands=['rickroll'])
def send_rickrol(message):
    bot.reply_to(message, 'https://youtu.be/Cxmvq1MCR3c?si=Ekv_xd7X6YW_6ulJ')

bot.message_handler(commands=['you'])
def send_you(message):
    bot.reply_to(message, f'Отлично')

bot.message_handler(commands=['do'])
def send_do(message):
    bot.reply_to(message, f'Ищу ошибку в твоем коде.')

bot.message_handler(commands=['color'])
def send_color(message):
    bot.reply_to(message, f'#800080.')

bot.message_handler(commands=['health'])
def send_health(message):
    bot.reply_to(message, f'Если не будешь качать торренты, то не буду болеть.')

bot.message_handler(commands=['mood'])
def send_mood(message):
    bot.reply_to(message, f'Пока хорошее.')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)




# Запуск бота
bot.polling()
