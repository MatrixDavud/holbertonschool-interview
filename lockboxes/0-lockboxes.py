#!/usr/bin/python3
"""Problem 0."""


def canUnlockAll(boxes):
    """Boxes is a list of lists.

    each box contains keys to other boxes, or it may have no key.
    If we can unlock all the boxes return True, False otherwise.
    """
    n = len(boxes)
    answer = True
    for i in range(1, n):
        flag = 0
        for j in range(n):
            if i in boxes[j] and j != i:
                flag = 1
                break
        if flag == 0:
            answer = False
    return answer
