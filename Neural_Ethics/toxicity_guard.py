"""AI Toxicity Guard v1.0
Filters unethical content from neural responses."""
import re

def clean_response(text):
    prohibited = ['toxic_word1', 'harm_intent', 'bias_alpha']
    for word in prohibited:
        text = text.replace(word, '[REDACTED]')
    return text

print('Ethics Filter Active.')