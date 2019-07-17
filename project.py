from tkinter import *
from tkinter.constants import CENTER
from tkinter import messagebox


def clear():
    global entry1,entry2
    entry1.delete(0,END)
    entry2.delete(0,END)


"""CAESAR CIPHER"""
def caesar_encryption():
    global entry1,entry2
    plain_text = entry1.get()
    key = entry2.get()
    key = int(key)
    alph = ("abcdefghijklmnopqrstuvwxyz")
    newMsg = ""
    for char in plain_text:
        if char in alph:
            pos = alph.find(char)
            newPos = (pos + key) % 26
            newChar = alph[newPos]
            newMsg += newChar
        else:
            newMsg += char

    messagebox.showinfo("Result", newMsg)

def caesar_decryption():
    global entry1,entry2
    cipher_text = entry1.get()
    key = entry2.get()
    key = int(key)
    cipher_text = cipher_text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in cipher_text:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter
            
    messagebox.showinfo("Result", result)

"""END OF CAESAR CIPHER"""

"""PLAYFAIR CIPHER"""

def Playfair_encryption():
    global entry1,entry2
    plain_text = entry1.get()
    key = entry2.get()
    # key = input('Enter the input key:- ')
    # plain_text = input('Enter the plain text:- ')
    special_symbol='x'                                              

    def construct_box(key):
        '''Creates Play Fair Box'''
        key.replace('j', 'i')
        d={i:0 for i in 'abcdefghiklmnopqrstuvwxyz'}
        box=[]                                              
        for i in key:
            if not d[i]:
                d[i]+=1
                box.append(i)
        box.extend([i for i in d if not d[i]])
        box = [box[i:i+5] for i in range(0,25,5)]
        return box

    def transform(data,ss='x'):
        '''Transforming data in sets of 2-2 and using special symbol '''
        data = [data[i:i+2] for i in range(0,len(data),2)]  #Splitting data in 2-2
        new = []
        for item in data:                                   #Inserting Special Symbol 
            if len(item)==1: new.append((item[0],ss))
            elif item[0]==item[1]: new.extend([(item[0],ss),(item[0],ss)])
            else: new.append((item[0],item[1]))
        return new

    def encryption(data,ss):
        box = construct_box(key)
        data = transform(data,ss)
        #print(*box,sep='\n')                               #To See the structure Uncomment these
        #print(data)
        ans = []
        for x,y in data:
            a=b=c=d=-1
            for i in range(5):
                for j in range(5):
                    if box[i][j]==x: a,b=i,j
                    if box[i][j]==y: c,d=i,j
            if a==c: ans.append((box[a][(b+1)%5],box[c][(d+1)%5]))          #Same Row
            elif b==d: ans.append((box[(a+1)%5][b] ,box[(c+1)%5][d]))       #Same Column 
            else: ans.append((box[a][d] ,box[c][b]))                        #Different Row & Column
        ans = ''.join([element for group in ans for element in group])
        return ans

    cipher_text = encryption(plain_text,special_symbol)
    messagebox.showinfo("Result", cipher_text)


"""END OF PLAYFAIR CIPHER"""


"""Start of AFFINE CIPHER """

def Affine_encryption():
    global entry1,entry2,entry3
    plain_text = entry1.get()
    key = []
    key.append(int(entry2.get()))
    key.append(int(entry3.get()))

    def encrypt(plain_text,key):
        return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in plain_text.upper().replace(' ', '') ]) 


    cipher = encrypt(plain_text,key)
    messagebox.showinfo("Result", cipher)
    
def Affine_decryption():
    global entry1,entry2,entry3
    cipher_text = entry1.get()
    key = []
    key.append(int(entry2.get()))
    key.append(int(entry3.get()))

    def egcd(a, b): 
        x,y, u,v = 0,1, 1,0
        while a != 0: 
            q, r = b//a, b%a 
            m, n = x-u*q, y-v*q 
            b,a, x,y, u,v = a,r, u,v, m,n 
        gcd = b 
        return gcd, x, y 
  
    def modinv(a, m): 
        gcd, x, y = egcd(a, m) 
        if gcd != 1: 
            return None  # modular inverse does not exist 
        else: 
            return x % m 
       
    def decrypt(cipher,key):
         return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ]) 

    plain = decrypt(cipher_text,key)
    messagebox.showinfo("Result", plain)
    

