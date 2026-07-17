from modules.monitoring import check_local_model

def test_model_is_local():
    assert check_local_model() is True