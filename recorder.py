import pyaudio
import wave

# تنظیمات ضبط صدا
audio_format = pyaudio.paInt16
channels = 1
sample_rate = 44100
chunk_size = 1024
record_time = 5  # مدت زمان ضبط به ثانیه

# ایجاد شیء PyAudio
audio = pyaudio.PyAudio()

# ایجاد شیء stream برای ضبط صدا
stream = audio.open(format=audio_format, channels=channels, rate=sample_rate,
                    input=True, frames_per_buffer=chunk_size)

# ضبط صدا
frames = []
print('Recording...')
for i in range(int(sample_rate / chunk_size * record_time)):
    data = stream.read(chunk_size)
    frames.append(data)
print('Finished recording.')

# تمیز کردن و ذخیره فایل صوتی
stream.stop_stream()
stream.close()
audio.terminate()

file_name = 'my_record.wav'
wave_file = wave.open(file_name, 'wb')
wave_file.setnchannels(channels)
wave_file.setsampwidth(audio.get_sample_size(audio_format))
wave_file.setframerate(sample_rate)
wave_file.writeframes(b''.join(frames))
wave_file.close()
