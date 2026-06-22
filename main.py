#text = "Hello world, hello everyone!"
from typing import Dict


def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def group_words(text: str) -> Dict[str, int]:
    words = text.lower().split()
    word_count: Dict[str, int] = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

counted_words = count_words("Hello world, hello everyone!")

print(f"counted_words = {counted_words}")

grouped_words = group_words("thE Cat sat on THE MAt the cAt ran tHe doG ran")

print(f"cat = {grouped_words["cat"]}", end="\n\n")

print(f"grouped_words = {grouped_words}")