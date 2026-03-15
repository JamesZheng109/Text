import pygame
pygame.init()
def play_sfx(sound,length=0,volume=None):
    '''play sfx
lenght=How many times sfx will be played
'''
    noise=pygame.mixer.Sound(sound)
    noise.play(length)
    if volume!=None:
        noise.set_volume(volume)
    return noise
def play_music(song,volume=1):
    '''play song'''
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)
def pause_music(state:0):
    '''pauses and unpauses based on state'''
    if state==0:
        pygame.mixer.music.pause()
    elif state==1:
        pygame.mixer.music.unpause()
    elif state==2:
        pygame.mixer.music.unload()
