# import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
def sentence_tokenization_demo():
    text = "NLTK is a great tool for NLP. It simplifies text processing!"
    # Word Tokenization
    words = word_tokenize(text)
    print("Words:", words)

def main():
    sentence_tokenization_demo()

if __name__=="__main__":
    main()