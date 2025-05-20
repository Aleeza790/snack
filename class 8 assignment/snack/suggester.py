import random

class SuggestionEngine:
    def __init__(self, snack_data):
        self.snack_data = snack_data
        self.last_suggestion = None

    def suggest_by_mood(self, mood, healthy_only=False):
        mood = mood.lower()
        matches = [snack for snack in self.snack_data if snack.matches_mood(mood)]

        if healthy_only:
            matches = [s for s in matches if s.is_healthy]

        if not matches:
            return self._fallback("mood")

        return self._select_snack(matches)

    def suggest_by_time(self, time_of_day, healthy_only=False):
        time_of_day = time_of_day.lower()
        matches = [snack for snack in self.snack_data if snack.matches_time(time_of_day) or 'any' in snack.time_tags]

        if healthy_only:
            matches = [s for s in matches if s.is_healthy]

        if not matches:
            return self._fallback("time")

        return self._select_snack(matches)

    def suggest_by_category(self, category):
        category = category.lower()
        matches = [snack for snack in self.snack_data if snack.category == category]
        return self._select_snack(matches)

    def suggest_random(self, healthy_only=False):
        pool = [s for s in self.snack_data if s.is_healthy] if healthy_only else self.snack_data
        return self._select_snack(pool)

    def _select_snack(self, snacks):
        if not snacks:
            return None
        # Weighted randomness by popularity
        weighted = [(snack, snack.popularity + 1) for snack in snacks]
        selected = random.choices(
            [snack for snack, _ in weighted],
            weights=[w for _, w in weighted],
            k=1
        )[0]
        self.last_suggestion = selected
        return selected

    def _fallback(self, reason):
        # Smart fallback logic — return a random snack
        return self.suggest_random()

    def get_last_suggestion(self):
        return self.last_suggestion
