# RGB to ACI table here: https://gohtx.com/acadcolors.php

import ezdxf, sys

if len(sys.argv) < 2: exit() # Exit when there is no file

def main():

    for filename in sys.argv[1:]:

        doc = ezdxf.readfile(filename)
        delete_lines(doc) # parse file

def delete_lines(doc):

    msp = doc.modelspace() # import file's modelspace
    # Query all lines in Magenta and then delete them
    dimlines = msp.query('*[color==6]') # 255, 0, 255
    for entity in dimlines: msp.delete_entity(entity)

    doc.save()

if __name__ == '__main__':
   main()