#word_file = open('CROSSWD.txt','r') #pay attention to where it is. ,'w'is writing mode, 'a' append mode that adds to the end to a file, 'r' is read mode
#print(type(word_file))
#print([x for x in dir(word_file) if '_' != x[0]]) #return x for data if _ is not the first character in x

#data = [1,2,3,8,5,6,10]
#print([2*x for x in data if x % 2 == 0]) #2,4,6,10 way to get particular data
#words= [] #empty list
#for line in word_file:
    #print(line)
#    print(line.strip()) #removes the extra char
#    words.append(line)

#print (words)
#while True:
#    print(word_file.readline()) #will keep attempting to read line even when running out of lines in the txt be specific 
#print(word_file.readline()) #reads the next line in crosswd so aa
#print(word_file.readline())



def more_than_20(file):
    words = []
    data = open (file, 'r') #can open file by providing name
    #for word in data: #itrate data using for loops
    #    if len(word.strip()) > 20:
        #    print(word.strip()) #f strip is not used the spaced lines would reamain
    #        words.append(word.strip())
    words = [x.strip() for x in data if len(x.strip()) > 20] #go through all x of data to see if it is greater than 20
    return words
#print(more_than_20('CROSSWD.txt')) #contains a list now


def has_no_e(word): 
    for x in word: #variable t or f to see if we encounter an e
        if 'e' in word:
            return False
        else:
            return True

#print(has_no_e(bear))

#for letter in word:
    #if 'e' == letter:
        #check = False
    #return check



def uses_only(word,letters): #only uses the letters for that word
    for x in word:
        if x not in letters:
            return False
    return True

#print(uses_only('abracadacra','abr'))


def all_uses_only(file, letters):
    with open(file, 'r') as f:
        words = f.read().splitlines()

    return [word for word in words if uses_only(word, letters)]
#print(all_uses_only('CROSSWD.txt', 'abc'))