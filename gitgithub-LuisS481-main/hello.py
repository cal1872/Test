import random

def hello():
    return random.choice(['Hello, world!', 'Hello, Python!'])

if __name__ == '__main__':
    print(hello())