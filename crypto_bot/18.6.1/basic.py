
import telebot
from conf import keys, TOKEN
from extensions import CnvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'чтобы начать работу введите команду боту в следующем формате:\n<имя валюты>\n' \
           '<в какую валюту перевести>\n' \
           '<количество переводимой валюты>\nувидеть список доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise CnvertionException('слишком много параметров')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except CnvertionException as e:
        bot.reply_to(message, f'ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'не удалось обработать команду\n{e}')
    else:
        result = float(total_base) * float(amount)
        text = f'цена: за {amount} {quote} в {base} будет {total_base} * {amount} =  {result} '
        bot.send_message(message.chat.id, text)


bot.polling()