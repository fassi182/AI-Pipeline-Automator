import json
import os
import sys

# ----------------------------
# Choose which pipeline to run
# ----------------------------
if len(sys.argv) > 1:
    mode = sys.argv[1].lower()
else:
    mode = "baseline"

if mode == "baseline":
    from Ai_pipeline import run_pipeline
    output_file = "evaluation/results/baseline.json"

elif mode == "latest":
    from Ai_pipeline_v2 import run_pipeline
    output_file = "evaluation/results/latest.json"

else:
    print("Usage:")
    print("python -m evaluation.run_evaluation baseline")
    print("python -m evaluation.run_evaluation latest")
    sys.exit()

from modules.assignment import assign_tasks
from evaluation.scoring import (
    task_count_similarity,
    keyword_overlap,
    assignment_accuracy,
)

# ----------------------------
# Load Golden Set
# ----------------------------

with open("golden_set/stories.json", "r") as file:
    stories = json.load(file)

results = []

total_task = 0
total_keyword = 0
total_assignment = 0

print("=" * 50)
print(f"Running {mode.capitalize()} Evaluation")
print("=" * 50)

for story in stories:

    generated_requirements = run_pipeline(
        story["user_story"]
    )

    generated_assignments = assign_tasks(
        generated_requirements
    )

    task_score = task_count_similarity(
        story["expected_requirements"],
        generated_requirements,
    )

    keyword_score = keyword_overlap(
        story["expected_requirements"],
        generated_requirements,
    )

    assignment_score = assignment_accuracy(
        story["expected_assignments"],
        generated_assignments,
    )

    total_task += task_score
    total_keyword += keyword_score
    total_assignment += assignment_score

    results.append(
        {
            "story_id": story["id"],
            "task_similarity": task_score,
            "keyword_overlap": keyword_score,
            "assignment_accuracy": assignment_score,
        }
    )

number_of_stories = len(stories)

average_task = total_task / number_of_stories
average_keyword = total_keyword / number_of_stories
average_assignment = total_assignment / number_of_stories

overall = (
    average_task
    + average_keyword
    + average_assignment
) / 3

data = {
    "task_similarity": average_task,
    "keyword_overlap": average_keyword,
    "assignment_accuracy": average_assignment,
    "overall_score": overall,
    "stories": results,
}

os.makedirs("evaluation/results", exist_ok=True)

with open(output_file, "w") as file:
    json.dump(data, file, indent=4)

print("\nResults saved to:", output_file)