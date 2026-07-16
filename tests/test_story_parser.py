from modules.story_parser import parse_story


def test_output_is_dictionary():

    result = parse_story(
        "As a user I want to register using my email so that I can access the system."
    )

    assert isinstance(result, dict)


def test_required_fields_exist():

    result = parse_story(
        "As a user I want to register using my email so that I can access the system."
    )

    assert "actor" in result
    assert "action" in result
    assert "benefit" in result


def test_values_are_strings():

    result = parse_story(
        "As a user I want to register using my email so that I can access the system."
    )

    assert isinstance(result["actor"], str)
    assert isinstance(result["action"], str)
    assert isinstance(result["benefit"], str)


def test_values_are_not_empty():

    result = parse_story(
        "As a user I want to register using my email so that I can access the system."
    )

    assert result["actor"] != ""
    assert result["action"] != ""
    assert result["benefit"] != ""