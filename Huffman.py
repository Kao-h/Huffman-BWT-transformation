#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:59:58 2021

@author: Kaouther Harbi
"""
# Huffman Coding in python


# Creating tree sorted_freq_table
class NodeTree:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    
    def left_child(self):
        return self.left

    def right_child(self):
        return self.right
    
    def sorted_freq_table(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)
    
    


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binary_sequence=''):
    if type(node) is str:
        return {node: binary_sequence}
    
    left_child = node.left_child()
    right_child = node.right_child()
    sorted_freq_table_dico = dict()
    sorted_freq_table_dico.update(huffman_code_tree(left_child, True, binary_sequence + '0')) #fill left child
    sorted_freq_table_dico.update(huffman_code_tree(right_child, False, binary_sequence + '1')) #fill right child
    return sorted_freq_table_dico


# Calculating frequency 
def frequency_table(texte):
    ''' given a text it returns the frequency of each string as a dictionnary'''
    frequency_table = {}
    for aa in texte:
        if aa in frequency_table:
            frequency_table[aa] += 1
        else:
            frequency_table[aa] = 1
    return frequency_table

def binary_tree(texte):
    '''building of the binary tree''' 
    freq_table = frequency_table(texte)
    sorted_freq_table = sorted(freq_table.items(), key=lambda x: x[1], reverse=True)
    while len(sorted_freq_table) > 1:
        (amino_acid1, min_freq1) = sorted_freq_table[-1] #first minimum freq
        (amino_acid2, min_freq2) = sorted_freq_table[-2] #second minimum freq
        sorted_freq_table = sorted_freq_table[:-2] #shorten the list of the freq table
        node = NodeTree(amino_acid1, amino_acid2) #create first 2 sorted_freq_table l,r = None
        sorted_freq_table.append((node, min_freq1 + min_freq2)) # node + data tuple
    
        tree = sorted(sorted_freq_table, key=lambda x: x[1], reverse=True)
    return tree

#extraction huffman coding as dictionnary
def dico_huffman(texte):
    tree = binary_tree(texte)
    huffmanCode = huffman_code_tree(tree[0][0])
    return huffmanCode

        
#convert a texte to binary        
def binary_huffman(texte):
    huffman_code = dico_huffman(texte)
    huff_crypted = ''
    for i in range (0,len(texte),1):
        if texte[i] in huffman_code:
            huff_crypted +=huffman_code[texte[i]]
    #print('Original sequence: \n'+ texte)
    #print('Binary sequence coding: \n'+ huff_crypted)
    return huff_crypted



#make the binary sequence length a multiple of 8
def seq_eight_bits(texte):
    binary_seq =binary_huffman(texte)
    added_0 = 0
    while len(binary_seq) % 8 != 0:
        binary_seq += '0'
        added_0 +=1
    #print('8 bits binary sequence: \n' + binary_seq)
    return binary_seq, added_0


#convert binary to unicode
def seq_unicode(texte):
    eight_bits, _ =  seq_eight_bits(texte)
    unicode = ''
    for binary in range (0, len(eight_bits),8):
        bits = eight_bits[binary: binary+8]
        code = int(bits,2)
        unicode += chr(code)
    #print('Encrypted sequence: \n' + unicode)
    return unicode


#summary of the compression steps
def huffman_compression(texte):
    eight_bits, _ =  seq_eight_bits(texte)
    cryption = seq_unicode(texte)
    _,addition = seq_eight_bits(texte)
    code = dico_huffman(texte)
    return cryption,addition,code,eight_bits


cry,plus,mat,bina =huffman_compression('AATGCCTTTCTTCATTGTTTCGAGAAACCTAAACA$AGGGCA')
#decompression

#convert unicode to binary and remove the added 0 
def unicode_binary(crypted,ad):
    ''' givien the crypted text and number of added zero returns a binary text'''
    sequence_unicode = crypted   
    bin_str = ''
    for u in sequence_unicode:
        #ord gives an integer representing the unicode
        code = ord(u)
        # convervion du binary 
        bin_str += '{:08b}'.format(code)
    bin_str = bin_str[0:len(bin_str)-ad]
    return bin_str
unicode_binary(cry, plus)

#get back to the original text from binary
def binary_original_seq(crypted,ad,dico):
    ''' givien the crypted text and number of added zero
    and encryption huffman dictionnary it return the original text'''
    back_bin = unicode_binary(crypted,ad)
    cadre = ''
    back_seq = '' 
    huffman_dictionnary = dico
    print(huffman_dictionnary)
    for i in range (0, len(back_bin),1):
        cadre += back_bin[i]
        #use of the dico to determine the original text
        for key, value in huffman_dictionnary.items():
            if cadre == value:
                cadre = ''
                back_seq += key
    #print('Back to original \n' +back_seq)
    return back_seq

#summuary of the decompression steps 
def huffman_decompression(texte,ad,dico):
    bina = unicode_binary(texte, ad)
    decrypt = binary_original_seq(texte,ad,dico)
    return decrypt, bina, ad


