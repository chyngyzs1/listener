import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import datetime
from subprocess import call

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
    print("Бот: " + words)

talk("Привет, спроси у меня что-либо")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Бот: Говорите...")
        r.pause_threshold  = 1
        r.adjust_for_ambient_noise(source, duration=1)
        # audio = r.listen(source)
        audio = r.record(source, duration=5)
    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        zadanie = command()
    return zadanie

# Открывает приложении
def openapp(zadanie):
    if 'стоп' in zadanie or "пока" in zadanie or "до свидание" in zadanie:
        talk("Да, конечно, без проблем. пока")
        sys.exit()
    if 'калькулятор' in zadanie:
        talk("Открываю калькулятор")
        call(["calc.exe"])
    elif 'саблайм текст' in zadanie:
        talk('Открываю Саблайм текст')
        call(["C:\Program Files (x86)\Sublime Text 3\sublime_text.exe"])
    # Можно и дальше добавлять

# Поиск в гугле
def searching(zadanie):
    url = 'https://www.google.com/search?sxsrf=ALeKk01Oc2MUWl9hzhzt-R2Q8QEfMqDoCg%3A1608197902815&source=hp&ei=DifbX5XbLpCelwTck5CQAg&q='
    webbrowser.open(url + zadanie)


# Основное условии(if)
def makeSmt(zadanie):
    if 'стоп' in zadanie or "пока" in zadanie or "до свидание" in zadanie:
        talk("Да, конечно, без проблем. пока")
        sys.exit()
    elif 'как тебя зовут' in zadanie or 'назови себя' in zadanie:
        talk('Меня зовут Бот красавчик')
    elif 'скажи дату' in zadanie:
        day = datetime.datetime.now()
        talk("Сегодня " + str(day.day) + "." + str(day.month) + "." + str(day.year))
    elif 'скажи время' in zadanie:
        now = datetime.datetime.now()
        talk("Сейчас " + str(now.hour) + ":" + str(now.minute))
    elif 'открой chrome' in zadanie:
        talk("Открываю хром")
        call(["C:\Program Files\Google\Chrome\Application\chrome.exe"])
    elif 'поищи в гугле' in zadanie:
        talk('Что хотели поискать')
        searching(command())
    elif 'открой приложение' in zadanie:
        talk("Кокое именно приложение вы хотели открыть")
        print('1-Калькулятор\n2-Саблайм текст')
        openapp(command())

while True:
    makeSmt(command())

talk("Привет, спроси у меня что-либо")