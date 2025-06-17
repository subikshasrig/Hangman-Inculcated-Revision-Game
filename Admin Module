import os
import pickle
import csv

def AdPhy():
    f=open('Physics.csv', 'a', newline='')
    w=csv.writer(f)
    n=eval(input('Enter the serial number of records to append: '))
    for i in range(n):
        sno=eval(input('Enter the serial number of record: '))
        print()
        hint=input('Enter the hint for the question: ')
        print()
        ans=input('Enter the answer for the given question: ')
        print()
        l=[sno,hint,ans]
        w.writerow(l)
    f.close()

def RePhy():
    f=open('Physics.csv', 'r', newline='')
    nf=open('nPhysics.csv','w', newline='')
    r=csv.DictReader(f)
    w=csv.writer(nf)
    c=int(input('Enter character number to delete: '))
    no=0
    line=0
    w.writerow(['Serial No.', 'Hint', 'Answer'])
    for i in r:
        if i['Serial No.']==str(c):
            pass
        else:
            no+=1
            i['Serial No.']=no
            l=[i['Serial No.'], i['Hint'], i['Answer']]
            w.writerow(l)
    f.close()
    nf.close()
    os.remove('Physics.csv')
    os.rename('nPhysics.csv', 'Physics.csv')

def VPhy():
    f=open('Physics.csv')
    os.startfile('Physics.csv')
    f.close()

def AdChem():
    f=open('Chemistry.csv', 'a', newline='')
    w=csv.writer(f)
    n=eval(input('Enter the serial number of records to append: '))
    for i in range(n):
        sno=eval(input('Enter the serial number of record: '))
        print()
        hint=input('Enter the hint for the question: ')
        print()
        ans=input('Enter the answer for the given question: ')
        print()
        l=[sno,hint,ans]
        w.writerow(l)
    f.close()

def ReChem():
    f=open('Chemistry.csv', 'r', newline='')
    nf=open('nChemistry.csv','w', newline='')
    r=csv.DictReader(f)
    w=csv.writer(nf)
    c=int(input('Enter character number to delete: '))
    no=0
    line=0
    w.writerow(['Serial No.', 'Hint', 'Answer'])
    for i in r:
        if i['Serial No.']==str(c):
            pass
        else:
            no+=1
            i['Serial No.']=no
            l=[i['Serial No.'], i['Hint'], i['Answer']]
            w.writerow(l)
    f.close()
    nf.close()
    os.remove('Chemistry.csv')
    os.rename('nChemistry.csv', 'Chemistry.csv')

def VChem():
    f=open('Chemistry.csv')
    os.startfile('Chemistry.csv')
    f.close()

def AdEng():
    f=open('characters.dat', 'rb')
    nf=open('ncharacters.dat', 'wb')
    rec=int(input('Enter number of records to append: '))
    print()
    no=0
    for i in range(rec): 
        try:
            while True:
                l=pickle.load(f)
                pickle.dump(l,nf)
                no+=1
        except EOFError:
            no+=1
        char=input('Enter character name: ')
        print()
        des=input('Enter Description: ')
        print()
        ln=[no,char.upper(),des]
        pickle.dump(ln,nf)
    f.close()
    nf.close()
    os.remove('characters.dat')
    os.rename('ncharacters.dat','characters.dat')

def ReEng():
    f=open('characters.dat','rb')
    nf=open('ncharacters.dat','wb')
    c=int(input('Enter character number to delete: '))
    x=0
    no=0
    try:
        while True:
            l=pickle.load(f)
            x+=1
            if x==c:
                pass
            else:
                no+=1
                l[0]=no
                pickle.dump(l,nf)
    except EOFError:
        f.close()
        nf.close()
    os.remove('characters.dat')
    os.rename('ncharacters.dat','characters.dat')

def VEng():
    f=open('characters.dat','rb')
    try:
        while True:
            l=pickle.load(f)
            print(l)
    except EOFError:
        f.close()






    
