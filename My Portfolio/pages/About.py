import streamlit as st

st.title("👩 About Me")

st.image("pages/grdr 2025-05-31 142856.632.jpg", width=200, caption="Rachel💐")
st.write("""
My name is Rachel. I am passionate, creative, and hardworking.
I love learning new things especially in technology and design. I enjoy expressing myself through art, technology and meaningful projects.
""")

st.header("My Personal information")

st.subheader("📌 Basic Details")

st.write("🎂 Birthday:December 12, 2004")
st.write("🎈 Age:21  years old")
st.write("📍 Location: Masbate Philippines")


st.subheader("🎨 My Hobbies")

st.markdown("""
- 🎵 Listening to Music  
- 🎬 Watching Movies  
- 💻 Exploring Technology  
- 📷 Taking Photos  
- 🎨 Designing / Creativity 
- ✈️Travelling 
- 📖 Reading books
""")

# Favorites
st.subheader("💖 My Favorites")

col1, col2 = st.columns(2)

with col1:
    st.success("🎨 Favorite Color: Purple")
    st.success("🍔 Favorite Food: Chicken carry")
    st.success("🥤 Favorite Drink: Cucumber")

with col2:
    st.info("🎵 Favorite Music: BTS song / OPM")
    st.info("🎬 Favorite Movie Genre: Horror / Comedy")
    st.info("🌸 Favorite Flower: Tulips and Sunflower")


st.subheader("🌟 Personality")

st.write("""
✔ Friendly  
✔ Creative  
✔ Hardworking  
✔ Positive Thinker  
✔ Goal Oriented
""")


st.subheader("🚀 Future Dream")

st.warning("To become successful and achieve my goals in life.")


st.subheader("💬 Favorite Quote")

st.info("Believe in yourself and everything becomes possible.")