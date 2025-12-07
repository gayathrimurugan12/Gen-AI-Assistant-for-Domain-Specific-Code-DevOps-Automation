"""
Module: code_generator.py
Purpose: Generate domain-specific boilerplate code from the dataset.
"""

import json
import os

# Load dataset
DATASET_PATH = os.path.join(os.path.dirname(__file__), "../dataset/dataset.json")
with open(DATASET_PATH, "r") as file:
    DATASET = json.load(file)

def generate_boilerplate(project_type):
    """
    Returns the boilerplate code for the given project type.
    """
    key = project_type.lower().replace(" ", "_")
    project = DATASET.get(key)
    if project and project.get("boilerplate"):
        return project["boilerplate"]
    return f"# No boilerplate code found for '{project_type}'."
