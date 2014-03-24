#!/usr/bin/env python

from analyse import Analyse
import md5

def get_md5_from_file(filename):
    m = md5.new()
    with open(filename) as fh:
        m.update(fh.read())
    return m.digest()

def test_line():
    an = Analyse("images/IR_0485.jpg")
    an.analyseImage(0,0,100,100)

    assert get_md5_from_file("tmp/graph.png") == '\xdcu\x87\x935\x9f\xa6\xa9HX\xe9j\x89C\xa9\xd8', "wrong md5sum"
    assert get_md5_from_file("tmp/line.png") == '_\x93\xb3E\xd3\x11`|\x90\xde"!q\xaa\xd9\xf2', "wrong md5sum"

if __name__ == "__main__":
    test_line()
    print "tests ok"