import unittest

class TestPerson:

    def test_skin_tone_default_value_is_empty_string(self):
        self.assertEqual(self.a_person.skin_tone, '')

    def test_skin_undertone_default_value_is_empty_string(self):
        self.assertEqual(self.a_person.skin_undertone, '')

    def test_season_value_is_empty_string(self):
        self.assertEqual(self.a_person.season, '')

    def test_match_yellow_to_winter(self):
        self.assertEqual(self.a_person.match_color_to_season('yellow'), 'winter')

    def test_match_pink_to_spring(self):
        self.assertEqual(self.a_person.match_color_to_season('pink'), 'spring')

    def test_match_blue_to_summer(self):
        self.assertEqual(self.a_person.match_color_to_season('blue'), 'summer')

    def test_match_green_to_fall(self):
        self.assertEqual(self.a_person.match_color_to_season('green'), 'fall')
