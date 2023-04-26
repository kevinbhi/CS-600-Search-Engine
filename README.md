# CS-600-Search-Engine

## Search Engine
This is a word search engine implemented in Python3 that returns the number of occurrences of a word in input files. The number of hits of a word in a file is used as the ranking criteria, having the files with more occurrences listed on top compared to the once with lower hits.

## Implementation
The input texts are read from downloaded html files. The program can be started with specifying the input folder. All .htm and .html files from that folder will be indexed. The content of each file is read and the words, excluding the words listed in stopwords.txt will be indexed using a trie.

The splitting of the content extraction of words is done using beautifulsoup module (bs4) for Python. Only full words are indexed. That is sampleword and sampleword's will be indexed as differently.

The trie implementation is in trie.py. The trie will have nodes for each characters in the words and also every node will have data about number of times the word is found in each file. That is the counts in each node indicates the number of occurrences of the word formed by traversing the trie from root till that node. The lookup function of the trie implementation will return the result as a map with files as keys and hit count as values. This result is sorted for display using pythons sorted() method and passing custom key comparator which sorts based on the hit cunt, in reverse order. The result is displayed using tabulate package for python.

## Running
The program can be run with python3 (python in windows environment). First the dependencies should be installed using pip3

pip3 install -r requirements.txt

then

python(3) app.py

## Sample session from the app

D:\CS-600-Search-Engine>
D:\CS-600-Search-Engine>python app.py
Starting app
Indexing
# D:\CS-600-Search-Engine\data\Babar_Azam.html
# D:\CS-600-Search-Engine\data\Joe_Root.html
# D:\CS-600-Search-Engine\data\Kane_Williamson.html
# D:\CS-600-Search-Engine\data\Rohit_Sharma.html
# D:\CS-600-Search-Engine\data\Virat_Kohli.html
Indexing complete
Enter word to search. Press CTRL+C to quit: india
┌─────────┬───────────────────────────────────────────────────┬──────────────┐
│   Index │ File                                              │   Occurrence │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       0 │ D:\CS-600-Search-Engine\data\Virat_Kohli.html     │          235 │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       1 │ D:\CS-600-Search-Engine\data\Rohit_Sharma.html    │           62 │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       2 │ D:\CS-600-Search-Engine\data\Joe_Root.html        │           19 │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       3 │ D:\CS-600-Search-Engine\data\Kane_Williamson.html │            9 │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       4 │ D:\CS-600-Search-Engine\data\Babar_Azam.html      │            7 │
└─────────┴───────────────────────────────────────────────────┴──────────────┘
Enter word to search. Press CTRL+C to quit:
Empty word. Try again
Enter word to search. Press CTRL+C to quit: sharma
┌─────────┬───────────────────────────────────────────────────┬──────────────┐
│   Index │ File                                              │   Occurrence │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       0 │ D:\CS-600-Search-Engine\data\Rohit_Sharma.html    │          150 │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       1 │ D:\CS-600-Search-Engine\data\Virat_Kohli.html     │           30 │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       2 │ D:\CS-600-Search-Engine\data\Babar_Azam.html      │            2 │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       3 │ D:\CS-600-Search-Engine\data\Joe_Root.html        │            1 │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       4 │ D:\CS-600-Search-Engine\data\Kane_Williamson.html │            1 │
└─────────┴───────────────────────────────────────────────────┴──────────────┘
Enter word to search. Press CTRL+C to quit: australia
┌─────────┬───────────────────────────────────────────────────┬──────────────┐
│   Index │ File                                              │   Occurrence │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       0 │ D:\CS-600-Search-Engine\data\Virat_Kohli.html     │           34 │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       1 │ D:\CS-600-Search-Engine\data\Joe_Root.html        │           20 │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       2 │ D:\CS-600-Search-Engine\data\Babar_Azam.html      │           14 │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       3 │ D:\CS-600-Search-Engine\data\Rohit_Sharma.html    │           12 │
├─────────┼───────────────────────────────────────────────────┼──────────────┤
│       4 │ D:\CS-600-Search-Engine\data\Kane_Williamson.html │            8 │
└─────────┴───────────────────────────────────────────────────┴──────────────┘
Enter word to search. Press CTRL+C to quit:
