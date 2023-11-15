from collections.abc import Callable
from .utils import empty_draw


def merge_sort(A: list[int], left: int, right: int, draw: Callable[[list[int], int, float], None] = empty_draw) -> None:
    if right - left <= 1:
        return

    middle = left + (right - left) // 2
    merge_sort(A, left, middle, draw)
    merge_sort(A, middle, right, draw)
    merge(A, left, middle, right, draw)


def merge(A: list[int], left: int, middle: int, right: int,
          draw: Callable[[list[int], int, float], None] = empty_draw) -> None:
    left_arr, right_arr = A[left:middle], A[middle:right]
    l, r, idx = 0, 0, left
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            A[idx] = left_arr[l]
            l += 1
        else:
            A[idx] = right_arr[r]
            r += 1
        idx += 1
        draw(A[:idx] + left_arr[l:] + right_arr[r:] + A[right:], idx, 0.05)

    while l < len(left_arr):
        A[idx] = left_arr[l]
        l, idx = l + 1, idx + 1
        draw(A[:idx] + left_arr[l:] + right_arr[r:] + A[right:], idx, 0.05)

    while r < len(right_arr):
        A[idx] = right_arr[r]
        r, idx = r + 1, idx + 1
        draw(A[:idx] + left_arr[l:] + right_arr[r:] + A[right:], idx, 0.05)


if __name__ == '__main__':
    from random import randint

    nums = [randint(0, 50) for _ in range(10)]
    nums_copy = nums.copy()
    merge_sort(nums, 0, len(nums))
    assert (nums == sorted(nums_copy))
