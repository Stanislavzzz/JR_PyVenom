import sys

from fastapi import FastAPI, Request, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from pathlib import Path
import logging
from datetime import datetime

from utils.file_utils import is_allowed_file, MAX_UPLOAD_SIZE, get_unique_name


logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)
log_file = logs_dir / "app.log"

logging.basicConfig(
    level=logging.INFO,
    # format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    format="[{asctime}]- {name} - {levelname} - {message}",
    style="{",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Главная страница сервиса."""

    return templates.TemplateResponse(request=request, name="index.html", context={})


@app.get("/images/", response_class=HTMLResponse)
async def images(request: Request):
    """Cтраница Изображений сервиса."""

    return templates.TemplateResponse(request=request, name="images.html", context={})


@app.get("/upload/", response_class=HTMLResponse)
async def upload(request: Request):
    """Cтраница загрузки изображения."""

    return templates.TemplateResponse(request=request, name="upload.html", context={})


@app.post("/upload/")
async def upload(request: Request, file: UploadFile = File(...)):
    """Cтраница загрузки изображения. POST"""

    my_file = Path(file.filename)
    logging.info(f"Получен файл: {file.filename}")

    if not is_allowed_file(my_file):
        logging.error(f"Неподдерживаемый формат файла {my_file}")
        raise HTTPException(status_code=400, detail="Неподдерживаемый формат файла")

    contents = await file.read(MAX_UPLOAD_SIZE + 1)
    if len(contents) > MAX_UPLOAD_SIZE:
        logging.error(f"Файл слишком большой {my_file}")
        raise HTTPException(status_code=400, detail="Файл слишком большой")

    new_file_name = get_unique_name(my_file)
    logging.info(f'New File name: {new_file_name}')

    image_dir = Path("images")
    image_dir.mkdir(exist_ok=True)
    save_path = image_dir / new_file_name
    save_path.write_bytes(contents)
    logging.info(f'Файл {str(save_path)} записан')

    return templates.TemplateResponse(request=request, name="upload.html", context={})


if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)