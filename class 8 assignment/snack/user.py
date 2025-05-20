import uuid

class User:
    def __init__(self, name="Guest"):
        self.name = name
        self.user_id = str(uuid.uuid4())[:8]  # short unique ID
        self.favorites = []
        self.recent_history = []

    def add_favorite(self, snack):
        if snack not in self.favorites:
            self.favorites.append(snack)

    def remove_favorite(self, snack):
        if snack in self.favorites:
            self.favorites.remove(snack)

    def get_favorites(self):
        return self.favorites

    def add_to_history(self, snack):
        if snack in self.recent_history:
            self.recent_history.remove(snack)
        self.recent_history.insert(0, snack)
        if len(self.recent_history) > 5:
            self.recent_history.pop()

    def get_recent_history(self):
        return self.recent_history

    def reset_user(self):
        self.favorites = []
        self.recent_history = []

    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id,
            "favorites": [str(snack) for snack in self.favorites],
            "recent_history": [str(snack) for snack in self.recent_history]
        }

    def __str__(self):
        return f"{self.name} ({self.user_id})"
