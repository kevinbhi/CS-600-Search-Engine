import os
import tabulate
import argparse
from trie import WebSearchTrie


def main(srcdir, stop_words_file):

    srcdir = srcdir or os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
    stop_words_file = stop_words_file or os.path.join(os.path.dirname(os.path.realpath(__file__)), "stopwords.txt")

    if not os.path.isdir(srcdir):
        print("Invalid directory")
        return

    if not os.path.isfile(stop_words_file):
        print("Invalid stop words directory")
        return

    files = []
    for f in os.listdir(srcdir):
        if os.path.isfile(os.path.join(srcdir, f)) and (f.endswith(".html") or f.endswith(".htm")):
            files.append(os.path.join(srcdir, f))

    print("Starting app")

    search_trie = WebSearchTrie(files=files, stop_words_file=stop_words_file)

    print("Indexing")

    search_trie.index()

    print("Indexing complete")

    while True:
        word = input("Enter word to search. Press CTRL+C to quit: ")
        if not word.strip():
            print("Empty word. Try again")
            continue
        result = search_trie.lookup(word.lower())
        result_list = sorted([[k, v] for k, v in result.items()], key=lambda t: t[1], reverse=True)
        table = []
        for index, row in enumerate(result_list):
            table.append([index, row[0], row[1]])
        print(tabulate.tabulate(table, headers=["Index", "File", "Occurrence"], tablefmt="simple_grid"))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--input-directory', required=False)
    parser.add_argument('-s', '--stop-words-file', required=False)

    args = parser.parse_args()

    try:
        main(args.input_directory, args.stop_words_file)
    except KeyboardInterrupt:
        print("\nInterrupted\n")
    except Exception as e:
        print("Exception running search engine app:", type(e), e)