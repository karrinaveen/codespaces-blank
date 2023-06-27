# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            temp = Bracket(next,i)
            opening_brackets_stack.append(temp)

        if next in ")]}":
            # Process closing bracket, write your code here
            if are_matching(opening_brackets_stack.pop().char,next):
                pass
            else:
                return i+1
    if len(opening_brackets_stack)==0:
        return "Success"
    else:
        return opening_brackets_stack[0].position+1   


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
