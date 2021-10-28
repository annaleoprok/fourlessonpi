text = input().split()
text[0], text[-1] = text[-1], text[0]
print(' '.join(text))