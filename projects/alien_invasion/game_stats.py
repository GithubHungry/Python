class GameStats():
    """Player stats in the game."""

    def __init__(self, ai_settings):
        """Initializing game stats."""
        self.ai_settings = ai_settings
        self.game_active = False
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        """Initializing stats, which will change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
