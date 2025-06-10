# Используем официальный образ Python как базовый
FROM python:3.11

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    ffmpeg \
    wget \
    unzip \
    libasound2-dev \
    portaudio19-dev \
    && apt-get clean \
    pip install --upgrade pip

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем Python зависимости
RUN pip install fastapi uvicorn pydub vosk aiofiles pyaudio aiofiles

# Создаем директорию для модели
RUN mkdir -p /app/model

# Скачиваем архив с моделью
RUN wget -O /app/model/vosk-model-small-ru-0.22.zip https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip

# Открываем порт, на котором будет работать приложение
EXPOSE 8765

# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8765"]
