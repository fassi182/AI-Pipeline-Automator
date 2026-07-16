import json

from Ai_pipeline import run_pipeline
from modules.assignment import assign_tasks
from evaluation.scoring import (
    task_count_similarity,
    keyword_overlap,
    assignment_accuracy,
)

# Load the Golden Set
with open("golden_set/stories.json", "r") as file:
    stories = json.load(file)

total_task_score = 0
total_keyword_score = 0
total_assignment_score = 0

print("=" * 50)
print("Running First Evaluation Pass")
print("=" * 50)

for story in stories:

    user_story = story["user_story"]

    expected_requirements = story["expected_requirements"]
    expected_assignments = story["expected_assignments"]

    # Run AI Pipeline (M1)
    generated_requirements = run_pipeline(user_story)

    # Run Assignment Engine (M4)
    generated_assignments = assign_tasks(generated_requirements)

    # Evaluate M1
    task_score = task_count_similarity(
        expected_requirements,
        generated_requirements,
    )

    keyword_score = keyword_overlap(
        expected_requirements,
        generated_requirements,
    )

    # Evaluate M4
    assignment_score = assignment_accuracy(
        expected_assignments,
        generated_assignments,
    )

    total_task_score += task_score
    total_keyword_score += keyword_score
    total_assignment_score += assignment_score

    print(f"\nStory ID: {story['id']}")
    print(f"Task Count Similarity : {task_score}%")
    print(f"Keyword Overlap       : {keyword_score}%")
    print(f"Assignment Accuracy   : {assignment_score}%")

number_of_stories = len(stories)

average_task_score = total_task_score / number_of_stories
average_keyword_score = total_keyword_score / number_of_stories
average_assignment_score = total_assignment_score / number_of_stories

print("\n" + "=" * 50)
print("Baseline Scores")
print("=" * 50)
print(f"Average Task Count Similarity : {average_task_score:.2f}%")
print(f"Average Keyword Overlap       : {average_keyword_score:.2f}%")
print(f"Average Assignment Accuracy   : {average_assignment_score:.2f}%")