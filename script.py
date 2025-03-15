# Fix the function so it handles empty names gracefully. Add an additional function to display a farewell message.

def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}! Welcome to the GitHub Collaboration Challenge."

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
