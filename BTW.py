#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:37:36 2021

@author: Kaouther Harbi

"""


sequence ='ACTTGATC'

def print_matrix(matrix):
    ''' function to print matrix'''
    for i in matrix:
        print(i)
        
    

def btw_transformation(sequence):
    '''

    Takes sequence as entry and performs BWT 
    '''
    sequence += '$'
    #put AA as a list
    amino_acids = list(sequence)
    lexicographic = []
    bwt = ''
    #loop to create a lexicographic order of the sequence
    for i in range(0, len(amino_acids), 1):
        shif_sequence = sequence[-1] + sequence[:-1]
        shifted = ''.join(shif_sequence)
        sequence = shifted
        lexicographic.append(shifted)
    
    #print(lexicographic)
    
    lexicographic_sort = sorted(lexicographic)
    #print_matrix(lexicographic)
    #lexicographic_matrix = print_matrix(lexicographic)
    #loop to put in place the final matrix 
    for i in range(0, len(amino_acids),1):
        element = lexicographic_sort[i]
        last = element[- 1]
        i = i + 1
        bwt +=last
        #print(last)
    #print('Transformed BWT = '+bwt)
    
    
    return bwt,lexicographic


   



#restore
def restore_btw(file):
        f = open(file, "r")
        transformed_bwt= ""
        #reading of the file
        for line in f :
            #retrive the bwt sequence in bwt variable deleting "\n"
            transformed_bwt += line
            transformed_bwt = transformed_bwt.strip("\n")
    
        #create an empty table of the size of the BWT text
        matrice =[]    
        table = [""] * len(transformed_bwt)
        for i in range(0,len(transformed_bwt),1):
            #the table is filled with original elements of the bwt + sorted
            table = [transformed_bwt[i] + table[i] for i in range(0,len(transformed_bwt),1)]
            matrice.append(table)
    
            #the matrice saves steps for sorted and an unsorted as list of lists
            table = sorted(table)
            matrice.append(table)
        #Find the text ending with a $
        for element in table : 
            if element.endswith("$"):
                #retrieve the original sequence ends with the dollar in a original_text sequence
                original_text = element
                original_text =original_text[0:len(original_text)-1]
                 
        return original_text,matrice

