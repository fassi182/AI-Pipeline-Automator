import json
import streamlit as st

st.set_page_config(
    page_title="AI Pipeline Evaluation Dashboard",
    layout="wide",
)

st.title("📊 AI Pipeline Evaluation Dashboard")

# -----------------------
# Load Results
# -----------------------

with open("evaluation/results/baseline.json") as file:
    baseline = json.load(file)

with open("evaluation/results/latest.json") as file:
    latest = json.load(file)

# -----------------------
# Overall Metrics
# -----------------------

st.header("Overall Evaluation")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Task Similarity",
    f"{latest['task_similarity']:.2f}%",
    delta=f"{latest['task_similarity']-baseline['task_similarity']:.2f}%"
)

col2.metric(
    "Keyword Overlap",
    f"{latest['keyword_overlap']:.2f}%",
    delta=f"{latest['keyword_overlap']-baseline['keyword_overlap']:.2f}%"
)

col3.metric(
    "Assignment Accuracy",
    f"{latest['assignment_accuracy']:.2f}%",
    delta=f"{latest['assignment_accuracy']-baseline['assignment_accuracy']:.2f}%"
)

st.divider()

st.subheader("Overall Score")

st.metric(
    "Current Overall Score",
    f"{latest['overall_score']:.2f}%",
    delta=f"{latest['overall_score']-baseline['overall_score']:.2f}%"
)

st.progress(latest["overall_score"] / 100)

st.divider()

st.subheader("Story-wise Comparison")

baseline_stories = {story["story_id"]: story for story in baseline["stories"]}
latest_stories = {story["story_id"]: story for story in latest["stories"]}
all_story_ids = sorted(set(baseline_stories) | set(latest_stories))

rows = []
for story_id in all_story_ids:
    base = baseline_stories.get(
        story_id,
        {
            "task_similarity": None,
            "keyword_overlap": None,
            "assignment_accuracy": None,
        },
    )
    new = latest_stories.get(
        story_id,
        {
            "task_similarity": None,
            "keyword_overlap": None,
            "assignment_accuracy": None,
        },
    )

    rows.append(
        {
            "Story": story_id,
            "Task (Old)": base["task_similarity"],
            "Task (New)": new["task_similarity"],
            "Keyword (Old)": base["keyword_overlap"],
            "Keyword (New)": new["keyword_overlap"],
            "Assignment (Old)": base["assignment_accuracy"],
            "Assignment (New)": new["assignment_accuracy"],
        }
    )

st.table(rows)