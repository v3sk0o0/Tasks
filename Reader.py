import os
import glob
import pdb
import sys
import itertools
from functools import partial
from pynput.keyboard import Key, Listener

class Reader:


    blocksize = 512

    def __init__(self,directory):

        self.generated_chapters = self.reader(directory)

    def all_chapters(self, file_name):
        with open(file_name, "r") as expect_result:
            chapter = ""
            for chunk in iter(partial(expect_result.read, self.blocksize), ''):
                for symbol in chunk:

                    if  "#" in symbol and chapter != "":
                        yield (chapter)
                        chapter = symbol
                    else:
                        chapter += symbol
            yield (chapter)

    def reader(self,directory):

        if not os.path.exists(directory):
            print("Can not find Book directory")
            return 1
        pattern = os.path.join(directory,"[0-9]*.txt")
        file_names =  sorted(glob.glob(pattern))
        if not file_names:
            print("Can not find chaptes")
            return 1
        for file_name in sorted(glob.glob(pattern)):
            return self.all_chapters(file_name)


    def on_press(self,key):
        #print('{0} pressed'.format(
         #   key))
        if Key.space == key:
            try:
                print (self.show_value())
            except StopIteration:
                print ("No more chapters left")
        elif Key.esc ==  key:
            return False
        else:
            print( "\n Space to continue, escape for exit \n")


    def show_value(self):
        return next(self.generated_chapters)


if __name__ == "__main__":
    try :
        directory =  sys.argv[1]
    except IndexError:
        print("pass directory path to Book as a  command line argument")
        sys.exit(1)


    reader = Reader(directory)
    # Collect events until released
    with Listener(on_press=reader.on_press) as listener:
        listener.join()
