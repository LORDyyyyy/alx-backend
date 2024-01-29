#!/usr/bin/env python3
""" doc """
import csv
import math
from typing import List, Tuple


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
        """ doc """
        assert isinstance(page, int) and page > 0, "Page must be an integer\
            greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "Page size must\
            be an integer greater than 0"

        index = Server.index_range(page, page_size)

        if index[1] > len(self.dataset()) or index[0] > len(self.dataset()):
            return []
        return self.dataset()[index[0]:index[1]]

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
            Return a tuple of size two containing a start index and an
            end index corresponding to the range of indexes to return in
            a list for those particular pagination parameters.
        """

        return ((page - 1) * page_size, page * page_size)
