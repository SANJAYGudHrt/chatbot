import streamlit as st
import openai
from spellchecker import SpellChecker


def correct_spelling(input_text):
    if not input_text:
        return input_text

    spell = SpellChecker()
    words = input_text.split()
    corrected_words = [spell.correction(word) for word in words]
    return " ".join(corrected_words)


def chat_with_gpt(input_topic):
    # Correct the input sentence for spelling mistakes
    corrected_topic = correct_spelling(input_topic)

    # Make API call to ChatGPT
    api_key = 'Your_api_key'
    openai.api_key = api_key

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use GPT-3.5 engine
            prompt=corrected_topic,
            max_tokens=100
        )

        if response and 'choices' in response and len(response['choices']) > 0:
            answer = response['choices'][0]['text'].strip()
            return answer
    except Exception as e:
        st.error(f"Error in API call: {e}")

    return "Error in API call. Please try again later."


def main():
    st.title("Chatbot with GPT-3.5 API and Spell Check")

    # Get the input topic from the user
    input_topic = st.text_input("Enter your topic:")

    if st.button("Get Answer"):
        if input_topic:
            # Chat with GPT and get the answer
            answer = chat_with_gpt(input_topic)
            st.subheader("Answer (less than 100 words):")
            st.write(answer)
        else:
            st.warning("Please enter a topic to get an answer.")


if __name__ == "__main__":
    main()
