import pygame.mixer
import os
pygame.init()
music_folder = "C:/Users/leedm/pp2-22B030387/TSIS7/songs"
_songs = []
for file in os.listdir("./songs"):
    if file.endswith(".mp3"):
        _songs.append(file)

current_song = 0
pygame.mixer.init()
pygame.mixer.music.load("./songs/dxrk-rave-mp3.mp3")
screen = pygame.display.set_mode((640, 480))
font = pygame.font.Font(None, 100)
text = font.render("PHONK", True, (255, 255, 255))
print(_songs)

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_song
    current_song += 1
    if current_song >= len(_songs):
        current_song = 0
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(music_folder, _songs[current_song]))
    pygame.mixer.music.play()

def previous_track():
    global current_song
    current_song -= 1
    if current_song < 0:
        current_song = len(_songs) - 1
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(music_folder, _songs[current_song]))
    pygame.mixer.music.play()

while True:
    screen.blit(text, (190, 190))
    for event in pygame.event.get():
        if event.type == SONG_END:
            next_track()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                previous_track()
        elif event.type == pygame.QUIT:  # quit
            pygame.mixer.music.stop()
            pygame.quit()
            exit()
    pygame.display.flip()
