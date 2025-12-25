LANGUAGES = {
    "python": ["python", "py"],
    "c": ["c language", "c"],
    "java": ["java"]
}

def extract_language(user_input: str):
    user_input = user_input.lower()
    for lang, keys in LANGUAGES.items():
        for k in keys:
            if k in user_input:
                return lang
    return "python"


def extract_project_type(user_input: str, dataset: dict):
    user_input = user_input.lower()
    for project in dataset.keys():
        if project.replace("_", " ") in user_input or project in user_input:
            return project
    return None
