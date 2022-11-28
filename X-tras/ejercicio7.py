words = input('Please enter the words separated by commas: ')
word_list = words.split(',')
reference_word = word_list[0]
count = 0
prefix = []
len_list = 0
len_list = len(reference_word)
for word in word_list[:1]:
    for letter in word:
        try:
            if letter == reference_word[count]:
                prefix.append(letter)
            else:
                if len_list > count:
                    len_list = count 
                break
        except:
            break
        count += 1
    count = 0      
for p in range(0, len_list):
    print(prefix[p], end ='')

