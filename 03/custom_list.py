class CustomList(list):
    @staticmethod
    def normalize_len(lst1, lst2):
        new_lst1, new_lst2 = lst1.copy(), lst2.copy()
        difference = len(lst1) - len(lst2)
        if difference > 0:
            new_lst2 += [0] * difference
        elif difference < 0:
            new_lst1 += [0] * -difference
        return new_lst1, new_lst2

    def __add__(self, other):
        lst, other_lst = self.normalize_len(self, other)
        result = [v + other_lst[i] for i, v in enumerate(lst)]
        return CustomList(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        lst, other_lst = self.normalize_len(self, other)
        result = [v - other_lst[i] for i, v in enumerate(lst)]
        return CustomList(result)

    def __rsub__(self, other):
        lst, other_lst = self.normalize_len(self, other)
        result = [other_lst[i] - v for i, v in enumerate(lst)]
        return CustomList(result)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __str__(self):
        lst_str = super().__str__()
        return f'{lst_str} Сумма: {sum(self)}'
