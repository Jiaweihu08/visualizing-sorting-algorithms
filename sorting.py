import sys
from random import shuffle
from time import sleep

import pygame

from algorithms.quick_sort import *

WIDTH = 800
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (128, 128, 128)


def draw(A: list[int], idx: int = -1, duration: float = 0.0) -> None:
	screen.fill(WHITE)
	count = 4
	# Draw a vertical line for each individual number
	# with p1 at the bottom, and p2 at the top.
	# The coordinate (0, 0) corresponds to the top left corner
	# of the pygame window.
	for i, num in enumerate(A):
		count += 4
		p1 = (20 + i + count, HEIGHT)
		p2 = (20 + i + count, HEIGHT - num)
		color = RED if i == idx else GREY
		pygame.draw.line(screen, color, p1, p2, 4)
	pygame.display.update()
	if duration != 0.0:
		sleep(duration)


def get_lists_to_sort() -> list[list[int]]:
	# ints with replicates
	with_replicates = [i * 30 for i in range(15) for _ in range(10)]
	shuffle(with_replicates)

	# random ints
	random_ints = [i * 3 for i in range(150)]
	shuffle(random_ints)

	# reversely sorted ints
	reversed_int = [i * 3 for i in reversed(range(150))]

	return [with_replicates, random_ints, reversed_int]


def main():
	list_of_lists = get_lists_to_sort()

	while True:
		draw(list_of_lists[0])
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					for list_of_ints in list_of_lists:
						draw(list_of_ints)
						sleep(0.5)
						quick_sort(list_of_ints, 0, len(list_of_ints), draw)
						# heap_sort(list_of_ints, draw)
						# merge_sort(list_of_ints, 0, len(list_of_ints), draw)
						# bubble_sort(list_of_ints, draw)
						sleep(1)

					list_of_lists = get_lists_to_sort()

				if event.key == pygame.K_c:
					list_of_lists = get_lists_to_sort()


if __name__ == '__main__':
	main()
