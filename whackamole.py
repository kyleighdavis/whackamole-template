import pygame
import random

#hello world
# comment 2
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        line_color = (0, 0, 0)
        screen.fill("light green")

        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        mole_pos = (0,0)
        running = True
        while running:
            for i in range(1, 16):
                pygame.draw.line(
                    screen,
                    line_color,
                    (0, i * 32),
                    (640, i * 32)
                )
            for i in range(1, 20):
                pygame.draw.line(
                    screen,
                    line_color,
                    (i * 32, 0),
                    (i * 32, 512)
                )
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row = y//32
                    col = x//32
                    event_pos = (row, col)
                    if event_pos == mole_pos:
                        random_col = random.randrange(0,16)
                        random_row = random.randrange(0,20)
                        row_pos = random_row * 32
                        col_pos = random_col * 32
                        screen.fill("light green")
                        screen.blit(mole_image, mole_image.get_rect(topleft=(row_pos, col_pos)))
                        mole_pos = (col_pos//32, row_pos//32)
            pygame.display.flip()
            clock.tick(60)



    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
