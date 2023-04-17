# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_choice = input()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    if "I" in input_choice:
        pattern = input().rstrip()
        text = input().rstrip()
    elif "F" in input_choice:
        with open("tests/06","r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    else:
        print("wrong input")
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    pattern_hash = sum([ord(char) for char in pattern])
    text_hash = sum([ord(text[i]) for i in range(len(pattern))])

    occurrences = []

    for i in range(len(text)-len(pattern) + 1):
        if text_hash == pattern_hash and text[i:i+len(pattern)] == pattern:
            occurrences.append(i)
        if i < len(text) - len(pattern):
            text_hash = text_hash - ord(text[i]) + ord(text[i+len(pattern)])
    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

