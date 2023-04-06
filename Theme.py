import pygame_menu

mytheme = pygame_menu.themes.THEME_ORANGE.copy()
mybg = pygame_menu.baseimage.BaseImage(
    image_path="assets/menu_bg.jpg",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY
)
mytheme.background_color = mybg
