from pygame import mixer
import pygame

#need to download a mp3 file and add it on the same folder with everything else
mp3_file = "filename.mp3"

mixer.init()

mixer.music.load(mp3_file)
mixer.music.play()

while mixer.music.get_busy():
    pygame.time.Clock().tick(10)

#okei elikkäs tällä koodilla kyllä musiikki soi, mutta se soi ensin loppuun ennen kuin mitään muuta tapahtuu eli
#täytyy vielä selvittää miten musiikin saa nimenomaan taustalle
#ja sit täytyy ladata musiikkia jeejee