
def word_replace( ):
    
    str = 'Hi, I am Yero, let me to tell you ...'
    word_to_replace = input('Enter the word to replace: ')
    word_replacement = input('Enter the word replacement: ')
    print(str.replace(word_to_replace, word_replacement))
    
print(word_replace())