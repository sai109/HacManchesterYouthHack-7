import pygame
import glob
# import pyganim
#
# pygame.init()
#
# size = width, height = 320, 240
# speed = [2, 2]
# black = 0, 0, 0
#
# screen = pygame.display.set_mode(size)
array = glob.glob('*.png')
finalArray = list(map(lambda x: (x, 200), array))
print(finalArray)
