"""
Module: docs_generator.py
Purpose: Generate documentation from the dataset for multiple languages.
"""

import json
import os

DATASET_PATH = os.path.join(os.path.dirname(__file__), "../dataset/dataset.json")
with open(DATASET_PATH, "r") as file:
    DATASET = json.load(file)

def generate_docs(project_type, language="python"):
    key = project_type.lower().replace(" ", "_")
    project = DATASET.get(key)
    if project and project.get("docs"):
        return project["docs"].get(language.lower(), f"# No docs found for {language}")
    return f"# No documentation found for '{project_type}'."
