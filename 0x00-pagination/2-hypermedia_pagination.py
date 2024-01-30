#!/usr/bin/env python3
''' Hypermedia pagination '''

import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    ''' index range '''
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

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
        ''' get page '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)

        if start > len(data):
            return []

        return data[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        ''' get hyper '''

        data = self.get_page(page, page_size)

        next_page = None
        start, end = index_range(page, page_size)
        if end < len(self.__dataset):
            next_page = page + 1

        prev_page = None
        if start > 0:
            prev_page = page - 1

        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
