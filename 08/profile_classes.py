import weakref
from memory_profiler import profile
from timeit import default_timer


class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class EmployeeSlots():
    __slots__ = ("name", "salary")

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


@profile
def run_employee(n):
    # time1 = default_timer()
    employees = [Employee("Имя", 12345) for _ in range(n)]
    # time2 = default_timer() - time1
    #
    # time3 = default_timer()
    for e in employees:
        e.name = "Новое имя"
        e.salary += 1000
    # time4 = default_timer() - time3
    #
    # print(f'''
    # Время создания пачки экземпляров класса Employee: {time2}
    # Время чтения/изменения атрибутов экземпляров класса Employee: {time4}
    # ''')


@profile
def run_slot_employee(n):
    # time1 = default_timer()
    employees = [EmployeeSlots("Имя", 12345) for _ in range(n)]
    # time2 = default_timer() - time1
    #
    # time3 = default_timer()
    for e in employees:
        e.name = "Новое имя"
        e.salary += 1000
    # time4 = default_timer() - time3
    #
    # print(f'''
    # Время создания пачки экземпляров класса EmployeeSlots: {time2}
    # Время чтения/изменения атрибутов экземпляров класса EmployeeSlots: {time4}
    # ''')


@profile
def run_weakref_employee(n):
    employees = []
    parent_class = Employee("Имя", 12345)

    # time1 = default_timer()
    for e in range(n):
        employees.append(weakref.ref(parent_class)())
    # time2 = default_timer() - time1
    #
    # time3 = default_timer()
    for e in employees:
        e.name = "Новое имя"
        e.salary += 1000
    # time4 = default_timer() - time3
    #
    # print(f'''
    # Время создания пачки экземпляров класса Employee с weakref: {time2}
    # Время чтения/изменения атрибутов экземпляров класса Employee с weakref: {time4}
    # ''')


if __name__ == '__main__':
    N = 500_000

    run_employee(N)
    run_slot_employee(N)
    run_weakref_employee(N)
