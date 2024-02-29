#!/usr/bin/env python3

from parser import Parser

_psr = Parser()

@_psr.add_argument("-h" , "--help", help_ ="show help message")
def help():
    _psr.help_message()

# if the argument have value u need to add parameter of value for your arg
@_psr.add_argument("-l" , "--low", help_ = "hello message" , need_value = True)
def sathello(value):
    print(value)
    print("hello world")

@_psr.add_argument("-p" , "--pizza", help_ = "hello pizza")
def pizza():
    print("Hello pizza")
    #print(parser.values["-p"])


@_psr.add_argument("-m" , "--music", help_ = "hello music")
def music():
    print("Hello music")

if __name__ == "__main__":
    if len(_psr.args) < 2:
        _psr.help_message()
    pizza()
    sathello()
    music()
    help()
