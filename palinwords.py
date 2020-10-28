
text = 'AMUMA' # '''MOEILIJKHEDEN INVOER
# VERNEDEREN
# AMUMA AMAMA MUMMUM
# AMATRAMA AAAA
# ABATRABAR
#DUMMY
# WORDS'''

text = text.split('\n')
words = []
for line in text:
    words = words + line.split()

for word in words:
    length = len(word)
    parts = [];
    for index in range(1, length -1):
        far = 1
        while far <= index and far <= length - index - 1:
            part = word[index - far:index + far + 1]
            if not part in parts:
                parts.append(word[index - far:index + far + 1])
            if (index + far + 2 < length):
                part = word[index - far:index + far + 2]
                if not part in parts:
                    parts.append(part)
            if (index - far -1 > 0):
                part = word[index - far -1:index + far +1]
                if not part in parts:
                    parts.append(part)
            far += 1
        print()
    print(parts)
    palinwords = 0
    for part in parts:
        length = len(part)
        if length % 2 == 0:
            for far in range(0, length // 2):                
                if part[far] == part[length - far - 1]:
                    palinwords += 1
        else:
            for far in range(0, length + 1 // 2):                
                if part[far] == part[length - far - 1]:
                    palinwords += 1
    print(palinwords)
              
        
        

