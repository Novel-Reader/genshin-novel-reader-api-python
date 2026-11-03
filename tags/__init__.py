"""Tag generation module for novel text."""

import re
from collections import Counter
from functools import lru_cache
from pathlib import Path

import jieba


STOPWORDS_PATH = Path(__file__).with_name("cn_stopwords.txt")
CUSTOM_TAGS_PATH = Path(__file__).with_name("game_role_tags.txt")
CUSTOM_TAGS = [
    line.strip()
    for line in CUSTOM_TAGS_PATH.read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.lstrip().startswith("#")
]


@lru_cache(maxsize=1)
def load_stopwords():
    with STOPWORDS_PATH.open(encoding="utf-8") as stopwords_file:
        return {line.strip() for line in stopwords_file if line.strip()}


def generate_tags(text, top_n=20):
    custom_tags = sorted(
        ((name, text.count(name)) for name in CUSTOM_TAGS if name in text),
        key=lambda item: item[1],
        reverse=True,
    )[:5]

    cleaned_text = re.sub(r"[^\w\s]", "", text)
    cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()
    words = (
        word.strip()
        for word in jieba.cut(cleaned_text)
    )
    filtered_words = [
        word for word in words if word and word not in load_stopwords() and len(word) > 1
    ]
    keywords = [word for word, _ in Counter(filtered_words).most_common(top_n)]

    tags = [name for name, _ in custom_tags] + keywords
    return ",".join(tags)[:50]
