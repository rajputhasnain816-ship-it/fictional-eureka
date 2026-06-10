import pygame
import sys
from datetime import datetime
import pytz

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Digital Clock - Multiple Time Zones")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BG = (15, 15, 35)
NEON_GREEN = (0, 255, 100)
NEON_BLUE = (0, 150, 255)
NEON_PURPLE = (200, 0, 255)
NEON_PINK = (255, 0, 127)
NEON_ORANGE = (255, 150, 0)
NEON_CYAN = (0, 255, 255)
DARK_GRAY = (40, 40, 50)
LIGHT_GRAY = (200, 200, 200)

# Clock
clock = pygame.time.Clock()
FPS = 1  # Update every second

# Fonts
main_font = pygame.font.Font(None, 80)
timezone_font = pygame.font.Font(None, 32)
info_font = pygame.font.Font(None, 24)
title_font = pygame.font.Font(None, 48)

# Define time zones with colors
TIMEZONES = [
    {"name": "New York (EST)", "zone": "America/New_York", "color": NEON_BLUE},
    {"name": "London (GMT)", "zone": "Europe/London", "color": NEON_GREEN},
    {"name": "Tokyo (JST)", "zone": "Asia/Tokyo", "color": NEON_PINK},
    {"name": "Sydney (AEDT)", "zone": "Australia/Sydney", "color": NEON_ORANGE},
    {"name": "Dubai (GST)", "zone": "Asia/Dubai", "color": NEON_CYAN},
    {"name": "Los Angeles (PST)", "zone": "America/Los_Angeles", "color": NEON_PURPLE},
]

class DigitalClock:
    def __init__(self, x, y, timezone_info, width=300, height=180):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.timezone_info = timezone_info
        self.tz = pytz.timezone(timezone_info["zone"])
        self.color = timezone_info["color"]
        self.selected = False
        
    def update(self):
        pass
    
    def draw(self, surface):
        # Draw background rectangle
        pygame.draw.rect(surface, DARK_GRAY, (self.x, self.y, self.width, self.height), border_radius=15)
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), 3, border_radius=15)
        
        # Add glow effect for selected clock
        if self.selected:
            pygame.draw.rect(surface, self.color, (self.x - 5, self.y - 5, self.width + 10, self.height + 10), 2, border_radius=15)
        
        # Get current time in this timezone
        now = datetime.now(self.tz)
        time_str = now.strftime("%H:%M:%S")
        date_str = now.strftime("%A, %b %d")
        
        # Draw time
        time_surface = main_font.render(time_str, True, self.color)
        time_rect = time_surface.get_rect(center=(self.x + self.width // 2, self.y + 60))
        surface.blit(time_surface, time_rect)
        
        # Draw timezone name
        tz_surface = timezone_font.render(self.timezone_info["name"], True, self.color)
        tz_rect = tz_surface.get_rect(center=(self.x + self.width // 2, self.y + 130))
        surface.blit(tz_surface, tz_rect)
        
        # Draw date on hover (if selected)
        if self.selected:
            date_surface = info_font.render(date_str, True, LIGHT_GRAY)
            date_rect = date_surface.get_rect(center=(self.x + self.width // 2, self.y + 160))
            surface.blit(date_surface, date_rect)
    
    def is_clicked(self, pos):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return rect.collidepoint(pos)
    
    def get_time_info(self):
        now = datetime.now(self.tz)
        return {
            "time": now.strftime("%H:%M:%S"),
            "date": now.strftime("%A, %B %d, %Y"),
            "timezone": self.timezone_info["name"],
            "offset": now.strftime("%z")
        }

class WorldClock:
    def __init__(self):
        self.clocks = []
        self.setup_clocks()
        self.selected_clock = None
        
    def setup_clocks(self):
        # Arrange clocks in a 3x2 grid
        positions = [
            (80, 150),      # Top-left
            (750, 150),     # Top-right
            (80, 450),      # Middle-left
            (750, 450),     # Middle-right
            (80, 750),      # Bottom-left
            (750, 750),     # Bottom-right
        ]
        
        for i, (x, y) in enumerate(positions):
            if i < len(TIMEZONES):
                clock = DigitalClock(x, y, TIMEZONES[i])
                self.clocks.append(clock)
    
    def handle_click(self, pos):
        for clock in self.clocks:
            if clock.is_clicked(pos):
                # Deselect previous
                if self.selected_clock:
                    self.selected_clock.selected = False
                # Select new
                clock.selected = True
                self.selected_clock = clock
                return
        
        # Deselect if clicked elsewhere
        if self.selected_clock:
            self.selected_clock.selected = False
            self.selected_clock = None
    
    def draw(self, surface):
        # Draw title
        title = title_font.render("⏰ WORLD CLOCK", True, NEON_CYAN)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 40))
        surface.blit(title, title_rect)
        
        # Draw subtitle
        subtitle = info_font.render("Click on a clock to see more details", True, LIGHT_GRAY)
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, 95))
        surface.blit(subtitle, subtitle_rect)
        
        # Draw all clocks
        for digital_clock in self.clocks:
            digital_clock.draw(surface)
        
        # Draw info panel if a clock is selected
        if self.selected_clock:
            self.draw_info_panel(surface, self.selected_clock)
    
    def draw_info_panel(self, surface, clock):
        info = clock.get_time_info()
        
        # Panel dimensions
        panel_x = SCREEN_WIDTH - 400
        panel_y = 150
        panel_width = 350
        panel_height = 250
        
        # Draw panel background
        pygame.draw.rect(surface, DARK_GRAY, (panel_x, panel_y, panel_width, panel_height), border_radius=15)
        pygame.draw.rect(surface, clock.color, (panel_x, panel_y, panel_width, panel_height), 2, border_radius=15)
        
        # Draw panel title
        title = info_font.render("DETAILS", True, clock.color)
        surface.blit(title, (panel_x + 20, panel_y + 15))
        
        # Draw info lines
        y_offset = panel_y + 60
        line_spacing = 50
        
        lines = [
            ("Time:", info["time"]),
            ("Date:", info["date"]),
            ("Zone:", info["timezone"]),
            ("Offset:", info["offset"]),
        ]
        
        for label, value in lines:
            label_surf = info_font.render(label, True, LIGHT_GRAY)
            value_surf = info_font.render(value, True, clock.color)
            
            surface.blit(label_surf, (panel_x + 20, y_offset))
            surface.blit(value_surf, (panel_x + 20, y_offset + 25))
            
            y_offset += line_spacing

# Create the world clock
world_clock = WorldClock()

# Game loop
running = True

while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            world_clock.handle_click(event.pos)
    
    # Draw everything
    screen.fill(DARK_BG)
    world_clock.draw(screen)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
