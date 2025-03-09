# plays music in the background, import background_music in master, change actual music file

from just_playback import Playback
playback = Playback()
playback.load_file('music-files/sample.mp3')


playback.play()

