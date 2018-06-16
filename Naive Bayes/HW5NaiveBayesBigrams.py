import numpy as np
from collections import Counter

def get_data_from_file(name):
    flag = False

    # absolute path, should probably change in future
    filename = name
    while flag == False:
        try:
            infile = open(filename,"r")
            flag = True
        except:
            print("Filename not valid")
            filename = input("Enter filename: ")

    # read lines into list
    lst = infile.read().split("\n")
    infile.close()

    # Replace line with list of elements in line
    for i in range(0,len(lst)-1):
        lst[i] = [str(e) for e in lst[i].split(" ")]


    for i in range(0,len(lst)-1):
        lst[i].remove("<eol>")

    new_lst = []
    for i in range(0,len(lst)-1):
        sentence = []
        for j in range(len(lst[i])-1):
            token = lst[i][j] + " " + lst[i][j+1]
            sentence.append(token)
        new_lst.append(sentence)


    # returns file data in list
    return new_lst

# class C = Macbeth, Hamlet, Romeo, Juliet
# evidence E = < word1, word2, ..., wordn >
# calculate P(C|E)
def main():
    hamlet_test = get_data_from_file("data/Testing Files/hamlet_test.txt")
    juliet_test = get_data_from_file("data/Testing Files/juliet_test.txt")
    macbeth_test = get_data_from_file("data/Testing Files/macbeth_test.txt")
    romeo_test = get_data_from_file("data/Testing Files/romeo_test.txt")

    hamlet_train = get_data_from_file("data/Training Files/hamlet_train.txt")
    juliet_train = get_data_from_file("data/Training Files/juliet_train.txt")
    macbeth_train = get_data_from_file("data/Training Files/macbeth_train.txt")
    romeo_train = get_data_from_file("data/Training Files/romeo_train.txt")

    # ------------------------------------------------
    # Training
    # ------------------------------------------------

    hamlet_list = []
    for line in hamlet_train:
        for word in line:
            hamlet_list.append(word)

    juliet_list = []
    for line in juliet_train:
        for word in line:
            juliet_list.append(word)

    macbeth_list = []
    for line in macbeth_train:
        for word in line:
            macbeth_list.append(word)

    romeo_list = []
    for line in romeo_train:
        for word in line:
            romeo_list.append(word)

    # ------------------------------------------------
    # (num times word is seen in a file)/(length of file)
    # P(xi|wj)
    # ------------------------------------------------

    hamlet_count = Counter(hamlet_list)
    hamlet_set = set(hamlet_list)

    juliet_count = Counter(juliet_list)
    juliet_set = set(juliet_list)

    macbeth_count = Counter(macbeth_list)
    macbeth_set = set(macbeth_list)

    romeo_count = Counter(romeo_list)
    romeo_set = set(romeo_list)

    # ------------------------------------------------
    # (num lines in file)/(total num lines)
    # P(wj)
    # ------------------------------------------------

    tot_lines = len(hamlet_train) + len(juliet_train) + len(macbeth_train) + len(romeo_train)

    hamlet_w = len(hamlet_train)/tot_lines
    juliet_w = len(juliet_train)/tot_lines
    macbeth_w = len(macbeth_train)/tot_lines
    romeo_w = len(romeo_train)/tot_lines

    # ------------------------------------------------
    # Testing
    # -----------------------------------------------

    # ------------------------------------------------
    # product(P(xi|wj)) of all xi in the line for each class wj
    # ------------------------------------------------

    correct = 0
    hamlet_correct = 0
    juliet_correct = 0
    macbeth_correct = 0
    romeo_correct = 0

    for line in hamlet_test:
        hamlet_test_freq = []
        juliet_test_freq = []
        macbeth_test_freq = []
        romeo_test_freq = []
        for word in line:
            hamlet_test_freq.append(hamlet_count[word]/len(hamlet_list))
            juliet_test_freq.append(juliet_count[word]/len(juliet_list))
            macbeth_test_freq.append(macbeth_count[word]/len(macbeth_list))
            romeo_test_freq.append(romeo_count[word]/len(romeo_list))

        hamlet_prod = 1
        for freq in hamlet_test_freq:
            hamlet_prod *= (freq)

        juliet_prod = 1
        for freq in juliet_test_freq:
            juliet_prod *= (freq)

        macbeth_prod = 1
        for freq in macbeth_test_freq:
            macbeth_prod *= (freq)

        romeo_prod = 1
        for freq in romeo_test_freq:
            romeo_prod *= (freq)

        # ------------------------------------------------
        # Multiply product with P(wj) for each class wj
        # ------------------------------------------------

        hamlet_test_w =  hamlet_prod * hamlet_w
        juliet_test_w =  juliet_prod * juliet_w
        macbeth_test_w = macbeth_prod * macbeth_w
        romeo_test_w =  romeo_prod * romeo_w

        # ------------------------------------------------
        # Choose max(wj)
        # ------------------------------------------------

        wjs = [hamlet_test_w,juliet_test_w,macbeth_test_w,romeo_test_w]
        wj = max(wjs)
        if wjs.index(wj) == 0:
            correct += 1
            hamlet_correct += 1

    for line in juliet_test:
        hamlet_test_freq = []
        juliet_test_freq = []
        macbeth_test_freq = []
        romeo_test_freq = []
        for word in line:
            hamlet_test_freq.append(hamlet_count[word]/len(hamlet_list))
            juliet_test_freq.append(juliet_count[word]/len(juliet_list))
            macbeth_test_freq.append(macbeth_count[word]/len(macbeth_list))
            romeo_test_freq.append(romeo_count[word]/len(romeo_list))

        hamlet_prod = 1
        for freq in hamlet_test_freq:
            hamlet_prod *= (freq)

        juliet_prod = 1
        for freq in juliet_test_freq:
            juliet_prod *= (freq)

        macbeth_prod = 1
        for freq in macbeth_test_freq:
            macbeth_prod *= (freq)

        romeo_prod = 1
        for freq in romeo_test_freq:
            romeo_prod *= (freq)

        # ------------------------------------------------
        # Multiply product with P(wj) for each class wj
        # ------------------------------------------------

        hamlet_test_w =  hamlet_prod * hamlet_w
        juliet_test_w =  juliet_prod * juliet_w
        macbeth_test_w = macbeth_prod * macbeth_w
        romeo_test_w =  romeo_prod * romeo_w

        # ------------------------------------------------
        # Choose max(wj)
        # ------------------------------------------------

        wjs = [hamlet_test_w,juliet_test_w,macbeth_test_w,romeo_test_w]
        wj = max(wjs)
        if wjs.index(wj) == 1:
            correct += 1
            juliet_correct += 1

    for line in macbeth_test:
        hamlet_test_freq = []
        juliet_test_freq = []
        macbeth_test_freq = []
        romeo_test_freq = []
        for word in line:
            hamlet_test_freq.append(hamlet_count[word]/len(hamlet_list))
            juliet_test_freq.append(juliet_count[word]/len(juliet_list))
            macbeth_test_freq.append(macbeth_count[word]/len(macbeth_list))
            romeo_test_freq.append(romeo_count[word]/len(romeo_list))

        hamlet_prod = 1
        for freq in hamlet_test_freq:
            hamlet_prod *= (freq)

        juliet_prod = 1
        for freq in juliet_test_freq:
            juliet_prod *= (freq)

        macbeth_prod = 1
        for freq in macbeth_test_freq:
            macbeth_prod *= (freq)

        romeo_prod = 1
        for freq in romeo_test_freq:
            romeo_prod *= (freq)

        # ------------------------------------------------
        # Multiply product with P(wj) for each class wj
        # ------------------------------------------------

        hamlet_test_w =  hamlet_prod * hamlet_w
        juliet_test_w =  juliet_prod * juliet_w
        macbeth_test_w = macbeth_prod * macbeth_w
        romeo_test_w =  romeo_prod * romeo_w

        # ------------------------------------------------
        # Choose max(wj)
        # ------------------------------------------------

        wjs = [hamlet_test_w,juliet_test_w,macbeth_test_w,romeo_test_w]
        wj = max(wjs)
        if wjs.index(wj) == 2:
            correct += 1
            macbeth_correct += 1

    for line in romeo_test:
        hamlet_test_freq = []
        juliet_test_freq = []
        macbeth_test_freq = []
        romeo_test_freq = []
        for word in line:
            hamlet_test_freq.append(hamlet_count[word]/len(hamlet_list))
            juliet_test_freq.append(juliet_count[word]/len(juliet_list))
            macbeth_test_freq.append(macbeth_count[word]/len(macbeth_list))
            romeo_test_freq.append(romeo_count[word]/len(romeo_list))

        hamlet_prod = 1
        for freq in hamlet_test_freq:
            hamlet_prod *= (freq)

        juliet_prod = 1
        for freq in juliet_test_freq:
            juliet_prod *= (freq)

        macbeth_prod = 1
        for freq in macbeth_test_freq:
            macbeth_prod *= (freq)

        romeo_prod = 1
        for freq in romeo_test_freq:
            romeo_prod *= (freq)

        # ------------------------------------------------
        # Multiply product with P(wj) for each class wj
        # ------------------------------------------------

        hamlet_test_w =  hamlet_prod * hamlet_w
        juliet_test_w =  juliet_prod * juliet_w
        macbeth_test_w = macbeth_prod * macbeth_w
        romeo_test_w =  romeo_prod * romeo_w

        # ------------------------------------------------
        # Choose max(wj)
        # ------------------------------------------------

        wjs = [hamlet_test_w,juliet_test_w,macbeth_test_w,romeo_test_w]
        wj = max(wjs)
        if wjs.index(wj) == 3:
            correct += 1
            romeo_correct += 1

    print("Hamlet accuracy: ",round(100*hamlet_correct/len(hamlet_test),2),"%")
    print("Juliet accuracy: ",round(100*juliet_correct/len(juliet_test),2),"%")
    print("Macbeth accuracy: ",round(100*macbeth_correct/len(macbeth_test),2),"%")
    print("Romeo accuracy: ",round(100*romeo_correct/len(romeo_test),2),"%")
    print("Total accuracy: ",round(100*correct/(len(hamlet_test)+len(juliet_test)+len(macbeth_test)+len(romeo_test)),2),"%")

main()
