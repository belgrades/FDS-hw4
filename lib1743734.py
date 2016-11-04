def jaccard(s1, s2):
    return len(s1.intersection(s2))*1.0/len(s1.union(s2))

def is_separator(char):
    # TODO: add ene.
    # TODO: check for special quotes.
    separators = ['<','>','/','?',';',':',',','.','"','','','','','','',]
    return char in separators

def remove_punctuation(line):
    last = 'normal'
    exit = ''
    while line:
        print(line)
        if is_separator(line[0]):
            print(line[0], ' is separator')
            last = 'separator'
        else:
            print(last)
            exit = exit+line[0] if last=='normal' else exit+' '+line[0]
            last = 'normal'
        line = line[1:]
    return exit   
     
word = "fer.,.,.,.nand-.-.-do"

print(remove_punctuation(word))
