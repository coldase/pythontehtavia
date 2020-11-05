import pygame

pygame.init()

screen_width = 400
screen_height = 400
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)

RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

FPS = 60

class Olio:
	def __init__(self):
		self.name = "Jarmo"
		self.speed = 3
		self.pos_x = 200
		self.pos_y = 200
		self.size = 20
		self.rects = self.buttons()

	def draw(self):
		pygame.draw.circle(screen, RED,(self.pos_x, self.pos_y),self.size)
		self.buttons()

	def move(self):
		
		key = pygame.mouse.get_pressed()
		pos = pygame.mouse.get_pos()

		if key[0] and self.rects[0].collidepoint(pos) and self.pos_y > self.size:
			self.pos_y -= self.speed
		if key[0] and self.rects[1].collidepoint(pos) and self.pos_y < screen_width - self.size:
			self.pos_y += self.speed
		if key[0] and self.rects[2].collidepoint(pos) and self.pos_x > self.size:
			self.pos_x -= self.speed
		if key[0] and self.rects[3].collidepoint(pos) and self.pos_x < screen_width - self.size:
			self.pos_x += self.speed
		if key[0] and self.rects[4].collidepoint(pos) and self.pos_y > self.size and self.pos_x < screen_width - self.size:
			self.pos_x += self.speed
			self.pos_y -= self.speed
		if key[0] and self.rects[5].collidepoint(pos) and self.pos_y < screen_width - self.size and self.pos_x < screen_width - self.size:
			self.pos_x += self.speed
			self.pos_y += self.speed
		if key[0] and self.rects[6].collidepoint(pos) and self.pos_y < screen_width - self.size and self.pos_x > self.size:
			self.pos_x -= self.speed
			self.pos_y += self.speed
		if key[0] and self.rects[7].collidepoint(pos) and self.pos_y > self.size and self.pos_x > self.size:
			self.pos_x -= self.speed
			self.pos_y -= self.speed

	def buttons(self):
		up = pygame.draw.circle(screen, WHITE,(70, 300),10)
		down = pygame.draw.circle(screen, WHITE,(70, 350),10)
		left = pygame.draw.circle(screen, WHITE,(45, 325),10)
		right = pygame.draw.circle(screen, WHITE,(95, 325),10)
		
		koil = pygame.draw.circle(screen, WHITE,(90, 305),7)
		kaak = pygame.draw.circle(screen, WHITE,(90, 345),7)
		loun = pygame.draw.circle(screen, WHITE,(50, 345),7)
		luod = pygame.draw.circle(screen, WHITE,(50, 305),7)
		
		return up, down, left, right, koil, kaak, loun, luod


ball = Olio()
clock = pygame.time.Clock()

run = True
while run:
	clock.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	screen.fill(BLACK)
	ball.draw()
	ball.move()
	pygame.display.flip()

pygame.quit()