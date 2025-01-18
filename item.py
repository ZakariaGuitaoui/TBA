"""class item"""
class Item:
    """class item"""
    def __init__(self, name, description, weight):
        """mise en place"""
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        """mise en place"""
        return f"{self.name}: {self.description} (Weight: {self.weight}kg)"
