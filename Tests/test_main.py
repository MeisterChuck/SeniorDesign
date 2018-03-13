from unittest import TestCase
from GetData.GetData import GetData


class TestMain(TestCase):
    def test_main(self):
        mental_state = ["Emotion", "Gambling", "Rest", "Structural", "WM"]
        data = GetData(mental_state)

        self.assertTrue(mental_state == data.category)
