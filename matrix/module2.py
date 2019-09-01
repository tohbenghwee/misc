#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      toh
#
# Created:     11/02/2015
# Copyright:   (c) toh 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def getData():
    list = []
    list.append({'Beer', 'Nuts', 'Diaper'})
    list.append({'Beer', 'Coffee', 'Diaper', 'Nuts'})
    list.append({'Beer', 'Diaper', 'Eggs'})
    list.append({'Beer', 'Nuts', 'Eggs', 'Milk'})
    list.append({'Nuts', 'Coffee', 'Diaper', 'Eggs', 'Milk'})
    return list

def isAssociationRule(X,Y,S):
    status = False;
    list = getData()
    total = len(list)
    #print(total)
    count_support = 0.0
    count_confid_inBoth = 0.0
    count_confid_total = 0.0

    for x in list:
        if x.issuperset(X) and x.issuperset(Y):
            count_support = count_support + 1

        if x.issuperset(Y):
            count_confid_total= count_confid_total+1
            if x.issuperset(X):
                count_confid_inBoth = count_confid_inBoth + 1


    support = count_support/total
    confid = count_confid_inBoth/count_confid_total
    #support
    print("Support : " + str(support))
    #confidence
    print("Confid : " + str(confid))
    if support >= S and confid >= S:
        status = True

    return status



    return t
if __name__ == '__main__':
    print(isAssociationRule({'Nuts'} , {'Diaper'}, 0.5 ))
    print(isAssociationRule({'Nuts'} , {'Eggs'}, 0.5 ))
    print(isAssociationRule({'Diaper'} , {'Eggs'}, 0.5 ))
    print(isAssociationRule({'Beer'} , {'Nuts'}, 0.5 ))
    print(isAssociationRule({'Coffee'} , {'Milk'}, 0.5 ))
