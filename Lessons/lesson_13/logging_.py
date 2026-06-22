

import logging
import sys

# Налаштування конфігурації логування
logging.basicConfig(filename='example.log', level=logging.INFO, format='%(name)s - %(asctime)s: [%(levelname)s] - %(message)s')

# Логування подій різного рівня (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.debug('our massage DEBUG')
logging.info('our massage INFO')
logging.warning('our massage WARNING')
logging.error('our massage ERROR')
logging.critical('our massage CRITICAL')



def fun_div(a, b):
    try:
        result =  a / b
        logging.info(f'Our result is: {result}')
        return result
    except ZeroDivisionError as err:
        logging.critical(err)


fun_div(1, 2)
fun_div(1, 0)



# Налаштування конфігурації логування
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Додавання обробника для виводу в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
sys.stdout('console_handler')
logging.getLogger('').addHandler(console_handler)

# Логування подій різного рівня
logging.debug('Це повідомлення рівня DEBUG')
logging.info('Це повідомлення рівня INFO')
logging.warning('Це повідомлення рівня WARNING')
logging.error('Це повідомлення рівня ERROR')
logging.critical('Це повідомлення рівня CRITICAL')