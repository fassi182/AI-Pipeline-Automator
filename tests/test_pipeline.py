import json

from Ai_pipeline import run_pipeline


def test_pipeline_runs():

    with open("golden_set/stories.json", "r") as file:
        stories = json.load(file)

    for story in stories:

        output = run_pipeline(story["user_story"])

        assert output is not None
        assert isinstance(output, dict)