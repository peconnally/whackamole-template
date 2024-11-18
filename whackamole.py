import pygame
import random
#make a comment
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_loc = (0,0)
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    adj_x = x // 32
                    adj_y = y // 32
                    topleft = (adj_x*32, adj_y*32)
                    if topleft == mole_loc:
                        newx = random.randrange(0,20) * 32
                        newy = random.randrange(0,16) * 32
                        mole_loc = (newx,newy)
            screen.fill("white")
            for i in range(1, 20):
                pygame.draw.line(screen, "dark blue", (32*i, 0), (32*i, 512))
            for i in range(1, 16):
                pygame.draw.line(screen, "dark blue", (0, 32*i), (640, 32*i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_loc[0], mole_loc[1])))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
