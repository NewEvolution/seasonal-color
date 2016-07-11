import unittest

class TestPerson:

    @classmethod
    def classSetup(self):
        self.a_person = Person()

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

    def test_match_season_to_palette(self):
        self.assertEqual(self.a_person.match_season_to_palette('winter'), ['325C', '608D', '323A'])
        self.assertEqual(self.a_person.match_season_to_palette('spring'), ['536F', '847K', '243A'])
        self.assertEqual(self.a_person.match_season_to_palette('summer'), ['948G', '915T', '256F'])
        self.assertEqual(self.a_person.match_season_to_palette('fall'), ['822S', '363G', '543K'])
