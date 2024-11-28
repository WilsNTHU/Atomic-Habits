import pygame
import sys
import json
import os

# File to store game data
DATA_FILE = "game_data.json"

# Function to load game data
def load_game_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {"number": 1.01, "clicks": 0}

# Function to save game data
def save_game_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# Load initial data
game_data = load_game_data()
number = game_data["number"]
clicks = game_data["clicks"]

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Atomic Habits")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (200, 200, 200)

# Font
font_large = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 36)

def draw_screen(number, clicks):
    screen.fill(black)
    
    # Display the current number
    number_text = font_large.render(f"Number: {number:.5f}", True, white)
    number_rect = number_text.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(number_text, number_rect)
    
    # Display the click count
    clicks_text = font_small.render(f"Total Clicks: {clicks}", True, white)
    clicks_rect = clicks_text.get_rect(center=(width // 2, height // 2 + 50))
    screen.blit(clicks_text, clicks_rect)
    
    # Draw reset button
    reset_rect = pygame.Rect(width // 2 - 60, height - 100, 120, 50)
    pygame.draw.rect(screen, red, reset_rect)
    reset_text = font_small.render("Reset", True, white)
    reset_text_rect = reset_text.get_rect(center=reset_rect.center)
    screen.blit(reset_text, reset_text_rect)
    
    pygame.display.flip()

# Main loop
running = True
while running:
    draw_screen(number, clicks)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Save data before quitting
            save_game_data({"number": number, "clicks": clicks})
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button click
            mouse_x, mouse_y = event.pos
            
            # Center click for number multiplication
            center_rect = pygame.Rect(width // 2 - 50, height // 2 - 50, 100, 100)
            if center_rect.collidepoint(mouse_x, mouse_y):
                number *= 1.01
                clicks += 1
            
            # Check for reset button click
            reset_rect = pygame.Rect(width // 2 - 60, height - 100, 120, 50)
            if reset_rect.collidepoint(mouse_x, mouse_y):
                number = 1.01
                clicks = 0

pygame.quit()
sys.exit()
