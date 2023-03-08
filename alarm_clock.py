# Program a simple alarm clock that plays a sound after a few minutes/seconds.
# 
# Started: 6 March 2023
# Completed: xx March 2023

# import time
# # from pydub import AudioSegment
# # from pydub.playback import play
# import sounddevice as sd
# import soundfile as sf

# # song = AudioSegment.from_wav("alarm-tone.wav")

# filename = 'alarm-tone.wav'
# data, fs = sf.read(filename, dtype='float32')  

# user_seconds = float(input("How many seconds do you want to wait before the alarm goes off? "))
# user_minutes = float(input("How many minutes do you want to wait before the alarm goes off? "))
# user_hours = float(input("How many hours do you want to wait before the alarm goes off? "))

# print("")
# timer_seconds = float(user_seconds + (user_minutes * 60) + (user_hours * 60 * 60))

# print("Waiting...")
# time.sleep(timer_seconds)
# # play(song)
# # print("Alarm went off...")
# sd.play(data, fs)
# status = sd.wait()

from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_wav('alarm-tone.wav')
play(sound)
