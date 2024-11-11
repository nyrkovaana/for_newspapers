from datetime import datetime


def parse_date(date_str):
    formats = [
        "%A, %B %d, %Y",        # The Moscow Times: "Wednesday, October 2, 2002"
        "%A, %d.%m.%y",         # The Guardian: "Friday, 11.10.13"
        "%A, %d %B %Y"          # Daily News: "Thursday, 18 August 1977"
    ]

    for date_format in formats:
        try:
        #Попытка преобразовать строку в объект datetime по каждому из форматов
            return datetime.strptime(date_str, date_format)
        except ValueError:
        # Если формат не подошёл, продолжаем с следующим форматом
            pass

    # Если ни один формат не подошёл, выбрасываем исключение
    raise ValueError(f"Неизвестный формат даты: {date_str}")




while True:
    # Ввод строки с датой
    date_input = input("Введите дату (или \"exit\" для выхода): ")

    if date_input == "exit":
        break

    try:
        # Пытаемся преобразовать введённую строку в дату
        result = parse_date(date_input)
        # Если преобразование прошло успешно, выводим результат
        print(f"Преобразованная дата: {result}")
    except ValueError as e:
        # Если произошла ошибка, выводим сообщение об ошибке
        print(e)