"""Count words."""
from collections import Counter
from re import split

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    counter = Counter()
    #print split(' ', s)
    counter.update(x for x in split(' ', s) if x)
    
    lst = counter.items()
    #print lst
    lst.sort(key=lambda k:(-k[1], k[0]), reverse=False)
    #print lst
    # TODO: Count the number of occurences of each word in s

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    top_n = list(lst[:n])
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
