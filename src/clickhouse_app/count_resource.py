from typing import Sequence


def words_counter_full(data: Sequence[Sequence]) -> dict:
    """Возвращает словарь, где ключ - слово, значение - количество слов в data"""
    result = {}
    for items in data:
        for word in items[0].lower().split():
            if word.isalpha() is False or len(word) < 4:
                continue
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    return result


def words_counter_top_100(data: dict) -> dict:
    """Возвращает отсортированный словарь с 100 наиболее популярных слов"""
    data_with_count = words_counter_full(data)
    result_data = sorted(data_with_count.items(), key=lambda item: item[1], reverse=True)
    return dict(result_data[:100])
