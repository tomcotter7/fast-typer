from PyPDF2 import PdfFileReader as reader
from google.cloud import texttospeech


def tts_text(text):
    client = texttospeech.TextToSpeechClient()
    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    # We can use wavenet voices using this parameter, name='en-GB-Wavenet-D'
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-GB", ssml_gender=texttospeech.SsmlVoiceGender.Male
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    return response


def create_audio(pdf_file, start_page_range, end_page_range):
    """Function to generate an .mp3 file for an input pdf

    Args:
        pdf_file (string): The input pdf filename
        page_range (range): The page range to ignore (could be a prelude for example).

    """
    read_Pdf = reader(open(pdf_file, 'rb'))
    pdf_text = ""
    for page in range(read_Pdf.numPages):
        if page not in start_page_range and page not in end_page_range:
            text = read_Pdf.getPage(page).extractText()
            pdf_text += text + "\n"
    pdf_text = [pdf_text[start:start+5000] for start in range(0, len(pdf_text), 5000)]
    responses = []
    for request in pdf_text:
        responses.append(tts_text(request).audio_content)
    response = b''.join(responses)
    with open("meditations.mp3", "wb") as out:
        out.write(response)
    # tts_text(pdf_text)

create_audio('meditations.pdf', range(3,73), range(282, 307))
