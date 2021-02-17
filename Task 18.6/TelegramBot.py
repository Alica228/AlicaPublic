import telebot
from extensions import *


file = open("config", "r"); TOKEN = file.read(); file.close()
bot = telebot.TeleBot(TOKEN)



# Тут обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    welcome = '''
Привет, вы попали к боту по переводу одной валюты в другую!
Я работаю так, вы мне пишите две валюты и количество, а я перевожу это количество из одной валюты в другую
Например, "Рубли Евро 50", я отвечу сколько Евро в 50 рублях

Команды:
/values - получить список всех известных мне валют
/start - вывести это сообщение
/help - вывести это сообщение
'''
    bot.send_message(message.chat.id, welcome)

# Тут обрабатываются все сообщения, содержащие команду '/values'.
@bot.message_handler(commands=['values'])
def get_currencies(message):
    bot.send_message(message.chat.id, ', '.join(allRates.AllCurrenciesRates.keys()))

# Тут обрабатываются все сообщения, которые не подошли под условия выше.
@bot.message_handler(content_types=['text'])
def send_rates(message):
    try:
        if message.text[0] == '/' and message.text[1] != ' ': raise APIException("Не знаю такой команды")
        text = [i.upper() for i in message.text.split(' ') if i != '']
        if len(text) != 3: raise APIException("Нужно три элемента в сообщении!")
        bot.send_message(message.chat.id, allRates.get_price(*text))
    except APIException as e:
        bot.send_message(message.chat.id, e)


allRates = Rates()
print("Bot has started")
bot.polling()