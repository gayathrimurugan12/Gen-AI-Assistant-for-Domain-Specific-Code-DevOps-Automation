"""
Module: test_generator.py
Purpose: Generate test cases from the dataset.
"""

import json
import os

DATASET_PATH = os.path.join(os.path.dirname(__file__), "../dataset/dataset.json")
with open(DATASET_PATH, "r") as file:
    DATASET = json.load(file)

def generate_tests(project_type):
    key = project_type.lower().replace(" ", "_")
    project = DATASET.get(key)
    if project and project.get("test"):
        return project["test"]
    return f"# No test cases found for '{project_type}'."
