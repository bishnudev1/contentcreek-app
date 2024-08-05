# ContentCreek

**Your neighborhood blog generation tool!** Just provide a title and select the desired word count to generate engaging blog content.

## Overview

ContentCreek is a powerful blog generation application that leverages advanced AI technologies to create high-quality, engaging content. Built using the `Llama-2-7B-32K-Instruct` model from Together AI and the LangChain library, ContentCreek provides a seamless experience for generating blog posts directly from your browser.

## Features

- **AI-Powered Content Generation**: Utilizes the `Llama-2-7B-32K-Instruct` model to generate contextually relevant and engaging blog content.
- **Customizable Word Count**: Choose the desired word count for your blog post to fit your specific needs.
- **User-Friendly Interface**: Developed with Streamlit for an intuitive and interactive web frontend.
- **Open Source**: Contribute and collaborate on GitHub to improve and expand the app's features.

## Tech Stack

- **AI Model**: `Llama-2-7B-32K-Instruct` by Together AI
- **Language**: Python
- **Web Frontend**: Streamlit
- **Content Generation Framework**: LangChain

## How to Use

1. **Provide a Title**: Enter a title for the blog post you want to generate.
2. **Select Word Count**: Choose the number of words for your blog post.
3. **Generate Content**: Click the generate button to create your blog post instantly.

## Installation

To run ContentCreek locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/contentcreek.git
2. Navigate to the project directory:
   ```bash
   cd contentcreek
   ```
3. Install all the required dependencies by:
   ```bash
   pip install -r requirements.txt
   ```
4. Create an .env variable in root directory with your own together api key:
   ```bash
   TOGETHER_API_KEY = "your-together-api-key"
   ```
5. Run the app locally by:
   ```bash
   streamlit run main.py
   ```

## Future contributions 
- Try to shift the UI part to Flask/FastAPI from Streamlit as some features like copy_to_clipboard does work good in cloud.
- Try some higher LLM's with bigger parameters such as GPT4 or Gemini to get 200% better responses.


## Want to learn or get practicals on Data Science end to end with notes ??
- Visit https://github.com/bishnudev1/MLOps 🥹
