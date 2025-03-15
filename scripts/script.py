# Fix the function so it handles empty names gracefully. Add an additional function to display a farewell message.

def greet(name):
    """Returns a greeting message."""
    if name == "":
        return "Hello, new user! Welcome to the Github Collaboration Challenge."
    else:
        return "Hello, " + name + ". Welcome to the GitHub Collaboration Challenge."
    
def goodbye(name):
    if name == "":
        return "Goodbye, new user. Hope to see you again soon!"
    else:
        return "Goodbye, " + name + ". Hope to see you again soon!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    print(goodbye(user_name)
