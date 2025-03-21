import spacy
from spacy.cli.download import download
download("en_core_web_sm", direct=True)

nlp = spacy.load('en_core_web_sm')
print("Model loaded successfully!")