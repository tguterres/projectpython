# MP3 Play
from pygame import mixer
mixer.init()
mixer.music.load('audioslave.mp3')
mixer.music.play()
mixer.event.wait()

