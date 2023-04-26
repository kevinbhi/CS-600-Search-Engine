import os
from bs4 import BeautifulSoup


class TrieNode():

    def __init__(self):
        self.links = {}
        self.results = {}


class WebSearchTrie():

    def __init__(self, files, stop_words_file="stopwords.txt"):
        self.files = files
        self.root = None
        self.stop_words = [l.strip().lower() for l in open(stop_words_file, encoding="utf-8").read().split() if l.strip()]

    def insert_to_trie(self, file, word):

        current = self.root

        if not word:
            print("Empty word insertion")
            return

        for chr in word:

            if chr not in current.links:

                current.links[chr] = TrieNode()

            current = current.links[chr]

        if file not in current.results:

            current.results[file] = 0

        current.results[file] += 1


    def lookup(self, word):

        if not word:
            print("Empty word lookup")
            return {}

        current = self.root

        for chr in word:
            if not chr in current.links:
                return {}
            current = current.links[chr]

        return current.results

    def index(self):

        self.root = TrieNode()

        for file in self.files:

            print("#", file)

            if not os.path.isfile(file):
                print("Invalid file send to index:", file)
                continue

            try:
                data = open(file, encoding="utf-8").read()
            except Exception as e:
                print("Exception reading file: {}\n{}: {}".format(file, type(e), e))
                continue

            soup = BeautifulSoup(data, "html.parser")

            words = [w.strip().lower() for w in soup.text.split() if w.strip()]

            for word in words:

                if word in self.stop_words:
                    continue

                self.insert_to_trie(file, word)
