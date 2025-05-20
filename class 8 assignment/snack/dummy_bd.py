from snack import Snack

snack_list = [
    Snack(
        name="Spicy Chips",
        category="spicy",
        mood_tags=["lazy", "sad", "bored"],
        time_tags=["evening", "night"],
        is_healthy=False,
        note="Crunchy and spicy, great for Netflix binges!",
        popularity=78
    ),
    Snack(
        name="Fruit Salad",
        category="healthy",
        mood_tags=["fresh", "energetic", "calm"],
        time_tags=["morning", "afternoon"],
        is_healthy=True,
        note="Naturally sweet and refreshing",
        popularity=65
    ),
    Snack(
        name="Dark Chocolate",
        category="sweet",
        mood_tags=["happy", "sad", "romantic"],
        time_tags=["any"],
        is_healthy=False,
        note="Mood-lifting and rich in antioxidants",
        popularity=90
    ),
    Snack(
        name="Butter Popcorn",
        category="salty",
        mood_tags=["chill", "bored", "lazy"],
        time_tags=["night", "evening"],
        is_healthy=False,
        note="Perfect for movie nights!",
        popularity=85
    ),
    Snack(
        name="Choco Cookies",
        category="sweet",
        mood_tags=["happy", "lazy", "hungry"],
        time_tags=["evening", "afternoon"],
        is_healthy=False,
        note="Classic treat with chocolate chips",
        popularity=88
    ),
    Snack(
        name="Greek Yogurt",
        category="healthy",
        mood_tags=["calm", "tired", "focused"],
        time_tags=["morning", "any"],
        is_healthy=True,
        note="High in protein and gut-friendly",
        popularity=70
    ),
    Snack(
        name="Energy Bar",
        category="quick",
        mood_tags=["focused", "energetic"],
        time_tags=["morning", "afternoon"],
        is_healthy=True,
        note="Quick energy boost for busy days",
        popularity=60
    ),
    Snack(
        name="French Fries",
        category="fried",
        mood_tags=["lazy", "sad", "bored"],
        time_tags=["afternoon", "evening"],
        is_healthy=False,
        note="Golden and crispy comfort food",
        popularity=95
    )
]
