import streamlit as st
import random

# Mocked snack database
snack_db = {
    "happy": ["🍦 Ice Cream", "🍭 Lollipop", "🧁 Cupcake"],
    "sad": ["🍫 Chocolate", "🥧 Pie", "🍪 Cookie"],
    "lazy": ["🍿 Popcorn", "🍟 Fries", "🍕 Pizza"],
    "fresh": ["🍎 Apple", "🥒 Cucumber sticks", "🍉 Watermelon"],

    "morning": ["🥞 Pancakes", "☕ Coffee & Biscuit", "🍌 Banana"],
    "afternoon": ["🥪 Sandwich", "🥤 Cold Drink", "🥗 Salad"],
    "evening": ["🍜 Noodles", "🌮 Tacos", "🥟 Dumplings"],
    "night": ["🍔 Burger", "🍩 Donut", "🥛 Warm Milk"]
}

random_snacks = list({snack for snacks in snack_db.values() for snack in snacks})


# Session Setup
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

if 'last_snack' not in st.session_state:
    st.session_state.last_snack = None

# --- Main Title ---
st.markdown("""
    <div style='text-align:center'>
        <h1 style='color:#6C63FF;'>🧞‍♂️ Snack Genie</h1>
        <h3>Your Magical Snack Companion ✨</h3>
    </div>
""", unsafe_allow_html=True)

st.divider()

# --- 3 Panel Menu ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🎭 By Mood")
    mood = st.text_input("Enter your mood (e.g. happy, sad, lazy, fresh)")
    if st.button("Suggest by Mood"):
        mood = mood.lower()
        if mood in snack_db:
            snack = random.choice(snack_db[mood])
            st.session_state.last_snack = snack
        else:
            st.warning("Mood not found in Genie’s book!")

with col2:
    st.subheader("🕓 By Time")
    time = st.selectbox("Choose time of day", ["", "morning", "afternoon", "evening", "night"])
    if st.button("Suggest by Time"):
        if time:
            snack = random.choice(snack_db[time])
            st.session_state.last_snack = snack
        else:
            st.warning("Pick a time to continue.")

with col3:
    st.subheader("🎲 Random")
    if st.button("Surprise Me!"):
        snack = random.choice(random_snacks)
        st.session_state.last_snack = snack

# --- Show Snack Suggestion ---
if st.session_state.last_snack:
    st.markdown(f"""
    <div style='text-align:center; margin-top:20px'>
        <h2>🧞 Genie suggests:</h2>
        <h1 style='font-size:48px'>{st.session_state.last_snack}</h1>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💖 Add to Favorites"):
        if st.session_state.last_snack not in st.session_state.favorites:
            st.session_state.favorites.append(st.session_state.last_snack)
            st.success("Added to favorites!")
        else:
            st.info("Already in favorites.")

# --- Favorites Section ---
st.divider()
st.subheader("⭐ Your Favorite Snacks")

if st.session_state.favorites:
    for fav in st.session_state.favorites:
        st.markdown(f"- {fav}")
else:
    st.info("You have no favorite snacks yet.")

