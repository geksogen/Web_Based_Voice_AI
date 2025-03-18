from fastapi import FastAPI, WebSocket
import uvicorn
import signal
import json
import aiofiles
import pyaudio
import os
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment

AudioSegment.converter = 'c:\\ffmpeg\\ffmpeg.exe'

app = FastAPI()

# Параметры записи
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 8192

# Инициализация PyAudio
audio = pyaudio.PyAudio()

# Путь к модели Vosk
model_path = "model"

# Проверяем, существует ли модель
if not os.path.exists(model_path):
    print(f"Модель не найдена в {model_path}")
else:
    # Загружаем модель
    model = Model(model_path)
    # Создаем распознаватель
    recognizer = KaldiRecognizer(model, RATE)

@app.websocket( "/ws" )
async def websocket_endpoint (websocket: WebSocket):
    try:
        await websocket.accept()
        while True:
            audio_data = await websocket.receive_bytes()

            async with aiofiles.open("audio.webm", 'wb') as out_file:
                await out_file.write(audio_data)

            # Загружаем файл
            audio = AudioSegment.from_file("audio.webm", format="webm")
            # Преобразование в моно (один канал)
            audio = audio.set_channels(1)
            # Установка частоты дискретизации 16000 Гц
            audio = audio.set_frame_rate(16000)
            # Установка размера сэмпла 16 бит
            audio = audio.set_sample_width(2)
            # Экспорт в формат WAV
            audio.export("audio.wav", format="wav")

            # Чтение аудиофайла
            wf = AudioSegment.from_wav("audio.wav")
            wf = wf.set_channels(1)
            wf = wf.set_frame_rate(RATE)

            recognizer.AcceptWaveform(wf.raw_data)
            result = recognizer.Result()
            result_dict = json.loads(result)
            text = result_dict.get("text", "")
            print("Распознанный текст: ", text)

            await websocket.send_json({"input": text,"response": text})
    except Exception as e:
        print("Error:", e)

def handle_shutdown(signal_num, frame):
    print(f"Received shutdown signal: {signal_num}")
def setup_signal_handlers():
    signal.signal(signal.SIGTERM, handle_shutdown)
    signal.signal(signal.SIGINT, handle_shutdown)

if __name__ == "__main__":
    setup_signal_handlers()
    config = uvicorn.Config("main:app", port=8765, log_level="info")
    server = uvicorn.Server(config)
    server.run()


