from modules.code_generator import generate_code
from modules.test_generator import generate_tests
from modules.docs_generator import generate_docs

def main():
    print("\n=== AI Code Assistant ===")
    print("Available projects: Calculator, REST API, Todo App, Weather App, Chatbot, Counter, Banking, Blog, Quiz, Currency Converter, Text Editor, Note App, Inventory, Password Checker, Email Sender, Number Guess Game")
    
    project = input("\nEnter your project type: ")
    language = input("Enter the programming language (python/c/java): ").lower()

    print("\n----- Generated Code -----\n")
    print(generate_code(project, language))

    print("\n----- Generated Tests -----\n")
    print(generate_tests(project, language))

    print("\n----- Generated Docs -----\n")
    print(generate_docs(project, language))

    print("\n✔ Program Finished Successfully!")

if __name__ == "__main__":
    main()
