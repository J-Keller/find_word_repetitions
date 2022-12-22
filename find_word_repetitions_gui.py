import tkinter
from tkinter.filedialog import askopenfilename
from pathlib import Path


inputFile = './bla.txt'
outputFile = './bli.txt'
pedantic = False
e_in = None
e_out = None


def choose_file(isInput: bool):
    global inputFile
    global outputFile
    global e_in
    global e_out
    if isInput:
        inputFile = askopenfilename()
        e_in.delete(0, tkinter.END)
        e_in.insert(0, inputFile)
    else:
        outputFile = askopenfilename()
        e_out.delete(0, tkinter.END)
        e_out.insert(0, outputFile)


def find_word_repetitions():
    txt = Path(inputFile).read_text()
    txt.replace('\n', '')

    out_file = open(outputFile, 'a')

    sentences = txt.split('.')

    previous_word = ''
    counter = 0
    for sentence in sentences:
        words = sentence.split(' ')
        counter += 1
        for word in words:
            if '-' in word:
                subwords = word.split('-')
                for w in subwords:
                    if pedantic:
                        if word == previous_word:
                            out_file.write(word)
                            out_file.write(str(counter) + ': ' + sentence)
                    else:
                        if word in previous_word or previous_word in word:
                            if word != '' and previous_word != '':
                                out_file.write(word)
                                out_file.write(str(counter) + ': ' + sentence)

            if pedantic:
                if word == previous_word:
                    out_file.write(word)
                    out_file.write(str(counter) + ': ' + sentence)
            else:
                if word in previous_word or previous_word in word:
                    if word != '' and previous_word != '':
                        out_file.write('\r\n' + word + ' ' + str(counter) + ':\n' + sentence + '\n')
            previous_word = word
    exit(0)

tk = tkinter.Tk()

frame = tkinter.Frame(tk, relief="ridge", borderwidth=2)
frame.pack(fill="both",expand=1)
# input file
label = tkinter.Label(frame, text="Zu prüfende Datei")
label.pack(expand=1)
e_in = tkinter.Entry(frame)
e_in.pack()
e_in.delete(0, tkinter.END)
e_in.insert(0, inputFile)
button = tkinter.Button(frame,text="Datei wählen",command=lambda: choose_file(True))
button.pack()
# output file
label = tkinter.Label(frame, text="Ergebnisdatei")
label.pack(expand=1)
e_out = tkinter.Entry(frame)
e_out.pack()
e_out.delete(0, tkinter.END)
e_out.insert(0, outputFile)
button = tkinter.Button(frame,text="Datei wählen",command=lambda: choose_file(False))
button.pack()
# checkbox
c = tkinter.Checkbutton(frame, text="Nur exakte übereinstimmungen nehmen")
c.pack()

button = tkinter.Button(frame,text="Ab dafür",command=lambda: find_word_repetitions())
button.pack()

tk.mainloop()