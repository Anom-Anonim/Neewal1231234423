#import schedule
#import telebot
#from threading import Thread
#from time import sleep

#TOKEN = "5131376956:AAGu0AVOiUZjgOvciaFDqA9Vl_w0iOUbOZo"

#bot = telebot.TeleBot(TOKEN)
#some_id = 735662028 # This is our chat id.

#def schedule_checker():
    #while True:
        #schedule.run_pending()
        #sleep(1)

#def function_to_run():
    #return bot.send_message(some_id, "This is a message to send.")
    #print('message go')

#if __name__ == "__main__":
    # Create the job in schedule.
    #schedule.every().tuesday.at("00:38").do(function_to_run)


    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    #Thread(target=schedule_checker).start() 


import schedule
import telebot
import config
from threading import Thread
from time import sleep

bot = telebot.TeleBot(config.TOKEN)
some_id = 735662028 # This is our chat id.

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


def test():
    return bot.send_message(some_id, "Доброе утро, Neewal!")
    print('Сообщение отправилось!')

def good_morning():
    return bot.send_message(some_id, "Доброе утро, Neewal!")
    print('Сообщение отправилось!')

def go():
    return bot.send_message(some_id, "Пора одеваться, Neewal!")
    print('Сообщение отправилось!')

def one_lesson_start():
    return bot.send_message(some_id, "До первого урока осталось 1 минута!")
    print('Сообщение отправилось!')

def one_lesson_stop():
    return bot.send_message(some_id, "До окончания первого урока осталось 1 минута!")
    print('Сообщение отправилось!')

def two_lesson_start():
    return bot.send_message(some_id, "До второго урока осталось 1 минута!")
    print('Сообщение отправилось!')

def two_lesson_stop():
    return bot.send_message(some_id, "До окончания второго урока осталось 1 минута!")
    print('Сообщение отправилось!')

def three_lesson_start():
    return bot.send_message(some_id, "До третьего урока осталось 1 минута!")
    print('Сообщение отправилось!')

def three_lesson_stop():
    return bot.send_message(some_id, "До окончания третьего урока осталось 1 минута!")
    print('Сообщение отправилось!')

def four_lesson_start():
    return bot.send_message(some_id, "До четвёртого урока осталось 1 минута!")
    print('Сообщение отправилось!')

def four_lesson_stop():
    return bot.send_message(some_id, "До окончания четвёртого урока осталось 1 минута!")
    print('Сообщение отправилось!')

def five_lesson_start():
    return bot.send_message(some_id, "До пятого урока осталось 1 минута!")
    print('Сообщение отправилось!')

def five_lesson_stop():
    return bot.send_message(some_id, "До окончания пятого урока осталось 1 минута!")
    print('Сообщение отправилось!')

def six_lesson_start():
    return bot.send_message(some_id, "До шестого урока осталось 1 минута!")
    print('Сообщение отправилось!')

def six_lesson_stop():
    return bot.send_message(some_id, "До окончания шестого урока осталось 1 минута!")
    print('Сообщение отправилось!')

def seven_lesson_start():
    return bot.send_message(some_id, "До седьмого урока осталось 1 минута!")
    print('Сообщение отправилось!')

def seven_lesson_stop():
    return bot.send_message(message.chat.id, "До окончания седьмого урока осталось 1 минута!")
    print('Сообщение отправилось!')

@bot.message_handler (commands=['start'])
def welcome(message):
    sticker = open('sticker/sticker.webp', 'rb')
    bot.send_sticker(some_id, sticker)
    bot.send_message (message.from_user.id, 'Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданые как ежедневник для Neewal!'.format(message.from_user, bot.get_me()),
        parse_mode='html')

