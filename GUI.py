#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:54:06 2021

@author: Kaouther Harbi
"""


from tkinter import Tk,filedialog, END,Button,Text,Label,Scrollbar,BOTH,Frame,messagebox,RIGHT, NORMAL, DISABLED
import BTW
import Huffman
import ast



#############################################
# Functions
def select_file():
    '''Check file we want to use'''
    
    global sequence
    sequence = ""
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("text files","*.txt"),
                                                   ("all files","*.*")))
    with open(filename ,"r") as file:
        for line in file:
            sequence += line.strip()
    print(sequence)
    
    sequence_label.configure(text= sequence_label.cget("text") + filename)
    
    

# fichier = select_file()
def check_sequence(sequence):
    """ function which checks if the sequenceuence is without a header and only
    composed of letters
    ----------------------------------------
    sequence: sequenceuence to check as str """
    
    boolean = True
    for i in range(0, len(sequence),1):
        if sequence[i] not in ['A','T','C','G','N','S']:
            boolean = False
            raise Exception('This is not a sequence in a valid format')
            break
    return boolean



#BWT

        
def final_bwt():
    '''gives the final result of BWT transormed text'''
    global count
    count = 0
    final_bwt_result,_ = BTW.btw_transformation(sequence)
    bwt_file = open("BWT_Transformation.txt", "w")
    bwt_file.write(final_bwt_result)
    bwt_file.close()
    Result.delete('1.0', END)
    Result.insert(END, 'Final BWT: '+final_bwt_result)
    

count = 0

 
def step_bwt():
    '''returns step by step BWT transformation'''
    global count
    _,matrice = BTW.btw_transformation(sequence)
    print(count)
    if count <= len(matrice):
        with open("Step_bwt.txt", "a") as myfile:
        
            Result.insert(END,'\n'+matrice[count])
            myfile.write('\n'+matrice[count])
            count +=1
    
        
def final_restore_bwt():
    messagebox.showinfo(root_window, message='Select the file you want to restore with BWT')
    file_torestore = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Rtext files","*.txt"),
                                                    ("all files","*.*")))
    print(file_torestore)
    #open the file we want to compress
    global count
    count = 0
    restored_seq,_,_ = BTW.restore_btw(file_torestore)
    Result.delete('1.0', END)
    Result.insert(END, 'Original sequence:  ' +restored_seq)
  
    
def step_restore_bwt():
    
    global count
        
    #get final transformed sequence and matrice created in restore 
    final,matrice = BTW.restore_btw('BWT_Transformation.txt')
    
    #clear result 
    Result.config(state=NORMAL)
    Result.delete('1.0', END)
    if count < len(matrice):
        for i in range(0,len(matrice[0]),1):
            #print alterned sorted and unsorted matrice of steps
            Result.insert(str(i+1) + '.' + str(len(matrice[i])), matrice[count][i] + "\n")
    else:
        Result.delete('1.0', END)
        Result.insert(END,'Restored after BWT:  '+final)
        count = 0
    Result.config(state=DISABLED) 
    count+=1

#Huffman

def final_compression():
    messagebox.showinfo(root_window, message='Select the file you want to compress usisng Huffman')
    to_compress = ''
    file_2 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("text files","*.txt"),
                                                    ("all files","*.*")))
    #open the file we want to compress
    with open(file_2 ,"r") as file2:
        for line in file2:
            to_compress += line.strip()
    print(to_compress)
    compressed,added,code_dico,binaire = Huffman.huffman_compression(to_compress)
    
    #save huff dico encryption
    with open('Huff_code.txt', 'w') as f:
        print(code_dico, file=f)
    
    
    #save encrypted
    with open("Huffman_compression.txt", "w") as myfile:
        myfile.write(compressed+ '\n'+ str(added))
        Result.delete('1.0', END)
        Result.insert(END, 'Huffman encryption : '+compressed)
        
def step_compression():
    messagebox.showinfo(root_window, message='Select the file you want to compress usisng Huffman')
    to_compress = ''
    file_2 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("text files","*.txt"),
                                                    ("all files","*.*")))
    #open the file we want to compress
    with open(file_2 ,"r") as file2:
        for line in file2:
            to_compress += line.strip()
    print(to_compress)
    compressed,added,code_dico,binaire = Huffman.huffman_compression(to_compress)
    
    #save huff dico encryption
    with open('Huff_code.txt', 'w') as f:
        print(code_dico, file=f)
        with open("Huffman_compression_steps.txt", "w") as myfile:
            myfile.write('Binary conversion:  '+ binaire+ '\n Added_0:  '+ str(added)+ '\n Compressed   '+compressed)
            Result.delete('1.0', END)
            Result.insert(END, 'Binary conversion: '+ binaire+ '\nAdded_0: '+ str(added)+ '\nCompressed  '+compressed)
   
def final_decompression():
    to_decompress = ''
    addition = ''
    #file to decompress
    messagebox.showinfo(root_window, message='Enter the file you want to decompress')
    #selection of file to decompress using huffman
    file_3 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("text files","*.txt"),
                                                    ("all files","*.*")))
    #reading encrypted text plus the number of added 0
    with open(file_3 ,"r") as file3:
        for index, line in enumerate(file3) :
            if index == 0:
                to_decompress = line.strip('\n')
            if index == 1:
                addition = int(line)
   
    #reading encryption using the dictionnary
    file = open('Huff_code.txt', 'r')
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    print(dictionary)
    
    decompressed = Huffman.binary_original_seq(to_decompress,addition,dictionary)
    print(decompressed)
    with open("Huffman_decompression.txt", "w") as myfile:
        myfile.write(decompressed)
        Result.delete('1.0', END)
        Result.insert(END, 'Huffman decrypted : '+decompressed)



##########################################
# Buttons


root_window = Tk()
root_window.title("Interative BWT & Huffman")
root_window.geometry('700x700')

select_button = Button(root_window, text = 'Select file', command = select_file, activeforeground ='green')
select_button.pack(padx=15, pady=20)

#check_sequence(sequence)
sequence_label = Label(root_window, text = 'Sequence"s path: ":')
sequence_label.pack(fill = BOTH)

#BWT buttons
final_bwt_button = Button(root_window, text= 'Final BWT', command =final_bwt, activeforeground ='blue')
final_bwt_button.pack(padx=30,  pady=10)

step_bwt_button = Button(root_window, text= 'STEP BWT', command = step_bwt, activeforeground ='blue')
step_bwt_button.pack(padx = 30,  pady=10)

final_restore_btw_button = Button(root_window, text= 'Final Restore BWT', command = final_restore_bwt, activeforeground ='blue')
final_restore_btw_button.pack(padx = 30,  pady=10)

step_restore_btw_button = Button(root_window, text= 'STEP Restore BWT', command = step_restore_bwt,activeforeground ='blue')
step_restore_btw_button.pack(padx = 30,  pady=10)


#####################################" Huffman
huffman_button = Button(root_window, text= 'Final compression Huffman', command = final_compression,activeforeground ='red')
huffman_button.pack(padx = 30,  pady=10)

step_huffman_button = Button(root_window, text= 'STEP compression Huffman',command= step_compression, activeforeground ='red')
step_huffman_button.pack(padx = 30,  pady=10)

decom_huffman_button = Button(root_window, text= 'Final decompression Huffman', command = final_decompression,activeforeground ='red')
decom_huffman_button.pack(padx = 30,  pady=10)



################################# Result
result_label = Label(root_window, width =10)
result_label.pack(fill = BOTH)

Result = Text(root_window, height=10, width=70)


# scrollbar
f = Frame(root_window)
scrollbar = Scrollbar(f, width= 20)
scrollbar.config(command=Result.yview)
scrollbar.pack(side=RIGHT)
Result.pack()
f.pack()

root_window.mainloop()
