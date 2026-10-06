import pygame

class AlertModule:
    def __init__(self):
        pygame.mixer.init()

    def mild_alert(self):
        print("[WARNING] Slight Drowsiness Detected")
        pygame.mixer.music.load("sounds/beep1.wav")
        pygame.mixer.music.play()

    def severe_alert(self):
        print("[DANGER] High Drowsiness Detected")
        pygame.mixer.music.load("sounds/beep2.wav")
        pygame.mixer.music.play()

    def voice_alert(self):
        print("[VOICE] Please take a break immediately")
        pygame.mixer.music.load("sounds/take_break.wav")
        pygame.mixer.music.play()
