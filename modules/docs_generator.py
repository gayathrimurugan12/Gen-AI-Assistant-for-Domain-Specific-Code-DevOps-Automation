"""
Module: docs_generator.py
Purpose: Generate documentation from the dataset.
"""

import json
import os

DATASET_PATH = os.path.join(os.path.dirname(__file__), "../dataset/dataset.json")
with open(DATASET_PATH, "r") as file:
    DATASET = json.load(file)

def generate_docs(project_type):
    key = project_type.lower().replace(" ", "_")
    project = DATASET.get(key)
    if project and project.get("docs"):
        return project["docs"]
    return f"# No documentation found for '{project_type}'."
