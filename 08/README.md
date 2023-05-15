### Замеры времени при большом количестве экземпляров с помощью функции default_timer из библиотеки timeit

![Замеры времени](https://github.com/ovsyannikovas/Ovsyannikova_dp_spring_2023/blob/main/08/time.png)

Быстрее всего создается пачка экземпляров класса Employee с weakref, медленнее - класса Employee без weakref.
Время чтения/изменения меньше всего у экземпляров класса EmployeeSlots, медленнее - у класса Employee с weakref.

### Профилирование с помощью декоратора @profile

![Профилирование profile](https://github.com/ovsyannikovas/Ovsyannikova_dp_spring_2023/blob/main/08/profile_classes.png)

Больше всего пямяти занимают экземпляры класса Employee, меньше всего - класса Employee с weakref.

### Профилирование с помощью написанного декоратора @profile_decorator

![Профилирование profile_decorator](https://github.com/ovsyannikovas/Ovsyannikova_dp_spring_2023/blob/main/08/profile_decorator.png)

Профилирование с декоратором @profile_decorator показывает аналогичные результаты.
