from collections.abc import Callable
from .utils import empty_draw


def bubble_sort(A: list[int], draw: Callable[[list[int], int, float], None] = empty_draw) -> None:
	for i in range(len(A)):
		for j in range(len(A) - i - 1):
			if A[j] > A[j + 1]:
				A[j], A[j + 1] = A[j + 1], A[j]
				draw(A, -1, 0.0)


if __name__ == '__main__':
	from random import randint

	nums = [randint(0, 50) for _ in range(10)]
	nums_copy = nums.copy()
	bubble_sort(nums)
	assert (nums == sorted(nums_copy))
