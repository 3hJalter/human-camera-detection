import telepot

class Response:
    def telegram_send(self, time):
        token = '5709908204:AAGBLbVoa8FZpWSyPu1arZGL42BG6TRngGY' # telegram token
        receiver_id = 5689048641 # https://api.telegram.org/bot<TOKEN>/getUpdates


        bot = telepot.Bot(token)

        bot.sendMessage(receiver_id, 'Detect new person at time: ' + time) 



