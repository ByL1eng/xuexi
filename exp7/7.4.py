from math import sqrt


class Vector:
    def __init__(self, vector):
        self.new_list = vector

    def __str__(self):
        s = ",".join([str(element) for element in self.new_list])
        return '(%s)' % s

    def equals(self, vector):
        if self.__str__() == vector.__str__():
            return True
        else:
            return False

    def compare(self, vector):
        if len(self.new_list) == len(vector.new_list):
            return True
        else:
            return False

    def norm(self):
        return sqrt(self.new_list[0] ** 2 + self.new_list[1] ** 2 + self.new_list[2] ** 2)

    def add(self, Object):
        if self.compare(Object):
            new_vector = Vector
            new_list = []
            for i in range(len(self.new_list)):
                new_list.append(self.new_list[i] + Object.new_list[i])
            return new_vector(new_list)
        else:
            return 'raises an exception'

    def subtract(self, vector):
        if self.compare(vector):
            new_vector = Vector
            new_list = []
            for i in range(len(self.new_list)):
                new_list.append(self.new_list[i] - vector.new_list[i])
            return new_vector(new_list)
        else:
            return 'raises an exception'

    def dot(self, vector):
        if self.compare(vector):
            sum_number = 0
            for i in range(len(self.new_list)):
                sum_number += (self.new_list[i] * vector.new_list[i])

            return sum_number
        else:
            return 'raises an exception'