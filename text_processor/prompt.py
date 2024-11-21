PROMPT = """Given the following text: {text} \nI want you to select words that must be emphasized when being spoken to achieve a more natural prosody. There can be multiple words, there can be one word or there can be no words to emphasized. When a word is selected to be emphasized, add square brackets around the word. If the word is next to a punctuation like comma, period, etc, only add the square brackets around the word not the punctuation. Take a look at the following example say you responded with "He is staying in Paris." and let "Paris" be the word to be emphasized, you want to return "He is staying in [Paris]." instead of "He is staying in [Paris.]"
There will also be words with special tags/words surrounded by angle brackets like <sound_scrolling_2> or <wave> that are not words but are part of the sentence. If a word is part of a special tag, do not emphasize it.
Return the result in the following JSON format: {{"emphasized_sentence": "[emphasized_sentence]"}}"""

