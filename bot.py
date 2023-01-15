import telegram
import time
import requests
import json
import telebot

bot = telebot.TeleBot('5722297233:AAGoeU3ubJWKPHm5gf3bRPwtKmaMcJrG-4E')
print("Connected")

@bot.message_handler(commands=['startsang'])
def send_welcome(message):
    target = 0.0094
    bot.reply_to(message, "I am running. \nDon't type anything. \nTarget: " + str(target))
    i=0
    while(True):
        currentPrice = Price()
        i=i+1
        res= str(i) + " - " + str(currentPrice)
        bot.send_message(-635032010, res)
        print(res)
        if Price() > target:
            bot.send_message(-890814471, Price())
            # bot.reply_to(message, Price())
        time.sleep(5)

def Price():
    response = requests.get("https://api.pancakeswap.info/api/v2/tokens/0x8bdd8dbcbdf0c066ca5f3286d33673aa7a553c10")

    dataPanCake = json.loads(response.text)
    data = dataPanCake['data']
    strPrice = data['price']
    price = float(strPrice)
    time.sleep(3)
    return price
    
bot.infinity_polling()


