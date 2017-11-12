import nltk
import operator

class Analyzer():
    """Implements sentiment analysis.

    Expanded to include a personal interest analysis.

    """

    def __init__(self, positives, negatives, classics, arthistory, tech):
        """Initialize Analyzer."""

        # Iniitalise words lists
        self.positives = []
        self.negatives = []
        self.classics = []
        self.arthistory = []
        self.tech = []

        # Open positive words and add them to the positives list
        with open(positives) as positive_file:
            file_iter = (l for l in positive_file if not (l.startswith(';') or l.startswith('\n')))
            for line in file_iter:
                self.positives.append(line.rstrip())

        # Open negative words and add them to the negatives list
        with open(negatives) as negative_file:
            file_iter = (l for l in negative_file if not (l.startswith(';') or l.startswith('\n')))
            for line in file_iter:
                self.negatives.append(line.rstrip())

        # Open classics words and add them to the classics list
        with open(classics) as classics_file:
            file_iter = (l for l in classics_file if not (l.startswith(';') or l.startswith('\n')))
            for line in file_iter:
                self.classics.append(line.rstrip())

        # Open arthistory words and add them to the arthistory list
        with open(arthistory) as arthistory_file:
            file_iter = (l for l in arthistory_file if not (l.startswith(';') or l.startswith('\n')))
            for line in file_iter:
                self.arthistory.append(line.rstrip())

        # Open tech words and add them to the tech list
        with open(tech) as tech_file:
            file_iter = (l for l in tech_file if not (l.startswith(';') or l.startswith('\n')))
            for line in file_iter:
                self.tech.append(line.rstrip())

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # Initialise counter
        counter = 0

        # Tolkenise tweets
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)

        # Loop through words in token check whether it's positive or negative, and add or subtract from counter accordingly
        for word in tokens:
            if word.lower() in self.positives:
                counter +=1
            elif word.lower() in self.negatives:
                counter -= 1

        return counter

    def analyze2(self, text):
        """Analyze text for interests in classics, art history, and tech, returning its score."""

        # Initialise counters dict
        counters = {'classics': 0, 'arthistory': 0, 'tech': 0}

        # Tolkenise tweets
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)

        # Loop through words in token check whether it's classics, art history, or tech related, and add to counter accordingly
        for word in tokens:
            if word.lower() in self.classics:
                counters['classics'] +=1
            elif word.lower() in self.arthistory:
                counters['arthistory'] += 1
            elif word.lower() in self.tech:
                counters['tech'] += 1

        # If no words have been added to counter, return 'neutral'. Else, return the key with the maximum value
        if counters['classics'] == 0 and counters['arthistory'] == 0 and counters['tech'] == 0:
            return "neutral"
        else:
            return max(counters, key=lambda key: counters[key])
