#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      toh
#
# Created:     04/02/2015
# Copyright:   (c) toh 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from pprint import pprint
from random import randint

def main():
    t = {i for i in range(99) if (i%2 != 0)}
    t = {i for i in range(1,100) if (i%2 != 0)}
    L= ['A','B','C','D','E']
    t= zip(range(0,5),L)
    for i in t:
        pprint(i)
    pprint(t)

    A = [10, 25, 40]
    B = [1, 15, 20]
    list_sum_zip = [ x[0]+x[1] for x in zip(A,B)]
    pprint(list_sum_zip)
    dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
    #k = 'Bilbo'
    k = 'Frodo'
    #Replace [...] with a one-line comprehension
    #value_list_modified_1 = [x[k] for x in dlist]# <-- Use the same expression here
    k = 'Frodo'
    value_list_modified_2 = [x[k] if k in x else 'NOT PRESENT' for x in dlist] # <-- as you do here
    #pprint(value_list_modified_1)
    pprint(value_list_modified_2)
    mydict = {'Neo':'Keanu','Morpheus':'Laurence','Trinity':'Carrie-Anne'}
    mydict['Neo'] if 'Neo' in mydict else 'NOT PRESENT'

    r = range(100)
    pprint(r)
    for i in r:
        print(i)

    square_dict = {x:x**2 for x in range(0,100)}
    pprint(square_dict)
    D = {'red','white','blue'}
    # Replace {...} with a one-line dictionary comprehension
    identity_dict = {v:v for v in D}

    base = 10
    digits = set(range(base))
    pprint(digits)
    id2salary = {0:1000.0, 1:1200.50, 2:990}
    names = ['Larry', 'Curly', 'Moe']
    # Replace { ... } with a one-line dictionary comprehension that uses id2salary and names.
    listdict2dict = { names[k]:v for(k,v) in id2salary.items() }
    pprint(listdict2dict)


def nextInts(L): return [ x+1 for x in L ]


def main2():
    a=1
    b=10
    v = randint(a,b)
    for i in range(1,10):
        v = randint(a,b)
        pprint(v)
    #print(movie_review(""))
    #print(movie_review(""))
    #print(movie_review(""))
    print(["See it!", "A gem!", "Ideological claptrap!"][2])


def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    return ["See it!", "A gem!", "Ideological claptrap!"][randint(0,2)];

## 2: (Task 2) Make Inverse Index
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.
    Distinguish between an occurence of a string (e.g. "use") in the document as a word
    (surrounded by spaces), and an occurence of the string as a substring of a word (e.g. "because").
    Only the former should be represented in the inverse index.
    Feel free to use a loop instead of a comprehension.

    Example:
    >>> makeInverseIndex(['hello world','hello','hello cat','hellolot of cats']) == {'hello': {0, 1, 2}, 'cat': {2}, 'of': {3}, 'world': {0}, 'cats': {3}, 'hellolot': {3}}
    True
    """
    mydict = {};
    for (i,s) in enumerate(strlist):
       for y in s.split():
        if mydict.get(y) != None:
            mydict[y].add(i);
        else:
            mydict[y] = {i}
    return mydict


## 4: (Task 4) And Search
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    Feel free to use a loop instead of a comprehension.

    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> andSearch(idx, ['Johann', 'the'])
    {2, 3}
    >>> andSearch(idx, ['Johann', 'Bach'])
    {0, 4}
    """
    doc_set = set()
    for x in query:
        if inverseIndex.get(x) != None:
            pprint(x)
            pprint(doc_set)
            if len(doc_set) != 0:
                doc_set = (doc_set.intersection(inverseIndex[x]))
            else:
                doc_set.update(inverseIndex[x])

    return doc_set

def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    '''
    len_of_list = len(A)
    list = []
    for x in range(len_of_list):
        list.append((A[x][0]+B[x][0],A[x][1]+B[x][1]))
    return list

## 3: (Problem 3) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    list = []
    for x in range(p,p+n):
        list.append(x)
    return list


## 1: (Problem 1) Python Comprehensions: Filtering
def myFilter(L, num):
    '''
    Input:
      -L: a list of numbers
      -num: a number
    Output:
      -a list of numbers not containing a multiple of num
    Examples:
      >>> myFilter([1,2,4,5,7],2)
      [1, 5, 7]
      >>> myFilter([10,15,20,25],10)
      [15, 25]
    '''
    #list = []
    #for x in L:
        #if x%num > 0:
            #list.append(x)

    #return list
    return [x for x in L if (x%num > 0)]


def my_lists(L):
    '''
    >>> my_lists([1,2,4])
    [[1], [1, 2], [1, 2, 3, 4]]
    >>> my_lists([0,3])
    [[], [1, 2, 3]]
    '''
    m_list = []
    for x in L:
        if x == 0:
            m_list.append([])
        else:
            m_list.append([y for y in range(1,x+1)])

    return m_list

## 3: (Problem 3) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    list = []
    for x in range(p,p+n):
        list.append(x)
    return list


if __name__ == '__main__':
    #main()
    main2()
    li = [1,2,3]
    pprint(nextInts(li))
    pprint(list(enumerate(['A','B','C'])))
    dict = {'a':'a'}
    print(type(dict))
    print( dict.get('b'))
    pprint(andSearch(makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach']),['Johann', 'the']))
    print(tuple_sum([(1,2), (10,20)],[(3,4), (30,40)]))
    pprint(row(10,4))
    #print(row(p=10))
    print(my_lists([1,2,4]))

    base = 10
    digits = set(range(base))
    print(digits)
    for x in digits:
        print(x)

    #pprint({x[0]*base**2 + x[1]*base**1+x[2]*base**0 : x  for x in  {(a,b,c) for a in digits for b in digits for c in digits}})

    comprehension_with_row = [row(x,20) for x in range(0,15)]
    comprehension_without_row = [[ y for y in range(x,x+20)] for x in range(0,15) ]
    #pprint(comprehension_without_row)

    print({x*y for x in {1,2,3} for y in {7,8,9}})
    X1 = {x*y for x in {2,3,4} for y in {5,6,7}}
    Y1 = {x*y for x in {1,3,9} for y in {2,6,18}}
    print(X1)
    print(Y1)

    S = {-4, -2, 1, 2, 5, 0}
    # Replace [ ... ] with a one-line list comprehension in which S appears
    exclude_zero_list = [(i,j,k) for i in S for j in S for k in S if ((i+j+k) == 0) and ((i == 0 and j==0 and k==0)== False)]
    print(exclude_zero_list)
