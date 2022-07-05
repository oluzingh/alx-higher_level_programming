#!/usr/bin/python3
def add_attribute(clas, name, first):
    if not hasattr(clas, name):
        raise TypeError("can't add new attribute")
    clas.name = first 
