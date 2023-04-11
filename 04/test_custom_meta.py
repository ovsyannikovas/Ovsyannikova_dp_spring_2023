import unittest
from custom_meta import CustomClass


class TestCustomClass(unittest.TestCase):

    def test_class_default_attrs(self):
        self.assertTrue(hasattr(CustomClass, 'custom_x'))
        self.assertFalse(hasattr(CustomClass, 'x'))
        self.assertEqual(CustomClass.custom_x, 50)

        self.assertTrue(hasattr(CustomClass, 'custom_line'))
        self.assertFalse(hasattr(CustomClass, 'line'))

    def test_inst_class_attrs(self):
        inst = CustomClass()

        self.assertTrue(hasattr(inst, 'custom_val'))
        self.assertFalse(hasattr(inst, 'val'))

    def test_inst_class_attr_val(self):
        inst = CustomClass(99)

        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_x, 50)

    def test_class_method_line(self):
        inst = CustomClass()
        self.assertTrue(hasattr(inst, 'custom_line'))
        self.assertFalse(hasattr(inst, 'line'))
        self.assertTrue(inst.custom_line(), 100)

    def test_class_method_str(self):
        inst = CustomClass()
        self.assertTrue(hasattr(inst, '__str__'))
        self.assertFalse(hasattr(inst, 'custom___str__'))
        self.assertTrue(str(inst), 'Custom_by_metaclass')

    def test_class_magic_methods(self):
        inst = CustomClass()
        self.assertTrue(hasattr(inst, '__str__'))
        self.assertFalse(hasattr(inst, 'custom___str__'))

    def test_class_non_attribute(self):
        inst = CustomClass()
        self.assertFalse(hasattr(inst, 'yyy'))

    def test_class_with_dynamic_var(self):
        inst = CustomClass()
        inst.dynamic = 'added later'

        self.assertTrue(hasattr(inst, 'custom_dynamic'))
        self.assertFalse(hasattr(inst, 'dynamic'))
        self.assertEqual(inst.custom_dynamic, 'added later')
