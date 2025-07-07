from nltk.corpus import wordnet
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def expand_query_wordnet(query):
    synonyms = set()
    for word in query.split():
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if lemma.name() != word:
                    synonyms.add(lemma.name().replace('_', ' '))
    return list(synonyms)

def expand_query_semantic(query, top_k=3):
    query_vec = model.encode(query, convert_to_tensor=True)
    vocab = ['vehicle', 'automobile', 'car', 'bus', 'train', 'bike', 'airplane']
    vocab_vecs = model.encode(vocab, convert_to_tensor=True)
    scores = util.cos_sim(query_vec, vocab_vecs)[0]
    top_indices = scores.topk(k=top_k).indices
    return [vocab[i] for i in top_indices]
