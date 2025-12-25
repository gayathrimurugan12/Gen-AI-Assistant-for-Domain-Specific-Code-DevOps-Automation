from flask import Flask, render_template, request
from modules.code_generator import generate_code
from modules.test_generator import generate_tests
from modules.docs_generator import generate_docs
import json
import os
from difflib import get_close_matches

app = Flask(__name__)

# Load dataset
DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset/dataset.json")
with open(DATASET_PATH, "r") as f:
    DATASET = json.load(f)

AVAILABLE_PROJECTS = list(DATASET.keys())
SUPPORTED_LANGUAGES = ["python", "c", "java"]

def normalize_project_name(name):
    return name.strip().lower().replace(" ", "_")

def suggest_project(name):
    normalized = normalize_project_name(name)
    matches = get_close_matches(normalized, AVAILABLE_PROJECTS, n=3, cutoff=0.5)
    return matches

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        project_input = request.form.get("project_type", "")
        language = request.form.get("language", "python").strip().lower()
        if language not in SUPPORTED_LANGUAGES:
            language = "python"

        project_key = normalize_project_name(project_input)

        if project_key not in AVAILABLE_PROJECTS:
            suggestions = suggest_project(project_input)
            if suggestions:
                project_key = suggestions[0]  # take first suggestion
            else:
                project_key = None

        if project_key:
            code = generate_code(project_key, language)
            tests = generate_tests(project_key, language)
            docs = generate_docs(project_key, language)
            result = {
                "project_type": project_input.title(),
                "code": code,
                "tests": tests,
                "docs": docs
            }
        else:
            result = {
                "project_type": project_input.title(),
                "code": "# Project not found",
                "tests": "# Project not found",
                "docs": "# Project not found"
            }

    return render_template("index.html", result=result, languages=SUPPORTED_LANGUAGES)

if __name__ == "__main__":
    app.run(debug=True)
