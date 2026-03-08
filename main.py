import pygame
import sys
from game import Game

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (100, 150, 200)
GREEN = (100, 200, 100)
RED = (200, 100, 100)

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Matching Puzzle - Sujal Win Puzzle")

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2

def draw_menu():
    screen.fill(BLUE)
    font_large = pygame.font.Font(None, 60)
    font_small = pygame.font.Font(None, 40)
    
    title = font_large.render("Memory Matching", True, WHITE)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
    screen.blit(title, title_rect)
    
    subtitle = font_small.render("Sujal Win Puzzle", True, WHITE)
    subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, 220))
    screen.blit(subtitle, subtitle_rect)
    
    instruction = font_small.render("Press SPACE to Start", True, WHITE)
    instruction_rect = instruction.get_rect(center=(SCREEN_WIDTH // 2, 350))
    screen.blit(instruction, instruction_rect)
    
    info = pygame.font.Font(None, 30).render("Find all 8 pairs in 30 moves!", True, WHITE)
    info_rect = info.get_rect(center=(SCREEN_WIDTH // 2, 450))
    screen.blit(info, info_rect)
    
    exit_text = pygame.font.Font(None, 25).render("Press ESC to Exit", True, WHITE)
    exit_rect = exit_text.get_rect(center=(SCREEN_WIDTH // 2, 600))
    screen.blit(exit_text, exit_rect)

def draw_game(game):
    screen.fill(BLACK)
    
    # Draw title
    font = pygame.font.Font(None, 40)
    title = font.render("Memory Matching Puzzle", True, WHITE)
    screen.blit(title, (150, 20))
    
    # Draw game board
    game.draw(screen)
    
    # Draw stats
    stats_font = pygame.font.Font(None, 30)
    moves_text = stats_font.render(f"Moves: {game.moves}/{game.max_moves}", True, WHITE)
    pairs_text = stats_font.render(f"Pairs Found: {game.pairs_found}/8", True, WHITE)
    
    screen.blit(moves_text, (50, 550))
    screen.blit(pairs_text, (50, 590))

def draw_game_over(game):
    screen.fill(BLACK)
    
    font_large = pygame.font.Font(None, 60)
    font_small = pygame.font.Font(None, 40)
    
    if game.won:
        message = font_large.render("YOU WON!", True, GREEN)
        detail = font_small.render(f"Matched all 8 pairs in {game.moves} moves!", True, WHITE)
    else:
        message = font_large.render("GAME OVER!", True, RED)
        detail = font_small.render(f"Out of moves. Found {game.pairs_found}/8 pairs", True, WHITE)
    
    message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, 250))
    detail_rect = detail.get_rect(center=(SCREEN_WIDTH // 2, 350))
    
    screen.blit(message, message_rect)
    screen.blit(detail, detail_rect)
    
    restart_text = font_small.render("Press SPACE to Play Again", True, WHITE)
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, 450))
    screen.blit(restart_text, restart_rect)
    
    exit_text = pygame.font.Font(None, 30).render("Press ESC to Menu", True, WHITE)
    exit_rect = exit_text.get_rect(center=(SCREEN_WIDTH // 2, 550))
    screen.blit(exit_text, exit_rect)

def main():
    state = MENU
    game = None
    
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if state == MENU:
                        running = False
                    else:
                        state = MENU
                
                if event.key == pygame.K_SPACE:
                    if state == MENU:
                        game = Game()
                        state = PLAYING
                    elif state == GAME_OVER:
                        game = Game()
                        state = PLAYING
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if state == PLAYING:
                    game.handle_click(event.pos[0], event.pos[1])
        
        # Update
        if state == PLAYING:
            game.update()
            if game.game_over:
                state = GAME_OVER
        
        # Draw
        if state == MENU:
            draw_menu()
        elif state == PLAYING:
            draw_game(game)
        elif state == GAME_OVER:
            draw_game_over(game)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()