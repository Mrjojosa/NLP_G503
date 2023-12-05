import streamlit as st
import whisper
import openai

st.title('Audio processor')

audioFile = st.file_uploader('Upload audio', type=['wav','mp3', 'm4a'])

model = whisper.load_model("base")

openai.api_key = "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"

st.header("Play original audio file")

st.audio(audioFile)

def click_button():
    st.write(summText["choices"][0]["text"])

if st.sidebar.button("Transcribe audio"):
    if audioFile is not None:
        st.sidebar.success("Transcribing audio")
        transcription = model.transcribe(audioFile.name)
        st.sidebar.success("Transcription complete")
        st.write(transcription["text"])
        textPrompt = "Summarize the following text " + transcription["text"]
        summText = openai.Completion.create(
            model = "text-davinci-003",
            prompt =  textPrompt,
            max_tokens = 1000
        )
        st.button('Show summarize', on_click=click_button)
    else:
        st.sidebar.error("Upload audio file")

