import streamlit as st
import llm_helper
from PIL import Image

def main():

    logo = Image.open("assets/favicon.ico")

    st.set_page_config(page_title="ContentCreek - Blog Generator", layout="centered",page_icon=logo)

    # App title
    st.title("🌟 ContentCreek 🌟")
    st.markdown("""
    **Welcome to ContentCreek**  
    Your neighborhood blog generation tool! Just provide a title and select the desired word count to generate engaging blog content. ✨
    """)

    # Input fields
    st.header("✍️ Enter Your Blog Details")
    title = st.text_input("Blog Title 📝")

    # Word count slider
    word_count = st.slider("🧩 Select Number of Words",
                           min_value=5,
                           max_value=500,
                           value=100,
                           step=5)

    # Generate button
    if st.button("🚀 Generate Blog"):
        if title:
            with st.spinner('Generating blog content...'):
                content = llm_helper.generate_response(title, word_count)
            st.write(f"**Generated Blog for:** _{title}_")
            st.text_area("📜 Generated Blog",
                         value=content,
                         height=300,
                         key="output")
            # # Copy to Clipboard button
            st.download_button(label="📋 Download",
                               data=content,
                               file_name="generated_blog.txt",
                               mime="text/plain")
            # if st.button("📋 Copy to Clipboard"):
            #     llm_helper.copy_to_clipboard(st, content)
        else:
            st.warning("🚨 Please enter a blog title before generating!")

if __name__ == "__main__":
    main()
