import pygame
import matplotlib
import numpy as np

pygame.font.init()
pygame.mixer.init()
win = pygame.display.set_mode((900, 700))

class PetInformation():
    def __init__(self, name, age, weight, type, breed, xp, nutrition_database_fn, exercise_database_fn, nutritional_requirements, exercise_requirements):
        self.set_value(name)
        self.set_value(age)
        self.set_value(weight)
        self.set_value(type)
        self.set_value(breed)
        self.set_value(xp)
        self.set_value(nutrition_database_fn)
        self.set_value(exercise_database_fn)
        self.set_value(nutritional_requirements)
        self.set_value(exercise_requirements)
    def get_value(self, text):
        return self._text
    def set_value(self, value):
        self._text = value.lower()

def home_screen():



def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
            else:
                print(event)

        win.fill((255, 255, 255))
        pygame.display.flip()
    pygame.quit()
