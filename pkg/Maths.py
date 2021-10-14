# -------------------------------------------------------------------------------
# Name:        Maths.py
# Project:     CA_Lab1
#
# Author:      Vitaliy Baseckas
#
# Created:     13.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
list=[]
def numbers():
    ''' This is a simple function to crated a list  with numbers from 0 to 9
    No input required
    Returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
    for i in range(10):
        list.append(i)
    #print(list)
    return str(list)

if __name__ == '__main__':
    numbers()