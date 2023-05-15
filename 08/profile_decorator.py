import weakref
import cProfile
import pstats
import io


class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class EmployeeSlots():
    __slots__ = ("name", "salary")

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


def profile_decorator(func):
    def wrap(*args, **kwargs):
        profiler = cProfile.Profile()

        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()

        out = io.StringIO()
        stats = pstats.Stats(profiler, stream=out)
        stats.print_stats()

        print(out.getvalue())
        return result

    return wrap


@profile_decorator
def run_employee(n):
    employees = [Employee("Имя", 12345) for _ in range(n)]

    for e in employees:
        e.name = "Новое имя"
        e.salary += 1000


@profile_decorator
def run_slot_employee(n):
    employees = [EmployeeSlots("Имя", 12345) for _ in range(n)]

    for e in employees:
        e.name = "Новое имя"
        e.salary += 1000


@profile_decorator
def run_weakref_employee(n):
    employees = []
    parent_class = Employee("Имя", 12345)

    for e in range(n):
        employees.append(weakref.ref(parent_class)())

    for e in employees:
        e.name = "Новое имя"
        e.salary += 1000


if __name__ == '__main__':
    N = 500_000

    run_employee(N)
    run_slot_employee(N)
    run_weakref_employee(N)
