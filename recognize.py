import speech_recognition as sr

#Функция распознования речи
def recognize_speech():
    # Создаем объект Recognizer
    recognizer = sr.Recognizer()

    # Используем микрофон для записи аудио
    with sr.Microphone() as source:
        print("Скажите что-нибудь:")
        audio = recognizer.listen(source)

    try:
        # Распознаем речь с помощью Google Web Speech API
        text = recognizer.recognize_google(audio, language='ru-RU', show_all=True)
        print("Вы сказали:", text)
        return text
    except sr.UnknownValueError:
        print("Извините, не удалось распознать речь")
        return ""
    except sr.RequestError as e:
        print("Ошибка сервиса распознавания речи; {0}".format(e))
        return ""

