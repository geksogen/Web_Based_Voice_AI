# Используем официальный образ Python как базовый
FROM python:3.11

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libasound2-dev \
    portaudio19-dev \
    && apt-get clean \
    pip install --upgrade pip

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir fastapi uvicorn pydub vosk aiofiles pyaudio aiofiles

# Копируем модель Vosk в контейнер (предполагается, что модель находится в папке "model")
COPY model /app/model

# Открываем порт, на котором будет работать приложение
EXPOSE 8765

# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8765"]
