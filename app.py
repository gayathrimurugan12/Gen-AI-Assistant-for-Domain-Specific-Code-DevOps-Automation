from flask import Flask, render_template, request
from modules.code_generator import generate_boilerplate
from modules.test_generator import generate_tests
from modules.docs_generator import generate_docs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = {}
    if request.method == "POST":
        project_type = request.form.get("project_type")
        result["code"] = generate_boilerplate(project_type)
        result["tests"] = generate_tests(project_type)
        result["docs"] = generate_docs(project_type)
        result["project_type"] = project_type
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
