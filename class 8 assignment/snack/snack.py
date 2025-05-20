class Snack:
    category_emojis = {
        "sweet": "🍭",
        "salty": "🥨",
        "healthy": "🥗",
        "quick": "⏱️",
        "drink": "🥤",
        "fried": "🍟",
        "baked": "🥐"
    }

    def __init__(self, name, category, mood_tags, time_tags, is_healthy=False, note=None, popularity=0):
        self.name = name
        self.category = category.lower()
        self.mood_tags = [tag.lower() for tag in mood_tags]
        self.time_tags = [tag.lower() for tag in time_tags]
        self.is_healthy = is_healthy
        self.note = note
        self.popularity = popularity

    def __str__(self):
        emoji = self.category_emojis.get(self.category, "🍿")
        health = "✅ Healthy" if self.is_healthy else "⚠️ Indulgent"
        note = f" - {self.note}" if self.note else ""
        return f"{emoji} {self.name} ({self.category.capitalize()}) | {health}{note}"

    def matches_mood(self, mood):
        return mood.lower() in self.mood_tags

    def matches_time(self, time):
        return time.lower() in self.time_tags

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "mood_tags": self.mood_tags,
            "time_tags": self.time_tags,
            "is_healthy": self.is_healthy,
            "note": self.note,
            "popularity": self.popularity
        }
