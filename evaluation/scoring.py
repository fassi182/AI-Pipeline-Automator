def task_count_similarity(expected, generated):

    expected_count = len(expected)
    generated_count = len(generated)

    score = min(expected_count, generated_count) / max(expected_count, generated_count)

    return round(score * 100, 2)


def keyword_overlap(expected, generated):

    expected_words = set()

    for sentence in expected:
        expected_words.update(sentence.lower().split())

    generated_words = set()

    for sentence in generated:
        generated_words.update(sentence.lower().split())

    common = expected_words.intersection(generated_words)

    score = len(common) / len(expected_words)

    return round(score * 100, 2)
def assignment_accuracy(expected, generated):

    correct = 0

    for e, g in zip(expected, generated):
        if e == g:
            correct += 1

    return round(correct / len(expected) * 100, 2)