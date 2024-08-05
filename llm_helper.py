import together
from langchain.prompts import PromptTemplate
from st_copy_to_clipboard import st_copy_to_clipboard
import os
from dotenv import load_dotenv

load_dotenv()

# Set your API key
together.api_key = os.getenv('TOGETHER_API_KEY')

isloading = False


def generate_response(topic, words=250):
  global isloading
  try:
    isloading = True
    template = """
            write a blog on topic {topic} within {words} words.
        """

    prompt = PromptTemplate(
        input_variables=["topic", "words"],
        template=template,
    )

    llm = together.Complete.create(
        model="togethercomputer/Llama-2-7B-32K-Instruct",
        max_tokens=words,
        temperature=0.7,
        prompt=prompt.format(topic=topic, words=words))

    result = llm["choices"][0]["text"]
    print(result)
    return result
  except Exception as e:
    print(e)
    return "Error occurred while generating the blog"
  finally:
    isloading = False


def copy_to_clipboard(st, text):
  try:
    st_copy_to_clipboard(text)
    st.success("Text copied to clipboard")

  except Exception as e:
    st.error(f"Error occurred while copying to clipboard: {e}")
