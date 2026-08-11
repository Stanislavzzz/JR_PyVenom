import sys
import time
from pathlib import Path
from typing import NamedTuple


DATA_DIR = Path("/app/data")
MESSAGES_FILE = DATA_DIR / "messages.txt"


def save_mesages(message):
    """Сохраняет сообщение и выводит содержимое файла."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with MESSAGES_FILE.open("a", encoding="utf-8") as file:
        file.write(f'{message}\n')
    print(f'Сообщение созранено: {message}')
    print(f'Путь к файла {MESSAGES_FILE} \n')

    print(f'Содержимое всего файла:')
    print(MESSAGES_FILE.read_text(encoding="utf-8"), end="")


def wait_for_command():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print('Контейнер запущен')
    running = True
    while running:
        time.sleep(3000)


if __name__ == '__main__':
    message = " ".join(sys.argv[1:]).strip()

    if message:
        save_mesages(message)
    else:
        wait_for_command()