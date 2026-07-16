import json

from Ai_pipeline import run_pipeline
from evaluation.scoring import (
    task_count_similarity,
    keyword_overlap,
)


# Load the Golden Set
with open("golden_set/stories.json", "r") as file:
    stories = json.load(file)


total_task_score = 0
total_keyword_score = 0

print("=" * 50)
print("Running First Evaluation Pass")
print("=" * 50)

for story in stories:

    user_story = story["user_story"]

    expected = story["expected_requirements"]

    generated = run_pipeline(user_story)

    task_score = task_count_similarity(expected, generated)

    keyword_score = keyword_overlap(expected, generated)

    total_task_score += task_score
    total_keyword_score += keyword_score

    print(f"\nStory ID: {story['id']}")
    print(f"Task Count Similarity : {task_score}%")
    print(f"Keyword Overlap       : {keyword_score}%")

number_of_stories = len(stories)

average_task_score = total_task_score / number_of_stories
average_keyword_score = total_keyword_score / number_of_stories

print("\n" + "=" * 50)
print("Baseline Scores")
print("=" * 50)
print(f"Average Task Count Similarity : {average_task_score:.2f}%")
print(f"Average Keyword Overlap       : {average_keyword_score:.2f}%")