import pygame
import math


pygame.init()


WIDTH, HEIGHT = 800, 770


PLANET = pygame.transform.scale(pygame.image.load("jupiter.png"), (50 * 2, 50 * 2))
BACKGROUND = pygame.transform.scale(pygame.image.load("space.jpg"), (WIDTH, HEIGHT))


PLANET_MASS = 100
SPACE_CRAFT_MASS = 5
G = 5
OBJECT_SIZE = 5
VELOCITY = 100
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
RED = (2, 239, 247)
BLUE = (0, 0, 255)


pygame.display.set_caption("Gravitation")


class planet:
  def __init__(self, x, y, mass):
    self.x = x
    self.y = y
    self.mass = mass
    
  def draw(self):
    WIN.blit(PLANET, (self.x - 50, self.y - 50))


class spacecraft:
  def __init__(self, x, y, vel_x, vel_y, mass):
    
    self.x = x
    self.y = y
    self.vel_x = vel_x
    self.vel_y = vel_y
    self.mass = mass
  
  def move(self, planet = None):
    
    distance = math.sqrt((self.x - planet.x)**2 + (self.y - planet.y)**2)
    force = (G * self.mass * planet.mass) / distance ** 2
    acceleration = force / self.mass
    angle = math.atan2(planet.y - self.y, planet.x - self.x )
    
    acceleration_x = acceleration * math.cos(angle)
    acceleration_y = acceleration * math.sin(angle)
    
    self.vel_x += acceleration_x
    self.vel_y += acceleration_y
    
    self.x += self.vel_x
    self.y += self.vel_y
    
  def draw(self):
    pygame.draw.circle(WIN, RED, (int(self.x), int(self.y)), OBJECT_SIZE)


def create_ship(Location, mouse):
  t_x, t_y = Location
  m_x, m_y = mouse
  vel_x = (m_x - t_x) / 100
  vel_y = (m_y - t_y) / 100
  
  obj = spacecraft(t_x, t_y, vel_x, vel_y, SPACE_CRAFT_MASS)
  return obj


def main():
  objects = []
  
  temp_obj_pos = None
  
  clock = pygame.time.Clock()
    
  running = True
  
  Planet = planet(WIDTH // 2, HEIGHT // 2, PLANET_MASS)
  
  while running:
    
    mouse_pos = pygame.mouse.get_pos()
    clock.tick(FPS)
    
    for event in pygame.event.get():
      
      if event.type == pygame.QUIT:
        running = False
        
      if event.type == pygame.MOUSEBUTTONDOWN:
        
        if temp_obj_pos:
          
          obj = create_ship(temp_obj_pos, mouse_pos)
          objects.append(obj)
          temp_obj_pos = None
          
        else:
           temp_obj_pos = mouse_pos
    
    WIN.blit(BACKGROUND, (0, 0))
    
    if temp_obj_pos:
      pygame.draw.line(WIN, WHITE, temp_obj_pos, mouse_pos, 2)
      pygame.draw.circle(WIN, RED, temp_obj_pos, OBJECT_SIZE)
      
    for obj in objects[:]:
      obj.draw()
      obj.move(Planet)  
      off_screen = obj.x < 0 or obj.x > WIDTH or obj.y < 0 or obj.y > HEIGHT
      collided = math.sqrt((obj.x - Planet.x) ** 2 + (obj.y - Planet.y) ** 2) <= 50
      
      if off_screen or collided:
        objects.remove(obj)
      
    
    Planet.draw()
       
    pygame.display.update()
  
  pygame.quit()   
    
  
    
if __name__ == "__main__":
  main()
        



    
    

    
    


