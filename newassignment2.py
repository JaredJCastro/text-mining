import sys
from unicodedata import category
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def process_file(filename):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='utf8')

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=True):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.

    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is True, do not include any stopwords in the list.

    returns: list of (frequency, word) pairs
    """
    t = []

    stopwords = process_file('data/stopwords.txt')

    stopwords = list(stopwords.keys())
    # print(stopwords)

    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        t.append((freq, word))

    t.sort(reverse=True)
    return t


def print_most_common(hist, num):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    for freq, word in t[:num]:
        print(word, '\t', freq)

def sent_analysis_yellow():
    """conducts sentiment analysis on 20 most common words in Yellow Wallpaper"""
    common_words = ['john','one','said','don\t','can','see','room','pattern','get','paper','now','like','little','just','think','much','good','well','know','go']
    for i in common_words:
        score = SentimentIntensityAnalyzer().polarity_scores(i)
        print(score)

def sent_analysis_wendigo():
    """conducts sentiment analysis on 20 most common words in Wendigo"""
    common_words = ['defago','simpson','like','fire','hank','time','though','voice','something','little','upon','yet','feet','man','cathcart','tent','even','seemed','camp']
    for i in common_words:
        score = SentimentIntensityAnalyzer().polarity_scores(i)
        print(score)

def sent_analysis_jekyll():
    """conducts sentiment analysis on 20 most common words in Dr. Jekyll"""
    common_words = ['said','utterson','mr','hyde','jekyll','one','man','lawyer','will','now','poole','upon','stir','like','well','door','life','see','even','hand']
    for i in common_words:
        score = SentimentIntensityAnalyzer().polarity_scores(i)
        print(score)


def main():
    hist1 = process_file('data/Yellow Wallpaper.txt')
    print('Total number of words in The Yellow Wallpaper:', total_words(hist1))
    print('Number of different words in The Yellow Wallpaper:', different_words(hist1))
    print('The most common words in Yellow Wallpaper are:')
    print_most_common(hist1, 20)
    print("Sentiment scoring on the 20 most common words in The Yellow Wallpaper are as follows:")
    sent_analysis_yellow()

    hist2 = process_file('data/Wendigo.txt')
    print('Total number of words in Wendigo:', total_words(hist2))
    print('Number of different words in Wendigo:', different_words(hist2))
    print('The most common words in Wendigo:')
    print_most_common(hist2, 20)
    print("Sentiment scoring on the 20 most common words in Wendigo are as follows:")
    sent_analysis_wendigo()

    hist3 = process_file('data/Dr. Jekyll.txt')
    print('Total number of words in Dr. Jekyll:', total_words(hist3))
    print('Number of different words in Dr. Jekyll:', different_words(hist3))
    print('The most common words in Dr. Jekyll:')
    print_most_common(hist3, 20)
    print("Sentiment scoring on the 20 most common words in the text are as follows:")
    sent_analysis_jekyll()


if __name__ == '__main__':
    main()