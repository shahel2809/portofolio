import streamlit as st

# Set page configuration to force Dark Mode and set the title
st.set_page_config(
    page_title="Shahelnetha's Portfolio",
    page_icon="👋",
    layout="centered",
    initial_sidebar_state="expanded",
)

# You can use standard Markdown to write content
st.title("👋 Hi, I'm Shahelnetha")
st.subheader("A passionate beginner Python Developer")

# Adding some styling and spacing
st.write("---")

# Section 1: About Me
st.header("🧑‍💻 About Me")
st.write("""
Welcome to my very first Python-based portfolio! 
I am currently learning programming and exploring the incredible world of Python. 
I enjoy solving problems, writing scripts, and building clean, simple applications like this one.
""")

# Section 2: Skills
st.header("🛠️ Skills")
# We use columns to make it look nicer
col1, col2 = st.columns(2)
with col1:
    st.write("✅ Python")
    st.write("✅ HTML / CSS")
with col2:
    st.write("✅ Problem Solving")
    st.write("✅ Teamwork")

# Section 3: Projects
st.write("---")
st.header("🚀 Projects")

# Using an expander block to keep it neat
with st.expander("1. My Python Portfolio (This App!)"):
    st.write("""
    Built using **Streamlit**, a Python library that makes it incredibly easy to turn data scripts into shareable web apps. 
    It features a sleek dark mode design and showcases my coding journey!
    """)
    
with st.expander("2. Number Guessing Game (Example)"):
    st.write("""
    A simple command-line game built purely in Python where the user has to guess a randomly generated number.
    """)

# Section 4: Contact
st.write("---")
st.header("📫 Get In Touch")
st.write("Want to chat about code or collaborate? Reach out to me!")

# Displaying contact info like buttons
st.markdown("[📧 Email Me](mailto:shahelnetha@example.com)")
st.markdown("[🐙 GitHub Profile](https://github.com/)")

# Footer
st.write("---")
st.caption("Built with ❤️ using Python and Streamlit.")
