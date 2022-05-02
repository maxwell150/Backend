#!/usr/bin/env python3
"""function takes two integer args and return a tuple of size containing
a start index and end index correspnding to range of indexes"""


def index_range(page: int, page_size: int) -> tuple:
    """helper function"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
