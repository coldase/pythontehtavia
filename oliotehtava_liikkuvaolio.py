import pygame
from time import sleep

pygame.init()

screen_width = 400
screen_height = 400
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("OLIOTEHTAVA")


RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
FPS = 60

class Olio:
	def __init__(self, player_color, start_point):
		self.player_color = player_color
		self.name = "Jarmo"
		self.speed = 3
		self.pos_x = start_point[0]
		self.pos_y = start_point[1]
		self.size = 20
		self.rects = self.buttons()
		self.button_color = WHITE

	def draw(self):
		pygame.draw.circle(screen, self.player_color,(self.pos_x, self.pos_y),self.size)
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


	def move_with_keys(self, player):
		keys = pygame.key.get_pressed()
		if player == 1:
			if keys[pygame.K_w] and self.pos_y > self.size:
				self.pos_y -= self.speed
				self.draw_nose("up")
			if keys[pygame.K_s] and self.pos_y < screen_width - self.size:
				self.pos_y += self.speed
				self.draw_nose("down")
			if keys[pygame.K_a] and self.pos_x > self.size:
				self.pos_x -= self.speed
				self.draw_nose("left")
			if keys[pygame.K_d] and self.pos_x < screen_width - self.size:
				self.pos_x += self.speed
				self.draw_nose("right")
			
		if player == 2:
			if keys[pygame.K_UP] and self.pos_y > self.size:
				self.pos_y -= self.speed
				self.draw_nose("up")
			if keys[pygame.K_DOWN] and self.pos_y < screen_width - self.size:
				self.pos_y += self.speed
				self.draw_nose("down")
			if keys[pygame.K_LEFT] and self.pos_x > self.size:
				self.pos_x -= self.speed
				self.draw_nose("left")
			if keys[pygame.K_RIGHT] and self.pos_x < screen_width - self.size:
				self.pos_x += self.speed
				self.draw_nose("right")


	def buttons(self, button_color=WHITE):
		up = pygame.draw.circle(screen, button_color,(70, 300),10)
		down = pygame.draw.circle(screen, button_color,(70, 350),10)
		left = pygame.draw.circle(screen, button_color,(45, 325),10)
		right = pygame.draw.circle(screen, button_color,(95, 325),10)
		
		koil = pygame.draw.circle(screen, button_color,(90, 305),7)
		kaak = pygame.draw.circle(screen, button_color,(90, 345),7)
		loun = pygame.draw.circle(screen, button_color,(50, 345),7)
		luod = pygame.draw.circle(screen, button_color,(50, 305),7)
		
		return up, down, left, right, koil, kaak, loun, luod

	def draw_nose(self, direction):
		if direction == "up":
			pygame.draw.circle(screen, self.player_color, (self.pos_x, self.pos_y - self.size), 10)
		elif direction == "down":
			pygame.draw.circle(screen, self.player_color, (self.pos_x , self.pos_y + self.size), 10)
		elif direction == "left":
			pygame.draw.circle(screen, self.player_color, (self.pos_x - self.size, self.pos_y), 10)
		elif direction == "right":
			pygame.draw.circle(screen, self.player_color, (self.pos_x + self.size, self.pos_y), 10)

ball = Olio(RED, (50,50))
ball_2 = Olio(GREEN, (350,350))
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
	ball.move_with_keys(1)
	ball_2.draw()
	ball_2.move()
	ball_2.move_with_keys(2)
	pygame.display.flip()

pygame.quit()