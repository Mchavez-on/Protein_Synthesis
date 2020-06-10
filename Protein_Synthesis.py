
import tkinter
import time
import random
from PIL import ImageTk
from PIL import Image

def protein_synthesis():
    print('''Protein Synthesis is the process of creating proteins AKA polypeptides where DNA's coded message leaves the nucleus and travels to the ribosomes. This process is represented by the Central Dogma: genetic information flows in one direction - DNA ---> RNA ---> Proteins''')

def transcription_base_pairing():
    DNA1 = str(input("Enter your DNA sequence below!: \n"))
    Translate_DNA1 = DNA1.maketrans("TCGA","AGCU")
    print("You have transferred DNA to RNA!:\n",DNA1.translate(Translate_DNA1))

def transcription():
    print('''Transcription will now begin. There are three main steps of transcription: initiation, elongation, termination. Our friend RNA polymerase uses a gene on one DNA strand to synthesize a complementary mRNA strand. Base pairing rules are applied here, however Uracil substitutes Thymine. When RNA polymerase reaches the terminator, it detaches itself away of DNA; releasing a newly synthesized mRNA strand''')
    print('''You will have the opportunity to transfer DNA to RNA!!''')
    transcription_base_pairing()
    print('''Once the mRNA strand has been transcribed and processed, it leaves the nucleus and goes to the cytoplasm where it attaches itself to a ribosome''')
    print('''Translation will now begin''')

def decoding():
    mRNA = str(input('''Enter your mRNA codon sequence below!: \n'''))
    Translate_mRNA = mRNA.maketrans("UCGA","AGCU")
    print("You have let tRNA decode mRNA!!:\n",mRNA.translate(Translate_mRNA))

def translation():
    print('''Translation acts like a cryptographer. The genetic code stored in mRNA's codons which code for a specific amino acid and equal three consecutive mRNA nucleotides. tRNA will bind and complement mRNA's start codon. The ribosome will now slide down one mRNA codon as tRNA's complementary anticodon arrives, carrying a specific amino acid. Codon and Anticodon pairing involves the same nitrogen base pairs, with the exception of Uracil substituting Thymine.''')
    print("Please let the protein AKA polypeptide chain continue growing by helping tRNA decode mRNA!! ")
    decoding()
    print('''This process continues until the ribosome reaches a stop codon where no tRNA arrives. Its subunits fall apart - releasing a protein/polypeptide! YAY!!!''')
    print('''This concludes Protein Synthesis''')
    

def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    image = ImageTk.PhotoImage(Image.open("/Users/marianachavez/Desktop/CIP Final Project/proteinsynthesis.png"))
    canvas.create_image(250,300,anchor="nw",image=image)
    canvas.create_text(230, 50, anchor='w', font='Courier 52', text='Protein Synthesis')
    

    '''image = ImageTk.PhotoImage(Image.open("transcription.gif"))
    canvas.create_image(0,300,anchor="nw",image=image)
    image = ImageTk.PhotoImage(Image.open("translation.gif"))
    canvas.create_image(0,300,anchor="nw",image=image)'''

    canvas.create_rectangle(0, 800, 10, 810)
    canvas.mainloop()
    return canvas
    

def main():
    protein_synthesis()
    transcription()
    translation()
    canvas = make_canvas(1000, 1000, 'TEST')
    '''canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Awesome')
    canvas.create_text(20, 100, anchor='w', font='Courier 52', text='Protein Synthesis')
    canvas.create_rectangle(0, 800, 10, 810)
    canvas.mainloop()'''


if __name__ == '__main__':
    main()
   