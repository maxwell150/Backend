#!/usr/bin/env python3
"""simple pagination"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get items"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(self.dataset()):
            return []
        return self.dataset()[start_index : end_index]

def index_range(page: int, page_size: int) -> tuple:
    """helper function"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


