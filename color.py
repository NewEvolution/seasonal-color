import unittest

class TestPerson:

    def test_skin_tone_default_value_is_empty_string(self):
        a_person = Person()
        self.assertEqual(a_person.skin_tone, '')

    def test_skin_undertone_default_value_is_empty_string(self):
        a_person = Person()
        self.assertEqual(a_person.skin_undertone, '')

    def test_season_value_is_empty_string(self):
        a_person = Person()
        self.assertEqual(a_person.season, '')

    def test_match_yellow_to_winter(self):
        a_person = Person()
        a_person.skin_undertone = 'yellow'
        self.assertEqual(a_person.match_color_to_season(), 'winter')

    def test_match_pink_to_spring(self):
        a_person = Person()
        a_person.skin_undertone = 'pink'
        self.assertEqual(a_person.match_color_to_season(), 'spring')

    def test_match_blue_to_summer(self):
        a_person = Person()
        a_person.skin_undertone = 'blue'
        self.assertEqual(a_person.match_color_to_season(), 'summer')

    def test_match_green_to_fall(self):
        a_person = Person()
        a_person.skin_undertone = 'green'
        self.assertEqual(a_person.match_color_to_season(), 'fall')
