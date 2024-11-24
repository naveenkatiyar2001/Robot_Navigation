import pygame
import math

# Robot class with Pygame integration
class Robot:
    def __init__(self, x, y, direction):
        self.x = x  # Robot's initial x-position
        self.y = y  # Robot's initial y-position
        self.direction = direction  # Direction of movement (angle in degrees)
        self.speed = 1  # Movement speed in grid units
        self.radius = 10  # Radius for display purposes in Pygame

    def move_forward(self):
        # Move the robot forward by updating its x and y position
        self.x += math.cos(math.radians(self.direction)) * self.speed
        self.y += math.sin(math.radians(self.direction)) * self.speed

    def turn_left(self, angle=90):
        # Turn the robot left by adjusting its direction
        self.direction = (self.direction - angle) % 360

    def turn_right(self, angle=90):
        # Turn the robot right by adjusting its direction
        self.direction = (self.direction + angle) % 360

    def draw(self, screen):
        # Draw the robot on the Pygame screen as a circle
        pygame.draw.circle(screen, (128, 255, 128), (int(self.x), int(self.y)), self.radius)

    def zigzag_move(self, screen, zigzag_count):
        # Implement a zigzag movement by alternating between moving forward and turning
        for _ in range(zigzag_count):
            self.move_forward()
            self.draw(screen)
            pygame.display.update()
            pygame.time.wait(100)
            self.turn_left(45)
            self.move_forward()
            self.draw(screen)
            pygame.display.update()
            pygame.time.wait(100)
            self.turn_right(45)