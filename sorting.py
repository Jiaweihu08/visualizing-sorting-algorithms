import pygame, sys
from random import randint, shuffle
from time import sleep


WIDTH = 800
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (128, 128, 128)


# -------------------------- Quick Sort
def quick_sort(A, l, r):
	if l >= r:
		return
	
	k = randint(l, r - 1)
	A[l], A[k] = A[k], A[l]
	
	m1, m2 = partition_3(A, l, r)
	quick_sort(A, l, m1)
	quick_sort(A, m2, r)


def partition_3(A, l, r):
	pivot = A[l]
	j = l
	count = 1
	for i in range(l+1, r):
		if A[i] < pivot:
			j += 1
			A[i], A[j] = A[j], A[i]
			draw(A, i, 0.05)
		elif A[i] == pivot:
			count += 1

	A[j], A[l] = A[l], A[j]
	draw(A, j, 0.05)
	return j, j + count


# -------------------------- Merge Sort
def merge_sort(A, l, r):
	if len(A[l:r]) == 1:
		return A[l:r]

	m = (l + r + 1) // 2

	A[l:m] = merge_sort(A, l, m)
	A[m:r] = merge_sort(A, m, r)

	return merge(A, l, m, r)


def merge(A, l, m, r):
	arr_l = A[l:m]
	arr_r = A[m:r]
	result = []

	while arr_l and arr_r:
		if arr_l[0] < arr_r[0]:
			result.append(arr_l.pop(0))
			idx = l
		else:
			result.append(arr_r.pop(0))
			idx = l + len(arr_l)
			
		draw(A[:l]+arr_l+arr_r+result+A[r:], idx, 0.05)

	while arr_l:
		result.append(arr_l.pop(0))
		draw(A[:l]+arr_l+result+A[r:], 0.05)
	
	while arr_r:
		result.append(arr_r.pop(0))
		draw(A[:l]+arr_r+result+A[r:], 0.05)

	return result


# -------------------------- Bubble Sort
def bubble_sort(A):
	for i in range(len(A)):
		for j in range(len(A) - i - 1):
			if A[j] > A[j + 1]:
				A[j], A[j + 1] = A[j + 1], A[j]
				draw(A)


# -------------------------- Heap Sort
def heap_sort(A):
	build_heap(A)

	result = []
	for _ in range(len(A)):
		A[0], A[-1] = A[-1], A[0]
		result.append(A.pop())
		if A:
			sift_down(A, 0)
		
		draw(A+result, -1, 0.05)
	return result


def build_heap(A):
	for i in reversed(range(len(A) // 2)):
		sift_down(A, i)


def sift_down(A, i):
	curr = A[i]

	l = i * 2 + 1
	if l < len(A) and A[l] < A[i]:
		A[l], A[i] = A[i], A[l]

	r = i * 2 + 2
	if r < len(A) and A[r] < A[i]:
		A[r], A[i] = A[i], A[r]
		if has_child(A, r):
			sift_down(A, r)

	if has_child(A, l):
		sift_down(A, l)


def has_child(A, i):
	return i <= len(A) // 2 - 1
	

# --------------------------
def draw(A, idx=-1, speed=0):
	screen.fill(WHITE)
	count = 4
	for i, val in enumerate(A):
		count += 4
		p1 = (20 + i + count, HEIGHT)
		p2 = (20 + i + count, HEIGHT - val)
		color = RED if i == idx else GREY
		pygame.draw.line(screen, color, p1, p2, 4)
	pygame.display.update()
	if speed != 0:
		sleep(speed)


def get_vals():
	A = [i * 3 for i in range(150)]
	shuffle(A)
	B = [i * 3 for i in reversed(range(150))]
	return [A, B]


# --------------------------
def main():
	vals = get_vals()

	while True:
		draw(vals[0])
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					for arr in vals:
						draw(arr)
						sleep(0.5)
						# quick_sort(arr, 0, len(arr))
						# heap_sort(arr)
						# merge_sort(arr, 0, len(arr))
						bubble_sort(arr)
						sleep(1)

					vals = get_vals()

				if event.key == pygame.K_c:
					vals = get_vals()



if __name__ == '__main__':
	main()





