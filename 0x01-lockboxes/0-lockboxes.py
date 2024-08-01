#!/usr/bin/python3
"""Lockboxes module"""


def check(keys, l):
    """Checks if all the box indexes have been obtained."""
    for i in range(l):
        if keys[i] != 1:
            return 0
    return (1)


def helper(boxes, index, keys):
    """Helper function"""
    ret = 0
    for i in boxes[index]:
        if i < len(boxes):
            if keys[i] == 0:
                keys[i] = 1
                ret = helper(boxes, i, keys)
                ret = check(keys, len(boxes))
    return (ret)


def canUnlockAll(boxes):
    """ Determines if all boxes of a box list can be opened."""
    keys = [0] * len(boxes)
    for i in range(len(boxes)):
        keys[i] = 0
    ret = 0
    if len(boxes):
        keys[0] = 1
    else:
        return (True)
    for i in boxes[0]:
        if i < len(boxes):
            if keys[i] == 0:
                keys[i] = 1
                ret = helper(boxes, i, keys)
                ret = check(keys, len(boxes))
    if ret == 1 or len(boxes) == 1:
        return (True)
    else:
        return (False)
