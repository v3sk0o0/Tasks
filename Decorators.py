import os
import pdb
from datetime import datetime

def accepts(*args):
    global types
    types = list(args)

    def real_decorator(function):
        def wrapper(*args, **kwargs ):

            if len(types) !=  len(args):
                raise TypeError("Different number of argumens")
            for index in range(len(args)):
                   if type(args[index]) != types[index]:
                        raise TypeError("Argument {0} of {1} is not {2}!".format(index,function.__name__,types[index].__name__))
            function(*args, **kwargs)


        return wrapper
    return real_decorator

def cypher(symbol, indentation):
    if  "A" <= symbol <= "Z":
        return (chr(ord("A") + ((ord(symbol) - ord("A") + indentation) % 26) ))
    elif "a" <= symbol <= "z":
        return (chr(ord("a") + ((ord(symbol) - ord("a") + indentation) % 26) ))
    else:
         return symbol


def encrypt(argument):

    if type(argument) != int:
        raise TypeError("Expected integer as an argument")
    def real_decorator(function):
         def wrapper():
            result = ("".join( [ cypher(char, argument % 26) for char in function() ]) )
            return result
         wrapper.__name__ = function.__name__
         return wrapper
    return real_decorator


def log(filename):
    def real_decorator(function):
        def wrapper(*args, **kwargs):

            dt = datetime.now()
            message = dt.strftime("{0} was called at %Y-%d-%m %H:%M:%S.%f".format(function.__name__))
            with open(filename, 'a') as the_file:
                the_file.write(message +  os.linesep)
            return function(*args, **kwargs)
        return wrapper
    return real_decorator



def performance(filename):
    def real_decorator(function):
        def wrapper(*args, **kwargs):

            start = datetime.datetime.now()
            result = function()
            stop  = datetime.datetime.now()
            difference = stop - start
            message = "{0} was called and took {1} seconds to complete".format(function.__name__, difference.total_seconds())
            with open(filename, 'a') as the_file:
                the_file.write(message +  os.linesep)
            return result

        return wrapper
    return real_decorator

