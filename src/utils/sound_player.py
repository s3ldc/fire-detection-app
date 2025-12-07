# sound_player.py (using pygame)
import pygame
import threading

pygame.mixer.init()

def play_alert_sound(path="assets/alert_sound.mp3"):
    def _play():
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

    threading.Thread(target=_play, daemon=True).start()
