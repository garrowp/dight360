from nltk.book import *


text_list = [text1, text2, text3, text4, text5, text6, text7, text8, text9]

for text in text_list:
    print(text.name, len(set(text)) / len(text), sep='\t')