my_str ='пишите код так, как будто сопровождать его будет склонный к насилию психопат, который, знает где вы живете.'
print(my_str)
print(my_str.islower())
print(my_str.isupper())
print(my_str.istitle())

if my_str.islower(): my_str.capitalize()
print(my_str.capitalize())

print(my_str.find('сопровождать'))
print(my_str.index('сопровождать'))
print(my_str.find('сопровождаff'))

print(my_str.replace('сопровождать', 'поддерживать'))
lst = my_str.split(',')
print(lst)
print(','.join(lst))