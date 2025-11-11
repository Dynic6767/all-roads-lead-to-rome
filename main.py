
import telebot


bot = telebot.TeleBot("8497488826:AAEMr6T9OLsgdSRTkMCNvecxuxaooA2tg8M")

user_states = {}

@bot.message_handler(commands=['start','help'] )
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Telegram бот. Я отвечаю на много вопросов. Вот мои командды: /hello , /bye.")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    user_states[message.chat.id] = 'waiting_for_feedback'  

@bot.message_handler(func=lambda message: message.chat.id in user_states and user_states[message.chat.id] == 'waiting_for_feedback')
def handle_response(message):
    if message.text.lower() == "хорошо":
        bot.reply_to(message, "Очень хорошо слышать")
        user_states.pop(message.chat.id)
    elif message.text.lower() == "плохо":
        bot.reply_to(message, "Извинте, это очень грустно слышать")
        user_states.pop(message.chat.id)

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()