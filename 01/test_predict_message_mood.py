import unittest
from unittest import mock

from predict_message_mood import SomeModel, predict_message_mood, BoundaryException


class TestSomeModel(unittest.TestCase):
    def setUp(self):
        self.model = SomeModel()

    def test_bad_mood(self):
        with mock.patch('predict_message_mood.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.2

            self.assertEqual(predict_message_mood('message', self.model), 'неуд')
            self.assertEqual(mock_model.call_args.args, ('message',))

    def test_good_mood(self):
        with mock.patch('predict_message_mood.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.9

            self.assertEqual(predict_message_mood('message', self.model), 'отл')
            self.assertEqual(mock_model.call_args.args, ('message',))

    def test_normal_mood(self):
        with mock.patch('predict_message_mood.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.5

            self.assertEqual(predict_message_mood('message', self.model), 'норм')
            self.assertEqual(mock_model.call_args.args, ('message',))

    def test_normal_mood_with_empty_string(self):
        with mock.patch('predict_message_mood.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.5

            self.assertEqual(predict_message_mood('', self.model), 'норм')
            self.assertEqual(mock_model.call_args.args, ('',))

    def test_normal_mood_with_castom_thresholds(self):
        with mock.patch('predict_message_mood.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.2

            self.assertEqual(predict_message_mood('message', self.model, 0.1, 0.5), 'норм')
            self.assertEqual(mock_model.call_args.args, ('message',))

    def test_normal_mood_with_bad_grater_than_good(self):
        with mock.patch('predict_message_mood.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.5

            with self.assertRaises(BoundaryException) as context:
                predict_message_mood('message', self.model, 0.8, 0.3)
                self.assertEqual(mock_model.call_args.args, ('message',))

            self.assertTrue(isinstance(context.exception, BoundaryException))

    def test_bad_mood_boundary(self):
        with mock.patch('predict_message_mood.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.3

            self.assertEqual(predict_message_mood('message', self.model), 'норм')
            self.assertEqual(mock_model.call_args.args, ('message',))

    def test_good_mood_boundary(self):
        with mock.patch('predict_message_mood.SomeModel.predict') as mock_model:
            mock_model.return_value = 0.8

            self.assertEqual(predict_message_mood('message', self.model), 'норм')
            self.assertEqual(mock_model.call_args.args, ('message',))
