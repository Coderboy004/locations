import unittest
from locations.main import Location


class TEST(unittest.TestCase):

    def Finding_Location(self):
        self.assertEqual(Location.Find_Location(text="San Francisco Mumbai allahabad ca us"))


unittest.main()