#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size=0):
        self.brand = brand
        self.size = size

    def get_size(self):
        return self._size
    
    def set_size(self, num):
        if type(num) == int:
            self._size = num 
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    size = property(get_size, set_size)