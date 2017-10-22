import random
import string
import pdb
import os
import sys


class GenerateBook:

    space = " "
    letters = list(string.ascii_letters)
    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    numbers = [i for i in range(1, 10)]
    internal_mark = [ "-" ,  "," , ";" , ":" ]
    end_mark= [ ".", "?", "!"]
    chapter_begin = "# Chapter {0}" + os.linesep
    space = " "


    def __init__(self,number_of_chapters, number_of_words_in_chapter, filename=None):
        self.number_of_chapters = number_of_chapters
        self.number_of_words_in_chapter = number_of_words_in_chapter
        self.path_to_file = os.environ["HOME"] + "/0011.txt" if filename == None else filename

    def generate_word(self,first_word=False):

        #longest word in English are  about 30 chars
        length = random.randint(1, 30)
        word = ""
        if first_word:
            word = random.choice(self.uppercase)

        while len(word) != length:
            word += str(random.choice(self.lowercase))

        return word


    def generate_number(self):

        length = random.randint(1, 10)

        word = ""
        while len(word) != length:
            word += str(random.choice(self.numbers))
        return word

    def internal_punctuation(self):
        return random.choice(self.internal_mark)


    def end_of_sentence(self):
        return random.choice(self.end_mark)


    def generate_sentence(self,number_of_word_in_sentence):

        sentence = ""

        random_dummy_value = random.randint(1, 100)
        for i in range(number_of_word_in_sentence):
            if i == 0:
                sentence += self.generate_word(first_word=True)
            elif random_dummy_value == random.randint(1, random_dummy_value):
                sentence += self.generate_number()
            else:
                sentence += self.generate_word()

            # end of sentence
            if i+1 ==  number_of_word_in_sentence:
                sentence += self.end_of_sentence()
                sentence += self.space
                if random_dummy_value % 11 == 0:
                    sentence += os.linesep
                return sentence


            if random_dummy_value % random.randint(1,23) == 0:
                sentence += self.internal_punctuation() + self.space
            else:
                sentence += self.space

            if random_dummy_value % 11 == 0:
                sentence += "\n"


    def generate_chapter(self,number_of_words_in_chapter, chapter_number):
        chapter = self.chapter_begin.format(chapter_number)
        left_words  = self.number_of_words_in_chapter

        while left_words != 0:

            if left_words <= int(random.randint(1,10)):
                chapter += self.generate_sentence(left_words)
                left_words = 0

            else:
                number_of_word_in_sentence = random.randint(1, left_words)
                left_words -= number_of_word_in_sentence
                chapter += self.generate_sentence(number_of_word_in_sentence)

        chapter += os.linesep
        return chapter



    def generate_book(self):

        print("Starting writing on file ", self.path_to_file )
        with open(self.path_to_file,'w') as fd:

            for chapter_number in range(1 , int(self.number_of_chapters) + 1):

                print("Start Generating Chapter {0}".format(chapter_number))
                fd.write(self.generate_chapter(self.number_of_words_in_chapter,
                                               chapter_number))

                print("Finish Generating Chapter {0}".format(chapter_number))

        print("Starting Finish on file ", self.path_to_file )


if __name__ == "__main__":
    try :
        chapter_count =  int(sys.argv[1])
        chapter_length_range = int(sys.argv[2])
    except IndexError:
        print("Pass two arguments: Number of chapters and Number of word in chapter")
        sys.exit(1)

    book = GenerateBook(chapter_count, chapter_length_range)
    book.generate_book()