if __name__ == "__main__":
    schedule.every().monday.at("07:00").do(good_morning)
    schedule.every().tuesday.at("07:00").do(good_morning)
    schedule.every().wednesday.at("07:00").do(good_morning)
    schedule.every().thursday.at("07:00").do(good_morning)
    schedule.every().friday.at("07:00").do(good_morning)



    schedule.every().monday.at("08:10").do(go)
    schedule.every().tuesday.at("08:10").do(go)
    schedule.every().wednesday.at("08:10").do(go)
    schedule.every().thursday.at("08:10").do(go)
    schedule.every().friday.at("08:10").do(go)



    schedule.every().monday.at("08:59").do(one_lesson_start)
    schedule.every().tuesday.at("08:59").do(one_lesson_start)
    schedule.every().wednesday.at("08:59").do(one_lesson_start)
    schedule.every().thursday.at("08:59").do(one_lesson_start)
    schedule.every().friday.at("08:59").do(one_lesson_start)



    schedule.every().monday.at("09:44").do(one_lesson_stop)
    schedule.every().tuesday.at("09:44").do(one_lesson_stop)
    schedule.every().wednesday.at("09:44").do(one_lesson_stop)
    schedule.every().thursday.at("09:44").do(one_lesson_stop)
    schedule.every().friday.at("09:44").do(one_lesson_stop)
 


    schedule.every().monday.at("09:54").do(two_lesson_start)
    schedule.every().tuesday.at("09:54").do(two_lesson_start)
    schedule.every().wednesday.at("09:54").do(two_lesson_start)
    schedule.every().thursday.at("09:54").do(two_lesson_start)
    schedule.every().friday.at("09:54").do(two_lesson_start)
 


    schedule.every().monday.at("10:39").do(two_lesson_stop)
    schedule.every().tuesday.at("10:39").do(two_lesson_stop)
    schedule.every().wednesday.at("10:39").do(two_lesson_stop)
    schedule.every().thursday.at("10:39").do(two_lesson_stop)
    schedule.every().friday.at("10:39").do(two_lesson_stop)
 


    schedule.every().monday.at("10:59").do(three_lesson_start)
    schedule.every().tuesday.at("10:59").do(three_lesson_start)
    schedule.every().wednesday.at("10:59").do(three_lesson_start)
    schedule.every().thursday.at("10:59").do(three_lesson_start)
    schedule.every().friday.at("10:59").do(three_lesson_start)
 
 


    schedule.every().monday.at("11:44").do(three_lesson_stop)
    schedule.every().tuesday.at("11:44").do(three_lesson_stop)
    schedule.every().wednesday.at("11:44").do(three_lesson_stop)
    schedule.every().thursday.at("11:44").do(three_lesson_stop)
    schedule.every().friday.at("11:44").do(three_lesson_stop)
 


    schedule.every().monday.at("11:54").do(four_lesson_start)
    schedule.every().tuesday.at("11:54").do(four_lesson_start)
    schedule.every().wednesday.at("11:54").do(four_lesson_start)
    schedule.every().thursday.at("11:54").do(four_lesson_start)
    schedule.every().friday.at("11:54").do(four_lesson_start)



    schedule.every().monday.at("12:39").do(four_lesson_stop)
    schedule.every().tuesday.at("12:39").do(four_lesson_stop)
    schedule.every().wednesday.at("12:39").do(four_lesson_stop)
    schedule.every().thursday.at("12:39").do(four_lesson_stop)
    schedule.every().friday.at("12:39").do(four_lesson_stop)



    schedule.every().monday.at("12:59").do(five_lesson_start)
    schedule.every().tuesday.at("12:59").do(five_lesson_start)
    schedule.every().wednesday.at("12:59").do(five_lesson_start)
    schedule.every().thursday.at("12:59").do(five_lesson_start)
    schedule.every().friday.at("12:59").do(five_lesson_start)



    schedule.every().monday.at("13:44").do(five_lesson_stop)
    schedule.every().tuesday.at("13:44").do(five_lesson_stop)
    schedule.every().wednesday.at("13:44").do(five_lesson_stop)
    schedule.every().thursday.at("13:44").do(five_lesson_stop)
    schedule.every().friday.at("13:44").do(five_lesson_stop)



    schedule.every().monday.at("13:54").do(six_lesson_start)
    schedule.every().tuesday.at("13:54").do(six_lesson_start)
    schedule.every().wednesday.at("13:54").do(six_lesson_start)
    schedule.every().thursday.at("13:54").do(six_lesson_start)
    schedule.every().friday.at("13:54").do(six_lesson_start)



    schedule.every().monday.at("14:39").do(six_lesson_stop)
    schedule.every().tuesday.at("14:39").do(six_lesson_stop)
    schedule.every().wednesday.at("14:39").do(six_lesson_stop)
    schedule.every().thursday.at("14:39").do(six_lesson_stop)
    schedule.every().friday.at("14:39").do(six_lesson_stop)



    schedule.every().monday.at("14:59").do(seven_lesson_start)
    schedule.every().monday.at("15:44").do(seven_lesson_stop)



    schedule.every().tuesday.at("14:59").do(seven_lesson_start)
    schedule.every().tuesday.at("15:44").do(seven_lesson_stop)



    schedule.every().wednesday.at("14:59").do(seven_lesson_start)
    schedule.every().wednesday.at("15:44").do(seven_lesson_stop)

    Thread(target=schedule_checker).start()

bot.polling (none_stop=True)