from config import MODEL_URL

def check_local_model():

    if MODEL_URL.startswith("http://localhost"):
        return True

    return False