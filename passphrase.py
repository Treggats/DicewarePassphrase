# -*- encoding: utf-8 -*-

from os.path import isfile, dirname, realpath

import random
import csv
import sys


class DicewarePassphrase(object):
    """
    DicewarePassphrase doc
    using the theory from diceware http://world.std.com/~reinhold/diceware.html
    Create a passphrase, generated at random.
    """
    def __init__(self, wordlist_file="diceware.wordlist.asc"):
        self.wordlist = None
        if not isfile(wordlist_file):
            path = realpath(__file__)
            dir_path = dirname(path)
            wordlist_file = "{}/{}".format(dir_path, wordlist_file)
        if not isfile(wordlist_file):
            exit("file does not exist")
            sys.exit()
        else:
            """Open the wordlist and store it in memory"""
            self.diceware = {}
            """Open a diceware wordlist"""
            self.wordlist = open(wordlist_file)
            self.reader = csv.reader(self.wordlist, delimiter="\t",
                            quotechar="\n")
            for line in self.reader:
                self.diceware[line[0]] = line[1]

    def __del__(self):
        if self.wordlist:
            """Close the wordlist file"""
            self.wordlist.close()

    def _create_word(self):
        """Generate a number, which is used as index
        for the wordlist"""
        number = ""
        for i in range(5):
            number += "{}".format(random.randrange(1, 6))
        return self.diceware[number]

    def passphrase(self, words=7):
        """Generate a passphrase, consisting of x words"""
        phrase = self._create_word()
        for i in range(words - 1):
            phrase += " {}".format(self._create_word())
        return phrase

