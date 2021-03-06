import sys
import pygame

from bullet import Bullet


def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	if event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	if event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False

def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)


def check_events(ai_settings, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

def update_bullets(bullets):
	bullets.update()

	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)


def update_screen(ai_settings, screen, ship, ai_ycy, bullets):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	ai_ycy.blitme()
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	pygame.display.flip()

