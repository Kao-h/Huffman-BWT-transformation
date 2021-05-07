# Interative BWT & Huffman
### Code to perform the Burrows–Wheeler transform and the Huffman Compresion

## WARNING put all the files downloaded it one folder and place yourself using cd bash command in that same repository
- Check your python version it needs to be python  ✨3 ✨
- Verify you have the following libaries: 
 -tkinter 
 -ast

## Features proposed by the code

- Transform a sequence with Burrows–Wheeler transform 
- Restore a sequence transformed using Burrows–Wheeler transform 
- Compress a file using Huffman compression method
- Decompress a file using Huffman compression method
- Save output and intermediate steps in files

## Usage

Launch the tkinter interface

```sh
python3 GUI.py
```


## Use of each buttons and their output files

In a good order this is representatoion of the use of each button, the file you need as an input and output file(s)
plus a description of what is printed on the screen.
While using the STEP buttons

| Button | Print | Input file | Output file |
| ------ | ------ |---------------| -----------|
|Select a file | Sequence"s path |sequence.txt |None 
| Final BWT | Transformed sequence |None|BWT_transformation.txt
| STEP BWT| steps of  BWT | None|Step_bwt.txt
| Final Restore BWT| Restored sequence | BWT_transformation.txt|None
| STEP Restore BWT | Steps of reconstruction of text | BWT_transformation.txt|None
| Final compression Huffman | Encryption text| BWT_transformation.txt|Huffman_compression.tx, Huff_code.txt
| STEP compression Huffman | Binary texte,Added zeros ,Encryption |BWT_transformation.txt|Huffman_compression_steps.txt
| Final decompression Huffman | Decompressed text | Huffman_compression.tx|Huffman_decompression.txt