"""End of AFFINE CIPHER """



def click1():
    global win
    global entry1,entry2
    win1=Toplevel(win)
    win1.geometry("700x250")
    win1.title("Caesar Cipher")
    l1= Label(win1,compound=LEFT,text= 'Enter the Plain Text/Cipher Text:', height="2", width="30").grid(row=1, column=0, sticky=W)
    l2= Label(win1,compound=LEFT,text= 'Enter the input key(in number):', height="2", width="30").grid(row=2, column=0, sticky=W)
    entry1= Entry(win1,width=20)
    entry2= Entry(win1,width=20)
    entry1.grid(row=1, column=1)
    entry2.grid(row=2, column=1)
    b1= Button(win1, width=7,text="Encrypt",command=caesar_encryption).grid(row=4, column=0, sticky=W)
    b2= Button(win1, width=7,text="Decrypt",command=caesar_decryption).grid(row=4, column=1, sticky=W)
    b3= Button(win1, width=7,text="cancel",command=clear).grid(row=4, column=3, sticky=W)


def click2():
    global win
    global entry1,entry2
    win1=Toplevel(win)
    win1.geometry("700x250")
    win1.title("PlayFair Cipher")
    l1= Label(win1,compound=LEFT,text= 'Enter the Plain Text', height="2", width="30").grid(row=1, column=0, sticky=W)
    l2= Label(win1,compound=LEFT,text= 'Enter the input key:', height="2", width="30").grid(row=2, column=0, sticky=W)
    entry1= Entry(win1,width=20)
    entry2= Entry(win1,width=20)
    entry1.grid(row=1, column=1)
    entry2.grid(row=2, column=1)
    b1= Button(win1, width=7,text="Encrypt",command=Playfair_encryption).grid(row=4, column=1, sticky=W)
    b3= Button(win1, width=7,text="cancel",command=clear).grid(row=4, column=2, sticky=W)

def click3():
    global win
    global entry1,entry2,entry3,entry4
    win1=Toplevel(win)
    win1.geometry("700x250")
    win1.title("Affine Cipher")
    l1= Label(win1,compound=LEFT,text= 'Enter the Plain Text/Cipher Text:', height="2", width="30").grid(row=1, column=0, sticky=W)
    l2= Label(win1,compound=LEFT,text= 'Enter the input key 1:', height="2", width="30").grid(row=2, column=0, sticky=W)
    l3= Label(win1,compound=LEFT,text= 'Enter the input key 2:', height="2", width="30").grid(row=3, column=0, sticky=W)
    entry1= Entry(win1,width=20)
    entry2= Entry(win1,width=20)
    entry3= Entry(win1,width=20)
    entry1.grid(row=1, column=1)
    entry2.grid(row=2, column=1)
    entry3.grid(row=3, column=1)
    b1= Button(win1, width=7,text="Encrypt",command=Affine_encryption).grid(row=5, column=0, sticky=W)
    b2= Button(win1, width=7,text="Decrypt",command=Affine_decryption).grid(row=5, column=1, sticky=W)
    b3= Button(win1, width=7,text="cancel",command=clear).grid(row=5, column=3, sticky=W)


def main(): 
    global win 
    win = Tk()            #calling window creating function (instance)
    win.title("Python Project")  
    win.geometry("700x250")          #name of the window
    label= Label(win,compound=CENTER,text="hello, welcome to Cipher application",width=40, height=1, bg="blue")
    label.pack()
    b1= Button(win,text="Caesar Cipher",command=click1, height=1, width=10, bg="blue").pack()
    b2= Button(win,text="Playfair Cipher",command=click2, height=1, width=10, bg="blue").pack()
    b3= Button(win,text="Affine Cipher",command=click3, height=1, width=10, bg="blue").pack()

main()
win.mainloop()              #only then window process starts

