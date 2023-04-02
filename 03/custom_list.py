class CustomList(list):
    def __init__(self, lst):
        super().__init__()
        self.lst = lst

    @staticmethod
    def normalize_len(lst1, lst2):
        difference = len(lst1) - len(lst2)
        if difference > 0:
            lst2 += [0] * difference
        elif difference < 0:
            lst1 += [0] * -difference
        return lst1, lst2

    def __add__(self, other):
        other_lst = other if not isinstance(other, CustomList) else other.lst
        lst, other_lst = self.normalize_len(self.lst, other_lst)
        result = [v + other_lst[i] for i, v in enumerate(lst)]
        return CustomList(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other_lst = other if not isinstance(other, CustomList) else other.lst
        lst, other_lst = self.normalize_len(self.lst, other_lst)
        result = [v - other_lst[i] for i, v in enumerate(lst)]
        return CustomList(result)

    def __rsub__(self, other):
        other_lst = other if not isinstance(other, CustomList) else other.lst
        lst, other_lst = self.normalize_len(self.lst, other_lst)
        result = [other_lst[i] - v for i, v in enumerate(lst)]
        return CustomList(result)

    def __eq__(self, other):
        return sum(self.lst) == sum(other.lst)

    def __ne__(self, other):
        return sum(self.lst) != sum(other.lst)

    def __ge__(self, other):
        return sum(self.lst) >= sum(other.lst)

    def __gt__(self, other):
        return sum(self.lst) > sum(other.lst)

    def __lt__(self, other):
        return sum(self.lst) < sum(other.lst)

    def __le__(self, other):
        return sum(self.lst) <= sum(other.lst)

    def __str__(self):
        return f'{self.lst} Сумма: {sum(self.lst)}'
