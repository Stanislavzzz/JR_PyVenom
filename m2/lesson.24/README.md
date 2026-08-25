    "fastapi (>=0.141.1,<0.142.0)",
    "pillow (>=12.3.0,<13.0.0)",
    "uvicorn (>=0.52.3,<0.53.0)"

pip freeze > requirements.txt

uvicorn app:app --reload --host 0.0.0.0 --port 8000