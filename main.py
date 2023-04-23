from aiogram import Bot, Dispatcher, executor, types
# import logging
# import time
# import os
import openai

openai.api_key = "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"
openai.Model.list()


TOKEN = '6040057808:AAFpAXnGhGEbhKyNYnkucZfS7wDQOXIOnIc'

HELP_COMMANDS = """
/help - виклик споміжних команд.

/start - включити чат.

/QA - Дає відповіді на запитання, спираючись на наявні знання (можна використовувати як основного).

/Grammar_correction - Виправляє речення стандартною англійською мовою.

/Summarize_for_a_2nd_grader - Перекладає складний текст на простіші поняття.

/Natural_language_to_OpenAI_API - Створює код для виклику OpenAI API, використовуючи інструкцію природною мовою.
/Text_to_command - Перекладіть текст у програмні команди.

/English_to_other_languages - Перекладає англійський текст на французьку, іспанську та японську мови.

/Natural_language_to_Stripe_API - Створює код для виклику API Stripe за допомогою природної мови.

/SQL_translate - Перекладає природну мову на запити SQL.

/Parse_unstructured_data - Створює таблиці з довгого тексту, вказавши структуру та надавши кілька прикладів.

/Classification - Класифікує елементи за категоріями на прикладі.

/Python_to_natural_language - Пояснює частину коду Python мовою, зрозумілою людині.

/Movie_to_Emoji - конвертує назви фільмів у емодзі.

/Calculate_Time_Complexity - Шукає часову складність функції.

/Translate_programming_languages - Для перекладу з однієї мови програмування на іншу ми можемо використовувати коментарі, щоб вказати вихідну та цільову мови.

/Advanced_tweet_classifier - Це розширена підказка для виявлення настрою. Це дозволяє надати йому список оновлень статусу, а потім задати настрої для кожного з них.

/Explain_code - Пояснює складний фрагмент коду.

/Keywords - Витягує ключові слова з блоку тексту. При нижчій температурі він вибирає ключові слова з тексту. При вищій температурі він генеруватиме пов’язані ключові слова, які можуть бути корисними для створення пошукових індексів.

/Factual_answering - Скеровує модель до фактичних відповідей, показуючи їй, як відповідати на запитання, які виходять за межі її бази знань.
 Використання «?» вказати відповідь на слова та фрази, яких він не знає, забезпечує природну відповідь, яка, здається, працює краще, ніж більш абстрактні відповіді.

/Ad_from_product_description - Перетворює опис продукту на текст оголошення.

/Product_name_generator - Складає назви продуктів із прикладів слів. Під впливом підказки спільноти.

/TLDR summarization - Підсумує текст, додавши 'tl;dr:' у кінець фрагмента тексту. Це показує, що API розуміє, як виконувати низку завдань без інструкцій.

/Python_bug_fixer - Існує кілька способів структурування підказки для перевірки на помилки. Тут ми додаємо коментар про те, що вихідний код має помилки, а потім просимо Codex створити виправлений код.

/Spreadsheet_creator - Створює електронні таблиці з різними видами даних. Це довга підказка, але дуже універсальна. Вихідні дані можна скопіювати та вставити в текстовий файл і зберегти як .csv із вертикальними роздільниками.

/JavaScript_helper_chatbot - Це чат-бот у стилі повідомлень, який може відповісти на запитання про використання JavaScript. Він використовує кілька прикладів, щоб почати розмову.

/MLAI_language_model_tutor - Це чат-бот у стилі QA, який відповідає на запитання про мовні моделі.

/Science_fiction_book_list_maker - Це створює список науково-фантастичних книг і зупиняється, коли він досягає №10.

/Tweet_classifier - Це базова підказка для виявлення настрою.

/Airport_code_extractor - Проста підказка для отримання кодів аеропортів із тексту.

/SQL_request - Створюйте прості запити SQL.

/Extract_contact_information - Вилучення контактної інформації з блоку тексту.

/JavaScript_to_Python - Перетворіть прості вирази JavaScript на Python.

/Friend_chat - Емуляція розмови текстового повідомлення.

/Mood_to_color - Перетворення текстового опису на колір.

/Write_a_Python_docstring - Приклад того, як створити рядок документації для заданої функції Python. Ми вказуємо версію Python, вставляємо код, а потім запитуємо в коментарі рядок документації та надаємо характерний початок рядка документації ("")

/Analogy_maker - Створіть аналогії. Змінено з підказки спільноти, щоб вимагати менше прикладів.

/JavaScript_one_line_function - Перетворіть функцію JavaScript на один рядок.

/Micro_horror_story_creator - Створює короткі історії жахів із двома-трьома реченнями на основі введеної теми.

/Third-person_converter - Перетворює POV від першої особи на зображення від третьої особи. Це змінено з підказки спільноти, щоб використовувати менше прикладів.

/Notes_to_summary - Перетворіть нотатки зустрічі на резюме.

/new-worked - ....

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