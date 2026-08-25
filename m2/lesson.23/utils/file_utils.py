import os
from pathlib import Path


ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif"}
MAX_UPLOAD_SIZE = 10 * 1024 * 1024


def is_allowed_file(filename: Path) -> bool:
    """Проверяем, есть ли расширение в разрешенной коллекции."""
    ext = filename.suffix.lower()
    print(ext)
    return ext in ALLOWED_EXTENSIONS


def get_unique_name(filename: Path) -> str:
    pass




if __name__ == '__main__':
    print(is_allowed_file(Path("test.png")))
    print(is_allowed_file(Path("test.mp4")))