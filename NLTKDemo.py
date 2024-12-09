
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
def sentence_tokenization_demo():
    print("word tokenization function:")
    text = "NLTK is a great tool for NLP. It simplifies text processing!"
    # Word Tokenization
    words = word_tokenize(text)
    print("Words:", words)

def stemming_demo():
    print("steming the words function:")
    stemmer = PorterStemmer()
    words = ["running", "ran", "runs", "easily", "fairly", "appreciation", "better", "Unfortunately", "simutaneously", "successfully"]
    stemmed_words = [stemmer.stem(word) for word in words]
    print("Stemmed Words:", stemmed_words)

def lemmatization_demo():
    print("lemmatization the words function:")
    lemmatizer = WordNetLemmatizer()
    words = ["running", "ran", "runs", "better", "easily"]
    lemmatized_words = [lemmatizer.lemmatize(word, pos="v") for word in words]
    print("Lemmatized Words:", lemmatized_words)

def part_of_speech_demo():
    print("part of speech demo")
    text = "NLTK helps in text processing"
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    print(f"POS Tags of sentence '{text}':\n{pos_tags}")
def main():
    sentence_tokenization_demo()
    stemming_demo()
    lemmatization_demo()
    part_of_speech_demo()
if __name__=="__main__":
    main()