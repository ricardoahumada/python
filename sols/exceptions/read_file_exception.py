#!/usr/bin/env python3

def try_open_file(afile):
    try:
        f = open(afile, 'r')
        return f
    except OSError:
        print("...File does not exist...:", afile, "...")
        return None


while True:
    filename = input('Enter the file name (exit to quit): ')
    if(filename=='exit'):
        break
    else:
        file = try_open_file(filename)
        if(file):
            print('...reading: ', filename)
            contentlines = file.readlines()
            print('The file has: ', len(contentlines))
            break
