class GameStats(object):
    """Track statistics for Alien Invastion."""
    def __init__(self, ai_settings):
        """Initialize statistis."""
        self.ai_settings = ai_settings
        self.reset_stats()


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.ai_settings.ship_limit
