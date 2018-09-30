class Array():
    def __init__(self, int_max_size):
        self.array = [None] * int_max_size
        self.size = int_max_size

    def append(self, value):
        int_i = 0
        ith_value = self.array[int_i]
        while ith_value != None:
            int_i += 1
            ith_value = self.array[int_i]
        self.array[int_i] = value

    def pop_index(self, index):
        current_index = index
        next_index = index + 1
        while next_index < self.size and self.array[next_index] != None:
            self.array[current_index] = self.array[next_index]
            current_index += 1
            next_index += 1
        self.array[current_index] = None

    def pop_last(self):
        current_index = 0
        while current_index < self.size and self.array[current_index] != None:
            current_index += 1
        self.pop_index(current_index - 1)

    def remove(self, value):
        bool_found = False
        int_i = 0
        while not bool_found:
            if self.array[int_i] == value:
                self.pop_index(int_i)
                bool_found = True
            int_i += 1

    def insert(self, int_index, value):
        int_i = 0
        while self.array[int_i] != None:
            int_i += 1
        while int_i > int_index:
            self.array[int_i] = self.array[int_i - 1]
            int_i -= 1
        self.array[int_i] = value

    def count(self, value):
        counter = 0
        int_i = 0
        while int_i < self.size and self.array[int_i] != None:
            if self.array[int_i] == value:
                counter += 1
            int_i += 1
        return counter

    def reverse(self):
        int_i = 0
        new_array = Array(self.size)
        while int_i < self.size and self.array[int_i] != None:
            int_i += 1
        int_i -= 1
        while int_i >= 0:
            new_array.append(self.array[int_i])
            int_i -= 1
        self.array = new_array.array

    def sort(self):
        sorted = Array(self.size)
        int_i = 0
        while int_i < self.size and self.array[int_i] != None:
            value = self.array[int_i]
            int_j = 0
            sorted_value = sorted.array[int_j]
            while int_j < sorted.size and sorted_value != None and sorted_value < value:
                int_j += 1
                sorted_value = sorted.array[int_j]
            if sorted_value == None:
                sorted.append(value)
            else:
                sorted.insert(int_j, value)
            int_i += 1
        self.array = sorted.array
