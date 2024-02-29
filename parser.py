#!/usr/bin/env python3

# import the necessary module for argument parsing
import sys

class ParserError(Exception):
    pass
# define the Parser class
class Parser(object):
    # initialize the Parser object with a description, banner, and custom help message
    def __init__(self, description: str = "", banner: str = "", my_own_help_msg: str = None) -> None:
        # store the command line arguments in a list
        self.args: list[str] = sys.argv
        # initialize an empty list to store the custom arguments
        self.my_args: list[str] = []
        # store the banner and custom help message
        self.banner = banner
        self.my_help_message = my_own_help_msg
        # store the description
        self.description = description
        # initialize an empty dictionary to store the argument values
        self.values = {}
    # define a decorator function to check if the custom argument is present in the command line arguments
    def add_argument(self, *args_: tuple, help_: str = "", need_value: bool = False) -> None:
    #def parse(self, *args_: str):
        self.my_args.append(tuple(args_) + (help_,))
        # define the decorator function
        def decf(fn):
            # define the wrapper function
            def wrapper(*ar, **kw):
                # if any of the specified arguments are present in the command line arguments, call the function
                if any(val in self.args for val in args_ if len(args_) > 1):
                    if need_value:
                        try :
                            if self.args[args_.index(args_[0]) + 2].startswith("-") :
                                raise ParserError
                            self.values.update((_arg , self.args[args_.index(args_[0]) + 2]) for _arg in list(args_) )#if len(args_) > 1 else args_[0])
                            fn( self.values[list(args_)[0]], *ar, **kw)
                        except IndexError :
                            raise ParserError
                    else :
                        fn(*ar, **kw)
            # return the wrapper function
            return wrapper
        # return the decorator function
        return decf

    # print the help message for the Parser object
    def help_message(self) -> None:
        # define the message before the custom arguments
        before_message: str = f"usage : {self.args[0]} [ARGUMENTS]"
        # print the banner, description, and message before the custom arguments
        print(self.banner)
        print(self.description)
        print(before_message + "\n")
        # iterate over the custom arguments
        for *_arg, _help in self.my_args:
            # print the argument and its help message
            print(",".join(_arg), end="\t")
            print(_help)
