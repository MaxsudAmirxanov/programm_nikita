from pyrogram import Client
from pyrogram.types import User
import random
import asyncio
import datetime
from time import sleep

#Наш копирайт
# text = {1: "тест1", 2: "test2", 3: "test3"}
text = """привет, меня зовут Никита, я уже несколько лет "живу" на фрилансе. 😅

Занимаюсь веб-дизайном и сейчас помогаю начинающим веб-дизайнерам выйти на стабильный доход от 50 000₽/месяц, действующим — плотно закрепиться на рынке и пробить планку в 200к за счёт получения знаний и практики в трендовом дизайне, выстраивании твёрдого позиционирования и прокачки навыка продаж. 

Своего первого клиента я закрыл на сайт за 130 тысяч рублей, а сейчас работаю с топами рынка инфобиза (Митрошина, Сташкевич, Тимочко, Хелли Фокси) и хочу предложить тебе небольшую БЕСПЛАТНУЮ консультацию 🔥

От тебя необходимо будет только твоё внимание и доверие, я погружусь в твою текущую ситуацию и дам пару советов, как сейчас выйти на новый уровень дохода. 

Было бы интересно созвониться на 20-30 минуток? """

#14460056
api_id=12566967
api_hash="8151e12ef5201646c9932a206b7dc614"


app = Client("me", api_id, api_hash )

async def main(v, choice_2, file_name, second):
    'Рассылка, по базе'
    async with app:

        number_r = random.randint(1,4)
        new_v = v.split('\n')

        index = 0
        for i in new_v:
            if i == '':
                continue
            print(i)
            index += 1
            if index == 1:
                if choice_2 == '3':
                    'Рассылка тестом'
                    first_name = (await app.get_users(i)).first_name
                    sleep(second)
                    await app.send_message(i, f"{first_name} {text}")
                    break

                elif choice_2 == '2':
                    'Рассылка с кружочками'
                    sleep(second)
                    # await app.send_message(i, f"Приветствую " + (await app.get_users(i)).first_name)
                    await app.send_video_note(i, f"data\{file_name}.mp4")
                    break

                elif choice_2 == '1':
                    'Рассылка с гс'
                    sleep(second)
                    await app.send_audio(i, f"data\{file_name}.ogg")
                    break


async def compiler_chat(chat, file_name):
    "Компилятор чатов"
    await app.start()
    async for user in app.iter_chat_members((await app.get_chat(chat)).id):
        
        timestamp = user.user.last_online_date

        try:
            value = datetime.datetime.fromtimestamp(timestamp)
        except TypeError:
            with open(f'data_for_user/{file_name}.txt', 'a', encoding='utf-8') as file:
                file.write(f"{user.user.username}\n")
                continue



        with open(f'data_for_user/{file_name}.txt', 'a', encoding='utf-8') as file:
            if value.strftime('%Y-%m-%d') == f'2022-03-22' or value.strftime('%Y-%m-%d') == f'2022-03-23' or value.strftime('%Y-%m-%d') == f'2022-03-24' or value.strftime('%Y-%m-%d') == f'2022-03-25' or value.strftime('%Y-%m-%d') == f'2022-03-26':
                file.write(f"{user.user.username}\n")

            else:
                print(f"Последний раз, когда пользовател заходил - {value.strftime('%Y-%m-%d %H:%M:%S')} - {user.user.username}")
            


def spam(data_base):
    number = 0
    choice_1 = int(input("Скольким пользователям хотите отправить сообщение? "))
    choice_2 = input('''
        1) Рассылка с гс
        2) Рассылка с кружочками
        3) Рассылка тестом
        ''')
    second = int(input('Введите задержку в секундах: '))
    if choice_2 == '2':
        file_name = 'Никита_кружочек'

    elif choice_2 == '1':
        file_name = 'Никита_гс'
    elif choice_2 == '3':
        file_name = 'Пусто'

    for v in open(f"data_for_user/{data_base}.txt", "r"):
        number += 1

        app.run(main(v, choice_2, file_name, second))
        if choice_1 == number:
            
    
            #Удаление строк ID, которым сообщение отправилось
            with open(f"data_for_user/{data_base}.txt", 'r') as f:
                lines = f.readlines()

            with open(f"data_for_user/{data_base}.txt", 'w') as f:
                f.writelines(lines[choice_1:])
            break



print('''
1) Запустить рассылку по базе 
2) Скомпилировать пользователей чата
''')
choice = input("Что хотите сделать? ")

if choice == '1':
    data_base = input('Ведите название файла (.txt указываеь не надо): \n')
    

    spam(data_base)

elif choice == '2':
    chat = input('Введите @ чата, который хотите скомпилировать: \n')
    file_name = input('Ведите название нового чата: \n')
    asyncio.run(compiler_chat(chat, file_name))