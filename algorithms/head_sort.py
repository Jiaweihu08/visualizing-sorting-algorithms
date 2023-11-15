from collections.abc import Callable
from collections import deque
from .utils import empty_draw


def heap_sort(A: list[int], draw: Callable[[list[int], int, float], None] = empty_draw) -> list[int]:
    heap = MinHeap(A)
    result = []
    for _ in range(len(A)):
        result.append(heap.pop())
        draw(result + heap.to_list(), -1, 0.05)
    return result


class MinHeap:
    def __init__(self, A: list[int]) -> None:
        self.arr = deque(A)
        self._build()

    def _build(self) -> None:
        for idx in reversed(range(self.size() // 2)):
            self._sift_down(idx)

    def pop(self) -> int:
        if len(self.arr) == 0:
            raise IndexError("pop from an empty heap")
        value = self.arr[0]
        self._swap(0, -1)
        self.arr.pop()
        if not self.is_empty():
            self._sift_down(0)
        return value

    def _sift_down(self, idx: int) -> None:
        l_idx = idx * 2 + 1
        if l_idx < self.size() and self.arr[l_idx] < self.arr[idx]:
            self._swap(idx, l_idx)

        r_idx = idx * 2 + 2
        if r_idx < self.size() and self.arr[r_idx] < self.arr[idx]:
            self._swap(idx, r_idx)
            if self._has_child(r_idx):
                self._sift_down(r_idx)

        if self._has_child(l_idx):
            self._sift_down(l_idx)

    def _swap(self, i: int, j: int) -> None:
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def _has_child(self, idx: int) -> bool:
        return idx <= self.size() // 2 - 1

    def size(self):
        return len(self.arr)

    def is_empty(self) -> bool:
        return self.size() == 0

    def to_list(self):
        return list(self.arr)

    # def append(self, value: int) -> None:
    #     self.arr.append(value)
    #     self._sift_up(self.size() - 1)

    # def _sift_up(self, idx: int) -> None:
    #     if idx > 0:
    #         parent_idx = (idx - 1) // 2
    #         if self.arr[idx] > self.arr[parent_idx]:
    #             self._swap(idx, parent_idx)
    #             self._sift_up(parent_idx)


if __name__ == '__main__':
    from random import randint

    nums = [randint(0, 50) for _ in range(10)]
    sorted_nums = heap_sort(nums)
    assert(sorted_nums == sorted(nums))
