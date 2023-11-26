import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
nltk.download('punkt')
nltk.download('stopwords')

def summarizer(input_text,summ_size):
    print(type(summ_size))
    def sentence_similarity(line1, line2, stopwords=None):
        if stopwords is None:
            stopwords = set()

        words1 = [word.lower() for word in line1 if word.lower() not in stopwords]
        words2 = [word.lower() for word in line2 if word.lower() not in stopwords]

        all_words = list(set(words1 + words2))

        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)

        for word in words1:
            vector1[all_words.index(word)] += 1

        for word in words2:
            vector2[all_words.index(word)] += 1

        return 1 - cosine_distance(vector1, vector2)

    def build_similarity_matrix(sentences, stopwords):
        similarity_matrix = np.zeros((len(sentences), len(sentences)))
        for i in range(len(sentences)):
            for j in range(len(sentences)):
                if i != j:
                    similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j], stopwords)
        return similarity_matrix

    #Generting summary
    sentences = nltk.sent_tokenize(input_text)
    stop_words = set(stopwords.words('english'))
    sentence_similarity_matrix = build_similarity_matrix(sentences, stop_words)
    sentence_similarity_scores = np.sum(sentence_similarity_matrix, axis=1)
    ranked_sentences = [sentence for _, sentence in sorted(zip(sentence_similarity_scores, sentences), reverse=True)[:summ_size]]
    summary = ' '.join(ranked_sentences)
    return summary,input_text,len(input_text.split(' ')),len(summary.split(' '))