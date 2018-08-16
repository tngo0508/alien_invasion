class GameStats(object):
    """Track statistics for Alien Invastion."""
    def __init__(self, ai_settings):
        """Initialize statistis."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
