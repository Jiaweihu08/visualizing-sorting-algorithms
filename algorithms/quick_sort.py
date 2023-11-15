from collections.abc import Callable
from .utils import empty_draw


def quick_sort(
		A: list[int], left: int, right: int,
		draw: Callable[[list[int], int, float], None] = empty_draw) -> None:
	if left >= right:
		return

	smaller, equal = partition_3(A, left, right, draw)
	quick_sort(A, left, smaller, draw)
	quick_sort(A, equal, right, draw)


def partition_3(
		A: list[int], left: int, right: int,
		draw: Callable[[list[int], int, float], None] = empty_draw) -> (int, int):
	pivot = A[left]
	# Keep the following invariants during partitioning:
	# bottom group: A[:smaller].
	# middle group: A[smaller:equal].
	# unclassified group: A[equal:larger].
	# top group: A[larger:].
	smaller, equal, larger = left, left, right
	# Keep iterating as long as there is an unclassified element.
	while equal < larger:
		# A[equal] is the incoming unclassified element.
		if A[equal] < pivot:
			A[smaller], A[equal] = A[equal], A[smaller]
			smaller, equal = smaller + 1, equal + 1
			draw(A, equal, 0.05)
		elif A[equal] == pivot:
			equal += 1
		else:  # A[equal] > pivot
			larger -= 1
			A[equal], A[larger] = A[larger], A[equal]
			draw(A, equal, 0.05)
	draw(A, equal, 0.05)
	return smaller, equal


# def partition_2(
# 		A: list[int], left: int, right: int,
# 		draw: Callable[[list[int], int, float], None]) -> int:
# 	"""slow for input sequences with a large number of duplicates."""
# 	pivot = A[left]
# 	i = left
# 	for j in range(left + 1, right):
# 		if A[j] < pivot:
# 			i += 1
# 			A[i], A[j] = A[j], A[i]
# 			draw(A, j, 0.05)
#
# 	A[left], A[i] = A[i], A[left]
# 	draw(A, i, 0.05)
# 	return i


if __name__ == '__main__':
	from random import randint

	nums = [randint(0, 50) for _ in range(10)]
	nums_copy = nums.copy()
	quick_sort(nums, 0, len(nums))
	assert (nums == sorted(nums_copy))
