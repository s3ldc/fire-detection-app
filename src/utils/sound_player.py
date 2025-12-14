# sound_player.py
import pygame
import threading

pygame.mixer.init()

is_playing = False   # Global audio lock


def _play_sound(path):
    global is_playing
    is_playing = True

    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    # wait until sound finishes
    while pygame.mixer.music.get_busy():
        pass

    is_playing = False  # allow next play


def play_alert_sound(path="assets/alert_sound.mp3"):
    global is_playing

    # If already playing, do nothing
    if is_playing:
        return

    # Otherwise start a new thread
    threading.Thread(target=_play_sound, args=(path,), daemon=True).start()
