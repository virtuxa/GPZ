import logging
import logging.handlers

import app

# Задаём формат логов
FORMAT = '%(asctime)s :: %(levelname)s :: %(name)s:%(lineno)s :: %(message)s'

# Вывод в консоль
def get_stream_handler():
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)
    return sh

# Вывод в файл с логами
def get_file_handler():
    fh = logging.handlers.RotatingFileHandler(filename="logs.log", mode="w")
    fh.setFormatter(logging.Formatter(FORMAT))
    fh.setLevel(logging.INFO)
    return fh

# Инициализация логгера, добавление handler'ов
def init_logger(name):

    # Задаём имя логгеру и назначаем уровень
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Добавляем handler'ы
    logger.addHandler(get_stream_handler())
    logger.addHandler(get_file_handler())

    logger.debug("logger was initialized")

# Запускаем инициализацию логгера, а также создаём логгер module.secure
init_logger("module")
logger = logging.getLogger("module.logger")

def main():
    app.main()

if __name__ == '__main__':
    logger.info("Starting logging module...")
    main()
    logger.info("Stopping logging module...")



# Использование dict?