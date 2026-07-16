from modules.decomposition import decompose_story


def test_output_is_list():

    result = decompose_story(
        "As a user I want to register using my email so that I can access the system."
    )

    assert isinstance(result, list)


def test_list_is_not_empty():

    result = decompose_story(
        "As a user I want to register using my email so that I can access the system."
    )

    assert len(result) > 0


def test_all_items_are_strings():

    result = decompose_story(
        "As a user I want to register using my email so that I can access the system."
    )

    for requirement in result:
        assert isinstance(requirement, str)


def test_requirements_are_not_empty():

    result = decompose_story(
        "As a user I want to register using my email so that I can access the system."
    )

    for requirement in result:
        assert requirement != ""