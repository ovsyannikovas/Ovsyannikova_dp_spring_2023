class CustomMeta(type):
    def __new__(mcs, name, bases, classdict, **kwargs):
        custom_classdict = {}
        custom_classdict['__setattr__'] = mcs.__setattr__

        for attr, val in classdict.items():
            if attr.startswith('__') and attr.endswith('__'):
                key = attr
            else:
                key = f'custom_{attr}'
            custom_classdict[key] = val

        return super().__new__(mcs, name, bases, custom_classdict)

    def __setattr__(cls, name, val):
        cls.__dict__[f'custom_{name}'] = val


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return 'Custom_by_metaclass'
