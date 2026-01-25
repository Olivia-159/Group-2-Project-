import pygame

def bid_screen():
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 750, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Place Your Bid")

    font = pygame.font.Font(None, 36)

    # Back button settings
    BACK_BUTTON_WIDTH = 67
    BACK_BUTTON_HEIGHT = 36
    BACK_BUTTON_X = 20
    BACK_BUTTON_Y = 20

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        screen.fill((30, 30, 50))
        text = font.render("Bid Screen", True, (255, 105, 180))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))

        # Draw back button
        back_button_rect = pygame.Rect(BACK_BUTTON_X, BACK_BUTTON_Y, BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT)
        back_button_color = (100, 100, 150) if back_button_rect.collidepoint(mouse_pos) else (255, 80, 80)
        pygame.draw.rect(screen, back_button_color, back_button_rect, border_radius=8)
        pygame.draw.rect(screen, (128, 0, 128), back_button_rect, 2, border_radius=8)

        small_font = pygame.font.Font(None, 28)
        back_text = small_font.render("Back", True, (255, 255, 255))
        screen.blit(back_text, (BACK_BUTTON_X + 10, BACK_BUTTON_Y + 8))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(mouse_pos):
                    running = False

    pygame.quit()