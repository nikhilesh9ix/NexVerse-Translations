import streamlit as st
from datetime import date
from gtts import gTTS, lang
from deep_translator import GoogleTranslator
import PyPDF2

# setting app's title, icon & layout
st.set_page_config(page_title="NexVerse", page_icon="🌐")

def get_key(val):
    """function to find the key of the given value in the dict object

    Args:
        val (str): value to find key

    Returns:
        key(str): key for the given value
    """
    for key, value in lang.tts_langs().items():
        if val == value:
            return key

def categorize_languages():
    """Separate languages into Indian and World categories."""
    indian_languages = ['Hindi', 'Bengali', 'Telugu', 'Marathi', 'Tamil', 'Urdu', 'Gujarati', 'Malayalam', 'Kannada', 'Odia', 'Punjabi']
    langs = lang.tts_langs()
    indian_langs = {key: value for key, value in langs.items() if value in indian_languages}
    world_langs = {key: value for key, value in langs.items() if value not in indian_languages}
    return indian_langs, world_langs

def read_pdf(file):
    """Reads a PDF file and extracts text from it.

    Args:
        file (BytesIO): BytesIO object representing the uploaded PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text

def translate_pdf_text(pdf_text, dest_lang):
    """Translates text extracted from a PDF to the specified destination language.

    Args:
        pdf_text (str): Text extracted from the PDF.
        dest_lang (str): Destination language for translation.

    Returns:
        str: Translated text.
    """
    translation = GoogleTranslator(source='auto', target=dest_lang).translate(pdf_text)
    return translation

def collect_feedback():
    feedback = st.sidebar.text_area("Feedback:", max_chars=500)
    if st.sidebar.button("Submit Feedback") and feedback:
        st.sidebar.success("Thank you for your feedback!")

def main():
    # gets gtts supported languages as dict
    indian_languages, world_languages = categorize_languages()

    st.header("Translate your thoughts.")
    st.write(f"Date : {date.today()}")

    translation_choice = st.radio("Choose an option:", ["Translate Sentence", "Translate PDF"])

    if translation_choice == "Translate Sentence":
        input_text = st.text_input("Enter text for translation", key="input_text")
        lang_choice_category = st.selectbox("Select Language Category", ["Indian Languages", "World Languages"])

        if lang_choice_category == "Indian Languages":
            lang_choices = indian_languages.values()
        else:
            lang_choices = world_languages.values()

        lang_choice = st.selectbox("Language to translate: ", lang_choices, key="lang_choice")

        if st.button("Translate"):
            if input_text == "":
                st.write("Please Enter text to translate")
            else:
                detect_expander = st.expander("Detected Language")
                with detect_expander:
                    from langdetect import detect
                    detected_lang = detect(input_text)
                    detect_text = f"Detected Language : {indian_languages.get(detected_lang, detected_lang)}"
                    st.success(detect_text)

                    detect_audio = gTTS(text=input_text, lang=detected_lang, slow=False)
                    detect_audio.save("user_detect.mp3")
                    audio_file = open("user_detect.mp3", "rb")
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format="audio/ogg", start_time=0)

                trans_expander = st.expander("Translated Text")
                with trans_expander:
                    translation = GoogleTranslator(source='auto', target=get_key(lang_choice)).translate(input_text)
                    translation_text = f"Translated Text : {translation}"
                    st.success(translation_text)

                    translated_audio = gTTS(text=translation, lang=get_key(lang_choice), slow=False)
                    translated_audio.save("user_trans.mp3")
                    audio_file = open("user_trans.mp3", "rb")
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format="audio/ogg", start_time=0)

                    with open("user_trans.mp3", "rb") as file:
                        st.download_button(
                            label="Download",
                            data=file,
                            file_name="trans.mp3",
                            mime="audio/ogg",
                        )

    elif translation_choice == "Translate PDF":
        uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])

        if uploaded_file is not None:
            pdf_text = read_pdf(uploaded_file)
            st.subheader("PDF Text:")
            st.write(pdf_text)

            lang_choice_pdf_category = st.selectbox("Select Language Category for PDF", ["Indian Languages", "World Languages"])

            if lang_choice_pdf_category == "Indian Languages":
                lang_choices_pdf = indian_languages.values()
            else:
                lang_choices_pdf = world_languages.values()

            lang_choice_pdf = st.selectbox("Language to translate PDF text: ", lang_choices_pdf, key="lang_choice_pdf")

            if st.button("Translate PDF Text"):
                if not pdf_text:
                    st.warning("The PDF does not contain any text.")
                else:
                    translated_pdf_text = translate_pdf_text(pdf_text, get_key(lang_choice_pdf))
                    st.subheader("Translated PDF Text:")
                    st.success(translated_pdf_text)

                    translated_pdf_audio = gTTS(text=translated_pdf_text, lang=get_key(lang_choice_pdf), slow=False)
                    translated_pdf_audio.save("translated_pdf.mp3")
                    audio_file_pdf = open("translated_pdf.mp3", "rb")
                    audio_bytes_pdf = audio_file_pdf.read()
                    st.audio(audio_bytes_pdf, format="audio/ogg", start_time=0)

                    with open("translated_pdf.mp3", "rb") as file_pdf:
                        st.download_button(
                            label="Download Translated PDF",
                            data=file_pdf,
                            file_name="translated_pdf.mp3",
                            mime="audio/ogg",
                        )

    collect_feedback()

if __name__ == "__main__":
    main()
