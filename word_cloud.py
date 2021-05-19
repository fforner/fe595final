from collections import Counter


def word_cloud_generator(text):
    stripped_text = []
    stripped_text = [word for word in text.split() if word.isalpha() and word.lower() not in open("stopwords.txt", "r").read() and len(word) >= 2]
    word_freqs = Counter(stripped_text)
    word_freqs = dict(word_freqs)
    word_freqs_js = []
    for key,value in word_freqs.items():
        temp = {"text": key, "size": value}
        word_freqs_js.append(temp)

    max_freq = max(word_freqs.values())
    return word_freqs_js,max_freq
