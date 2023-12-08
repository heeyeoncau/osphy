import pygame
import pygame_menu
import play

pygame.init()
surface = pygame.display.set_mode((600,400))

ABOUT=['Use your mouse to control your balls to move',
        'Q: to eject spore in your moving direction',
        'W: to split your balls',
        '',
        'OSPHY_2023_2']
WINDOW_SIZE = (600,400)
THEME = pygame_menu.themes.THEME_DARK
MODE = ['Partial vision','Full vision']
selected_mode = 0

from typing import Tuple, Any

def set_mode(value: Tuple[Any, int], mode: str):
    global selected_mode
    selected_mode = value[1]

    selected, index = value
    print(f'Selected mode: "{selected}" ({mode}) at index {index}')


def start_the_game():    
    global selected_mode

    if selected_mode == 0:
       play.play_partial_against_bot()
    else:
        play.play_all_against_bot()

#ABOUT(How to Play)
about_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.6,
        theme=THEME,
        title='How to Play',
        width=WINDOW_SIZE[0] * 0.6
)
for m in ABOUT:
    about_menu.add.label(m,align=pygame_menu.locals.ALIGN_CENTER, font_size=15)

#MAIN
main_menu = pygame_menu.Menu('GoBigger',400,300,
                        theme= THEME )

main_menu.add.button('Play',start_the_game)
main_menu.add.selector('Mode:  ',[('Partial vision',1),('Full vision',2)],onchange=set_mode)
main_menu.add.button('How to Play',about_menu)
main_menu.add.button('Quit',pygame_menu.events.EXIT)

main_menu.mainloop(surface)