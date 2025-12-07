from modules.code_generator import generate_code
from modules.test_generator import generate_tests
from modules.docs_generator import generate_docs

def main():
    print("\n=== AI Code Assistant ===")
    print("Available domains: Calculator, REST API, Chatbot, ML Model")

    project = input("\nEnter your project type: ")

    print("\n----- Generated Code -----\n")
    print(generate_code(project))

    print("\n----- Generated Tests -----\n")
    print(generate_tests(project))

    print("\n----- Generated Docs -----\n")
    print(generate_docs(project))

    print("\n✔ Program Finished Successfully!")

if __name__ == "__main__":
    main()
