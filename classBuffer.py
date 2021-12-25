class Buffer:

    def __init__(self):
        self.input_number = []

    def add(self, *a):
        self.input_number.extend(a)                # add elements
        while len(self.input_number) - 5 >= 0:
            print(sum(self.input_number[0:5]))     # sum first five elements
            self.input_number = self.input_number[5:]    # remaining elements

    def get_current_part(self):
        return self.input_number        # return the remaining elements


buffer = Buffer()
buffer.add(1, 6, 9)
buffer.get_current_part()                       # вернуть [элементы списка]
buffer.add(4, 5, 6, 8, 2, 10)                   # вывод суммы первой пятерки элементов
buffer.get_current_part()                       # вернуть [оставшиеся элементы]
buffer.add(7, 11, 9, 12)                        # вывод суммы второй пятерки элементов
buffer.get_current_part()                       # вернуть [оставшиеся элементы]
buffer.add(14, 16, 21, 17)                      # вывод сумм третьей пятерки
buffer.get_current_part()                       # вернуть [оставшиеся элементы]
print('The remaining elements: ', buffer.input_number)
