from aiogram import Bot, Dispatcher, executor, types
# import logging
# import time
# import os
import openai

openai.api_key = ""
openai.Model.list()


TOKEN = ''

HELP_COMMANDS = """
/help - виклик споміжних команд.

/start - включити чат.

/QA - Дає відповіді на запитання, спираючись на наявні знання (можна використовувати як основного).

/Grammar_correction - Виправляє речення стандартною англійською мовою.

/Summarize_for_a_2nd_grader - Перекладає складний текст на простіші поняття.

/Natural_language_to_OpenAI_API - Створює код для виклику OpenAI API, використовуючи інструкцію природною мовою.
/Text_to_command - Перекладіть текст у програмні команди.

/English_to_other_languages - Перекладає англійський текст на французьку, іспанську та японську мови.

"""

bot = Bot(TOKEN)
dp = Dispatcher(bot)

# start func
@dp.message_handler(commands=['start'])
async def start_commnd(message: types.Message):
    await message.answer(text=f'Привіт {message.from_user.first_name}, вітаю тебе в інтегрованому ChatGPT в телеграм, можеш задати своє запитання, перед тим як задати запитання краще подивись які є види чату, щоб це подивитись напиши команду /help')


#help func
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=f'{HELP_COMMANDS}')

#gpt func
@dp.message_handler(commands='Q&A')
async def answer(message: types.Message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        preence_penalty=0

    )
    await message.reply(response['choices'][0]['text'])


@dp.message_handler(commands='Grammar_correction')
async def answer(message: types.Message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0

    )
    await message.reply(response['choices'][0]['text'])

@dp.message_handler(commands='Summarize_for_a_2nd_grader')
async def answer(message: types.Message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0.7,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0

    )
    await message.reply(response['choices'][0]['text'])

@dp.message_handler(commands='Natural_language_to_OpenAI_API')
async def answer(message: types.Message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0

    )
    await message.reply(response['choices'][0]['text'])

@dp.message_handler(commands='English_to_other_languages')
async def answer(message: types.Message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0

    )
    await message.reply(response['choices'][0]['text'])

@dp.message_handler(commands='Natural_language_to_Stripe_API')
async def answer(message: types.Message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0

    )
    await message.reply(response['choices'][0]['text'])


#print(openai.Model.list())   


if __name__ == '__main__':
    executor.start_polling(dp)
