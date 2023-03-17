import unittest
from unittest import mock

from predict_message_mood import SomeModel, predict_message_mood, BoundaryException


class TestSomeModel(unittest.TestCase):
    def setUp(self):
        self.model = SomeModel()

    def test_bad_mood(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.2

            self.assertEqual(predict_message_mood('message', self.model), 'неуд')

    def test_good_mood(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.9

            self.assertEqual(predict_message_mood('message', self.model), 'отл')

    def test_normal_mood(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.5

            self.assertEqual(predict_message_mood('message', self.model), 'норм')

    def test_normal_mood_with_empty_string(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.5

            self.assertEqual(predict_message_mood('', self.model), 'норм')

    def test_normal_mood_with_castom_thresholds(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.2

            self.assertEqual(predict_message_mood('message', self.model, 0.1, 0.5), 'норм')

    def test_normal_mood_with_bad_grater_than_good(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.5

            with self.assertRaises(BoundaryException) as context:
                predict_message_mood('message', self.model, 0.8, 0.3)

            self.assertTrue(isinstance(context.exception, BoundaryException))
