import time


def retry(max_retries, time_sleep):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    # Спроба виклику функції, яку декоруємо

                    asd = func(*args, **kwargs)
                    print('я закінчив виконувати фунцію')
                    return asd
                except Exception as e:
                    # Обробка помилки та вивід повідомлення про спробу
                    print(f"Помилка: {e}. Повторна спроба {retries + 1}/{max_retries}")
                    time.sleep(time_sleep)
                    retries += 1
            # Викидаємо виняток, якщо досягнуто максимальну кількість спроб
            raise Exception("Досягнуто максимальну кількість спроб")
        return wrapper
    return decorator

# Параметризоване застосування декоратора
@retry(max_retries=15, time_sleep=1)
def connect_to_server():
    print('Відсилаю запит на сервер')
    # Спроба з'єднатися з сервером
    raise ConnectionError("Не вдалося підключитися до сервера")

@retry(max_retries=3, time_sleep=5)
def connect_to_server_2():
    print('Відсилаю запит на сервер')
    # Спроба з'єднатися з сервером

# Виклик функції
connect_to_server_2()

connect_to_server()

# @retry(max_retries=3, time_sleep=5)
# get():
#  request_get