text = input()
words = text.split()
start_with = ['http', 'https', 'www', 'WWW']
for word in words:
    # finish the code here
    if \
            word.startswith('https') or word.startswith('http') or word.startswith('www') or word.startswith('WWW') and word.count('.') >= 2:
        print(word)


# for word in input().split():
#     if word.lower().startswith(('https://', 'http://', 'www.')):
#         print(word)
