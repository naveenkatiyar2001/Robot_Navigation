def detect_obstacle(x, y, obstacles):
    detection_radius = 20 
    #Simulate obstacle detection within 0.2m radius
    for (ox, oy) in obstacles:
        if abs(x-ox) < detection_radius and abs(y - oy) < detection_radius:
            return True
    return False    