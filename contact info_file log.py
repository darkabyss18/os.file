import os
import logging




def directory():
    txt = input('please specify the directory you would like to store your file under. (keep in mind it is case sensitive): ')
    X = ''
    for root, dirs, files in os.walk('C:\\'):
        for name in dirs:
            if name == txt:
                global x
                x = (os.path.abspath(os.path.join(root, name)))
                print (x)
                print('this directory exists!')
                info()
                confirm()
           


def info():
    name = '\\' + input('what would you like to name the file? ') + '.log'
    global x
    inp_1 = input('Please input your name: ')
    inp_2 = input ('Please enter your adress: ')
    inp_3 = input('Please enter your phone number: ')
    
    global h
    h = x + name

    wr = open (h, 'w')
    mes = f'Name: {inp_1}, Adress: {inp_2}, Phone Number: {inp_3}'
    wr.writelines(mes)
    wr.close
    

    print (h)
    



def confirm():
    l = open (h, 'r')
    lines = l.readlines()
    l.close

    print (lines[-1])
    
    directory()

directory()
print('invalid file location')
directory()  
