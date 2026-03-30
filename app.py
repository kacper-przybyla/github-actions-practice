def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}!"

def is_positive(n):
    return n > 0

if __name__ == "__main__":
    print("Hello from a containerized Python app!")
    print("This image was built by GitHub Actions.")
    print(greet("World"))