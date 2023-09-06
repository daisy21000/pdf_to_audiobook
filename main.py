from pypdf import PdfReader
from gtts import gTTS

reader = PdfReader('Drift.pdf')
text = ''
for page in reader.pages:
    text += page.extract_text() + '\n'

tts = gTTS(text, lang='en')

tts.save('drift.mp3')
