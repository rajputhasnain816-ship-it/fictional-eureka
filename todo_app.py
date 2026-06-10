import pygame
import sys
import json
import os
from datetime import datetime

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("To-Do List Application")

# Colors
DARK_BG = (20, 20, 40)
CARD_BG = (30, 40, 70)
INPUT_BG = (40, 50, 80)
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 120)
NEON_BLUE = (0, 150, 255)
NEON_GREEN = (50, 255, 100)
NEON_RED = (255, 60, 60)
NEON_YELLOW = (255, 220, 0)
NEON_PURPLE = (180, 60, 255)
NEON_CYAN = (0, 255, 200)
COMPLETED_COLOR = (100, 150, 100)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Fonts
title_font = pygame.font.Font(None, 56)
large_font = pygame.font.Font(None, 40)
normal_font = pygame.font.Font(None, 28)
small_font = pygame.font.Font(None, 22)
tiny_font = pygame.font.Font(None, 18)

# Data storage
DATA_FILE = "todos.json"

class Task:
    def __init__(self, title, description="", priority="normal", due_date=None, task_id=None):
        self.id = task_id or datetime.now().timestamp()
        self.title = title
        self.description = description
        self.priority = priority  # low, normal, high
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date,
            "completed": self.completed,
            "created_at": self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        task = Task(
            data["title"],
            data.get("description", ""),
            data.get("priority", "normal"),
            data.get("due_date"),
            data.get("id")
        )
        task.completed = data.get("completed", False)
        task.created_at = data.get("created_at")
        return task
    
    def get_priority_color(self):
        if self.priority == "high":
            return NEON_RED
        elif self.priority == "normal":
            return NEON_YELLOW
        else:
            return NEON_CYAN

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.input_text = ""
        self.input_active = False
        self.selected_task = None
        self.filter_mode = "all"  # all, active, completed
        self.sort_mode = "date"  # date, priority
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
            except Exception as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        try:
            with open(DATA_FILE, 'w') as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, title, priority="normal"):
        """Add a new task"""
        if title.strip():
            task = Task(title.strip(), priority=priority)
            self.tasks.insert(0, task)
            self.save_tasks()
            self.input_text = ""
            return True
        return False
    
    def delete_task(self, task_id):
        """Delete a task"""
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.save_tasks()
    
    def toggle_task(self, task_id):
        """Toggle task completion status"""
        for task in self.tasks:
            if task.id == task_id:
                task.completed = not task.completed
                break
        self.save_tasks()
    
    def get_filtered_tasks(self):
        """Get tasks based on filter"""
        if self.filter_mode == "active":
            return [t for t in self.tasks if not t.completed]
        elif self.filter_mode == "completed":
            return [t for t in self.tasks if t.completed]
        else:
            return self.tasks
    
    def get_sorted_tasks(self):
        """Get filtered and sorted tasks"""
        tasks = self.get_filtered_tasks()
        if self.sort_mode == "priority":
            priority_order = {"high": 0, "normal": 1, "low": 2}
            tasks.sort(key=lambda t: (t.completed, priority_order.get(t.priority, 1)))
        else:
            tasks.sort(key=lambda t: t.completed)
        return tasks
    
    def get_stats(self):
        """Get task statistics"""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.completed)
        active = total - completed
        high_priority = sum(1 for t in self.tasks if t.priority == "high" and not t.completed)
        
        return {
            "total": total,
            "completed": completed,
            "active": active,
            "high_priority": high_priority
        }
    
    def draw_header(self, surface):
        """Draw the header"""
        title = title_font.render("✓ TO-DO LIST", True, NEON_CYAN)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 30))
        surface.blit(title, title_rect)
        
        # Stats
        stats = self.get_stats()
        stats_text = f"Total: {stats['total']} | Active: {stats['active']} | Completed: {stats['completed']} | High Priority: {stats['high_priority']}"
        stats_surf = small_font.render(stats_text, True, LIGHT_GRAY)
        surface.blit(stats_surf, (50, 80))
    
    def draw_input_section(self, surface):
        """Draw the task input section"""
        input_y = 130
        input_height = 50
        input_width = SCREEN_WIDTH - 100
        input_x = 50
        
        # Input box background
        color = NEON_BLUE if self.input_active else DARK_GRAY
        pygame.draw.rect(surface, INPUT_BG, (input_x, input_y, input_width, input_height), border_radius=10)
        pygame.draw.rect(surface, color, (input_x, input_y, input_width, input_height), 2, border_radius=10)
        
        # Input text
        text_surf = normal_font.render(self.input_text or "Add a new task...", True, 
                                       WHITE if self.input_text else DARK_GRAY)
        surface.blit(text_surf, (input_x + 15, input_y + 10))
        
        # Cursor
        if self.input_active:
            cursor_x = input_x + 15 + text_surf.get_width()
            pygame.draw.line(surface, NEON_BLUE, (cursor_x, input_y + 10), (cursor_x, input_y + 40), 2)
        
        # Priority selector buttons
        button_y = input_y
        button_height = input_height
        button_width = 80
        priority_x = input_x + input_width + 20
        
        priorities = ["Low", "Normal", "High"]
        colors = [NEON_CYAN, NEON_YELLOW, NEON_RED]
        
        for i, (priority, color) in enumerate(zip(priorities, colors)):
            bx = priority_x + i * (button_width + 10)
            pygame.draw.rect(surface, color, (bx, button_y, button_width, button_height), 2, border_radius=10)
            text = small_font.render(priority, True, color)
            text_rect = text.get_rect(center=(bx + button_width // 2, button_y + button_height // 2))
            surface.blit(text, text_rect)
    
    def draw_filter_buttons(self, surface):
        """Draw filter and sort buttons"""
        button_y = 200
        button_height = 35
        button_width = 100
        spacing = 15
        
        # Filter buttons
        filters = ["All", "Active", "Completed"]
        filter_x = 50
        
        for i, filter_name in enumerate(filters):
            x = filter_x + i * (button_width + spacing)
            is_selected = self.filter_mode == filter_name.lower()
            color = NEON_GREEN if is_selected else DARK_GRAY
            
            pygame.draw.rect(surface, color, (x, button_y, button_width, button_height), 2 if not is_selected else 0, border_radius=8)
            if is_selected:
                pygame.draw.rect(surface, color, (x, button_y, button_width, button_height), fill=True, border_radius=8)
            
            text_color = DARK_BG if is_selected else color
            text = small_font.render(filter_name, True, text_color)
            text_rect = text.get_rect(center=(x + button_width // 2, button_y + button_height // 2))
            surface.blit(text, text_rect)
        
        # Sort buttons
        sorts = ["By Date", "By Priority"]
        sort_x = 50 + 400
        
        for i, sort_name in enumerate(sorts):
            x = sort_x + i * (button_width + spacing)
            is_selected = (sort_name == "By Date" and self.sort_mode == "date") or \
                         (sort_name == "By Priority" and self.sort_mode == "priority")
            color = NEON_PURPLE if is_selected else DARK_GRAY
            
            pygame.draw.rect(surface, color, (x, button_y, button_width, button_height), 2 if not is_selected else 0, border_radius=8)
            if is_selected:
                pygame.draw.rect(surface, color, (x, button_y, button_width, button_height), fill=True, border_radius=8)
            
            text_color = DARK_BG if is_selected else color
            text = small_font.render(sort_name, True, text_color)
            text_rect = text.get_rect(center=(x + button_width // 2, button_y + button_height // 2))
            surface.blit(text, text_rect)
    
    def draw_tasks(self, surface):
        """Draw the task list"""
        tasks = self.get_sorted_tasks()
        
        if not tasks:
            no_tasks = normal_font.render("No tasks yet! Add one to get started.", True, DARK_GRAY)
            surface.blit(no_tasks, (50, 300))
            return
        
        task_y = 260
        task_height = 70
        task_spacing = 15
        max_tasks = 9
        
        for i, task in enumerate(tasks[:max_tasks]):
            task_x = 50
            task_width = SCREEN_WIDTH - 100
            
            # Task background
            task_bg_color = CARD_BG if not task.completed else (40, 60, 50)
            pygame.draw.rect(surface, task_bg_color, (task_x, task_y, task_width, task_height), border_radius=10)
            
            # Priority indicator
            priority_color = task.get_priority_color()
            pygame.draw.rect(surface, priority_color, (task_x, task_y, 5, task_height), border_radius=10)
            
            # Checkbox
            checkbox_x = task_x + 15
            checkbox_y = task_y + 15
            checkbox_size = 30
            checkbox_color = NEON_GREEN if task.completed else DARK_GRAY
            pygame.draw.rect(surface, checkbox_color, (checkbox_x, checkbox_y, checkbox_size, checkbox_size), 2)
            
            if task.completed:
                pygame.draw.line(surface, NEON_GREEN, (checkbox_x + 5, checkbox_y + 15), 
                               (checkbox_x + 12, checkbox_y + 22), 3)
                pygame.draw.line(surface, NEON_GREEN, (checkbox_x + 12, checkbox_y + 22), 
                               (checkbox_x + 25, checkbox_y + 8), 3)
            
            # Task title
            title_color = LIGHT_GRAY if not task.completed else COMPLETED_COLOR
            title_text = normal_font.render(task.title, True, title_color)
            surface.blit(title_text, (task_x + 60, task_y + 10))
            
            # Priority and date
            info_text = f"Priority: {task.priority.upper()} | Created: {task.created_at[:10]}"
            if task.due_date:
                info_text += f" | Due: {task.due_date}"
            
            info_surf = tiny_font.render(info_text, True, DARK_GRAY)
            surface.blit(info_surf, (task_x + 60, task_y + 38))
            
            # Delete button
            delete_x = task_x + task_width - 40
            delete_y = task_y + 15
            delete_size = 30
            pygame.draw.rect(surface, NEON_RED, (delete_x, delete_y, delete_size, delete_size), 2, border_radius=5)
            delete_text = small_font.render("✕", True, NEON_RED)
            delete_rect = delete_text.get_rect(center=(delete_x + delete_size // 2, delete_y + delete_size // 2))
            surface.blit(delete_text, delete_rect)
            
            task_y += task_height + task_spacing
    
    def draw_instructions(self, surface):
        """Draw instructions"""
        instructions = [
            "💡 Click on a task to complete it | Click the ✕ to delete | Type in the input box and press ENTER to add a task"
        ]
        
        instr_y = SCREEN_HEIGHT - 50
        for instr in instructions:
            instr_text = tiny_font.render(instr, True, DARK_GRAY)
            surface.blit(instr_text, (50, instr_y))
            instr_y += 25
    
    def handle_click(self, pos):
        """Handle mouse clicks"""
        x, y = pos
        
        # Filter buttons
        button_y = 200
        button_height = 35
        button_width = 100
        spacing = 15
        
        filters = ["all", "active", "completed"]
        filter_x = 50
        
        for i, filter_name in enumerate(filters):
            bx = filter_x + i * (button_width + spacing)
            if bx <= x <= bx + button_width and button_y <= y <= button_y + button_height:
                self.filter_mode = filter_name
                return
        
        # Sort buttons
        sorts = ["date", "priority"]
        sort_names = ["By Date", "By Priority"]
        sort_x = 50 + 400
        
        for i, sort_name in enumerate(sorts):
            bx = sort_x + i * (button_width + spacing)
            if bx <= x <= bx + button_width and button_y <= y <= button_y + button_height:
                self.sort_mode = sort_name
                return
        
        # Task interactions
        tasks = self.get_sorted_tasks()
        task_y = 260
        task_height = 70
        task_spacing = 15
        
        for i, task in enumerate(tasks[:9]):
            task_x = 50
            task_width = SCREEN_WIDTH - 100
            
            if task_x <= x <= task_x + task_width and task_y <= y <= task_y + task_height:
                # Check if clicking checkbox
                checkbox_x = task_x + 15
                checkbox_y = task_y + 15
                checkbox_size = 30
                
                if checkbox_x <= x <= checkbox_x + checkbox_size and checkbox_y <= y <= checkbox_y + checkbox_size:
                    self.toggle_task(task.id)
                    return
                
                # Check if clicking delete button
                delete_x = task_x + task_width - 40
                delete_y = task_y + 15
                delete_size = 30
                
                if delete_x <= x <= delete_x + delete_size and delete_y <= y <= delete_y + delete_size:
                    self.delete_task(task.id)
                    return
                
                return
            
            task_y += task_height + task_spacing
        
        # Input box
        input_y = 130
        input_height = 50
        input_width = SCREEN_WIDTH - 100
        input_x = 50
        
        if input_x <= x <= input_x + input_width and input_y <= y <= input_y + input_height:
            self.input_active = True
        else:
            self.input_active = False
    
    def handle_key_press(self, key):
        """Handle keyboard input"""
        if not self.input_active:
            return
        
        if key == pygame.K_RETURN:
            self.add_task(self.input_text)
            self.input_text = ""
        elif key == pygame.K_BACKSPACE:
            self.input_text = self.input_text[:-1]
    
    def handle_text_input(self, text):
        """Handle text input"""
        if self.input_active:
            self.input_text += text
    
    def draw(self, surface):
        """Draw everything"""
        surface.fill(DARK_BG)
        self.draw_header(surface)
        self.draw_input_section(surface)
        self.draw_filter_buttons(surface)
        self.draw_tasks(surface)
        self.draw_instructions(surface)

# Create app
app = TodoApp()

# Main loop
running = True

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            app.handle_click(event.pos)
        elif event.type == pygame.KEYDOWN:
            app.handle_key_press(event.key)
        elif event.type == pygame.TEXTINPUT:
            app.handle_text_input(event.text)
    
    app.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
