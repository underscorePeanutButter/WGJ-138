import pygame
import sys

screen_width = 700
screen_height = 500
screen_dimensions = (screen_width, screen_height)

black = (0, 0, 0)
white = (255, 255, 255)

console = pygame.display.set_mode(screen_dimensions)

console_text_lines = []

def print_to_console(text):
    console_text_lines.append(text)

def input_on_console():
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for i in range(1, len(console_text_lines) + 1):
        pass

    console.fill(black)
