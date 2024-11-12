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
        for i in range(1, 16):
            pygame.draw.line(
                screen,
                line_color,
                (0, i*32),
                (640, i*32)
            )
        for i in range(1, 20):
            pygame.draw.line(
                screen,
                line_color,
                (i*32, 0),
                (i*32, 512)
            )

        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos == pygame.mouse.get_pos():
                        random_row = random.randrange(0,16)
            pygame.display.flip()
            clock.tick(60)



    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
