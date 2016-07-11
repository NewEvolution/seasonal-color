class Person:

    def __init__(self):
        self.skin_tone = ''
        self.skin_undertone = ''
        self.season = ''

    def match_color_to_season(self, color):
        pairings = {
                'yellow': 'winter',
                'pink': 'spring',
                'blue': 'summer',
                'green': 'fall'
                }
        self.season = pairings[color]
        return self.season

    def match_season_to_palette(self, season):
        pairings = {
                'winter': ['325C', '608D', '323A'],
                'spring': ['536F', '847K', '243A'],
                'summer': ['948G', '915T', '256F'],
                'fall': ['822S', '363G', '543K']
                }
        return pairings[season]
