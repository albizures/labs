

in_file = open('in.txt', 'r')
out_file = open('out.txt', 'w')

text = in_file.read()

in_file.close()

lines = text.split('\n')
out_words = []


def is_palindrome(word):
    length = len(word)

    if length == 0 or length == 1:
        return True

    offset = 0

    while offset < length // 2:
        if word[offset] != word[-offset - 1]:
            return False
        offset += 1

    return True


# def is_paliword(word):
#     counter = 0
#     parts = get_word_parts(word)
#     print(parts)
#     for part in parts:
#         if len(part) > 2 and is_palindrome(part):
#             counter += 1

#     return counter > 1


def is_paliword(word):
    length = len(word)
    palindromes = []

    index = 1
    while index < length - 2:
        offset = 1
        while offset <= index and offset <= length - index - 1:
            start = index - offset
            end = index + offset + 1
            part = word[start:end]
            if is_palindrome(part):
                palindromes.append(word[start:end])
                break
            elif (end + 1 < length):
                part = word[start:end + 1]
                if is_palindrome(part):
                    palindromes.append(part)
                    break
            elif (start - 1 > 0):
                part = word[start - 1:end]
                if is_palindrome(part):
                    palindromes.append(part)
                    break

            offset += 1
        index += 1
    return len(palindromes) > 1


for line in lines:
    for word in line.split(' '):
        if is_paliword(word):
            out_words.append(word)


out_file.write('\n'.join(out_words))


out_file.close()
