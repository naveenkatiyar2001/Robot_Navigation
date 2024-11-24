import pygame
import random
from robot import Robot
from obstacle_detection import detect_obstacle
from pathfinding import astar_search


#Initiallize Pygame
pygame.init()

#set up the display window
screen_width, screen_height = 1200, 1200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Robot Navigation in Warehouse")

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Obstacle coordinats based on question
obstacles = [ (100,100), (300, 100), (500, 100), (700, 100), (900, 100), (100, 300), (300, 300), 
             (500, 300), (700, 300), (900, 300),]

#Create a warehouse system
warehouse_size = 50



#function to draw the warehosue_grid
def draw_warehouse():
    for x in range (0, screen_width, warehouse_size):
        for y in range(0, screen_height, warehouse_size):
            rect = pygame.Rect(x, y, warehouse_size, warehouse_size)
            pygame.draw.rect(screen, WHITE, rect, 1)

#Function to draw obstacles on the grid
def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, (*obstacle, warehouse_size, warehouse_size))  


#Main simulation loop
def main():
    running = True
    robot = Robot(0, 0, 0) #Initialize robot at 0,0 facing right
    start = (robot.x, robot.y)
    goal = (1100, 1100)


# Run A* to find path from start to goal 
    warehouse = [[0 for _ in range(screen_width // warehouse_size)] for _ in range(screen_height // warehouse_size)]
     
    for (ox, oy) in obstacles:
        grid_x = int(oy / warehouse_size)
        grid_y = int(ox / warehouse_size)

        if 0 <= grid_x <len(warehouse) and 0 <= grid_y < len(warehouse[0]):
            warehouse[grid_x][grid_y] = 1
        else:
            print(f"Obstacle at {(ox, oy)} is out of grid bounds.")    

    path = astar_search(start, goal, warehouse) 

    while running:
        screen.fill(WHITE)
        draw_warehouse()
        draw_obstacles()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# Move the robot along the path calculated by A*
        if path:
            for position in path:
                robot.x, robot.y = position
                if detect_obstacle(robot.x, robot.y, obstacles):
                    print("Obstacle detected")
                    robot.turn.left(45)
            
                robot.draw(screen)
                pygame.display.update()
                pygame.time.wait(100)
        else:
            print("No path found!")     

            #Update display
        pygame.display.update()   
        pygame.time.Clock().tick(30)
    pygame.quit()    

if __name__ == "__main__":
    main()
