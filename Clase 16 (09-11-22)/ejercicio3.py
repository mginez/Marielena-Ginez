

def reverse(word, len):
    if len == 0:
        return word[0]
    return  word[len] + reverse(word, len-1)

def main():

    word = input('Palabra: ')
    length = len(word) - 1
    print(reverse(word, length))

main()