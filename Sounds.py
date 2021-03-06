import pygame


class Sounds:
    def __init__(self):
        pygame.mixer.music.load('Resources/Kirby_Gourmet_Race.ogg')
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.play(-1)

        self.mistake_sound = pygame.mixer.Sound('Resources/mistake.ogg')
        self.tool_change_sound = pygame.mixer.Sound('Resources/tool_change.ogg')
        self.snow_clean_sound = pygame.mixer.Sound('Resources/snow.ogg')
        self.leaves_clean_sound = pygame.mixer.Sound('Resources/leaves.ogg')
        self.win_sound = pygame.mixer.Sound('Resources/win.ogg')

        self.is_playing = True

    def tool_change(self):
        self.tool_change_sound.play()

    def clean(self, terrain):
        if terrain == 'snow':
            self.snow_clean_sound.play()
        else:
            self.leaves_clean_sound.play()

    def mistake(self):
        self.mistake_sound.play()

    def pause(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
        else:
            pygame.mixer.music.unpause()
            self.is_playing = True

    def win(self):
        self.win_sound.play()
