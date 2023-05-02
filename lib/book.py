#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count=0):
        self.title = title
        self.page_count = page_count

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, num):    
        if isinstance(num, int):
            self._page_count = num
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    page_count = property(get_page_count, set_page_count)

towers = Book("Towering Inferno", 417)
towers.genre = "Non-fiction"
print(towers.genre)
print(towers.page_count)
print(towers.title)