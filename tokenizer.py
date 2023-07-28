from tensorflow.keras.preprocessing.text import Tokenizer

#Let's add custom sentences 
sentences = [
    "Apples are red",
    "Apples are round",
    "Oranges are round",
    "Grapes are green"
]

#Tokenize the sentences
myTokenizer = Tokenizer(num_words=100)
myTokenizer.fit_on_texts(sentences)
print(myTokenizer.word_index)