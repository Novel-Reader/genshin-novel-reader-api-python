"""Tag generation module for novel text."""

import re
from collections import Counter
from functools import lru_cache
from pathlib import Path

import jieba


STOPWORDS_PATH = Path(__file__).with_name("cn_stopwords.txt")
CUSTOM_TAGS = [
    "绫华", "凯亚", "琴", "丽莎", "迪卢克", "芭芭拉", "莫娜", "迪奥娜", "优菈", "米卡",
    "香菱", "魈", "胡桃", "云堇", "嘉明", "枫原万叶", "宵宫", "九条裟罗", "雷神", "雷电影",
    "心海", "荒泷一斗", "神子", "久岐忍", "鹿野院", "平藏", "多莉", "流浪者", "林尼", "琳妮特",
    "菲米尼", "芙宁娜", "娜维娅", "卡萨帕", "阿蕾奇诺", "三月七", "克拉拉",
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
