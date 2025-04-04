def main():
    string = 'abcde'
    string = reverse_string(string)
    print (string)

class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def spop(self):
        return self.data.pop(len(self.data) - 1)

    def read(self):
        return self.data[len(self.data) - 1]

def reverse_string(string: str) -> str:
    stack = Stack()
    rstring = ""

    for letter in string:
        stack.push(letter)

    while (len(stack.data) > 0):
        rstring += stack.spop()

    return rstring

main()
    

    