from pybot_eto import eto_command
from pybot_func import nagasa_command, seireki_command
from pybot_random import choice_command, dice_command
from pybot_datetime import today_command, now_command, weekday_command
from pybot_weather import weather_command
from pybot_wikipedia import wikipedia_command

with open('../../Chapter6/pybot.txt', encoding = 'utf-8') as command_file:
    raw_data = command_file.read()
lines = raw_data.splitlines()

bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

# while True:
def pybot(command):
    # command = input('pybot> ')
    response = ''
    for message in bot_dict:
        if message in command:
            response = bot_dict[message]
            break
    try:
        if '西暦' in command:
            response = seireki_command(command)
        if '長さ' in command:
            response = nagasa_command(command)
        if '干支' in command:
            response = eto_command(command)
        if '選ぶ' in command:
            response = choice_command(command)
        if 'さいころ' in command:
            response = dice_command(command)
        if '今日' in command:
            response = today_command(command)
        if '現在' in command:
            response = now_command(command)
        if '曜日' in command:
            response = weekday_command(command)
        if '天気' in command:
            response = weather_command()
        if '事典' in command:
            response = wikipedia_command(command)

        if not response:
            response = '何デショウ？'

        return response

        # print(response)
        # if 'さようなら' in command:
        #     break
        # if 'bye' in command:
        #     break
    except Exception as e:
        print('！予期せぬエラーが発生しました！')
        print('* 種類', type(e))
        print('* 内容', e)
