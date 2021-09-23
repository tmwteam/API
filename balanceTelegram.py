import telebot
import requests

bot = telebot.TeleBot('Токен для бота в телеграмм')
APIKey = 'Ключ API который выдали вам сотрудники '
login = 'Логин от аккаунта'
password = 'Пароль от аккаунта'


def get_token(login, password):
    url_token = 'https://api.timeweb.ru/v1.2/access'
    headers = {'accept': 'application/json',
               'x-app-key': APIKey}
    response = requests.post(url_token, headers=headers, auth=(login, password))
    json = response.json()
    token = json['token']
    return token

token = get_token(login, password)

def get_balance(token):
    headers = {'accept': 'application/json',
               'x-app-key': APIKey,
                'Authorization': 'Bearer ' + token}
    response = requests.get('https://api.timeweb.ru/v1.1/finances/accounts/'+login, headers=headers)
    json = response.json()
    balance = json['balance']
    return balance


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Напиши баланс и узнаешь баланс на своем аккаунте\n")
    print(message.chat.id)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'баланс':
        bot.send_message(IDChat, get_balance(token)+" рублей на балансе") #Вместо IDChat можно указать свой телеграм, что бы только Вы видели всю информацию, его можно увидеть в консоле, строчка 34 выводит после того как боту напишите /start


bot.polling()
