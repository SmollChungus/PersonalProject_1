class Achievement:
    def __init__(self, name, description, criteria, tier):
        self.name = name
        self.description = description
        self.criteria = criteria
        self.unlocked = False
        self.tier = tier  