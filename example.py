#!/usr/bin/env python3

from parser import Parser

_psr = Parser()
_psr.add_argument("-h" , "--help", help_ ="show help message")
_psr.add_argument("-l" , "--low", help_ = "hello message")
_psr.add_argument("-p" , "--pizza", help_ = "hello pizza")
_psr.add_argument("-m" , "--music", help_ = "hello music")

@_psr.parse("-h" , "--help")
def help():
    _psr.help_message()

@_psr.parse("-l" , "--low")
def sathello():
    print("Hello World")

@_psr.parse("-p" , "--pizza")
def pizza():
    print("Hello pizza")
    #print(parser.values["-p"])


@_psr.parse("-m" , "--music")
def music():
    print("Hello music")

#print(_psr.my_args)
if __name__ == "__main__":
    if len(_psr.args) < 2:
        _psr.help_message()
    pizza()
    sathello()
    music()
    help()