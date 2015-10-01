import sys
from random import choice


class SimpleMarkovGenerator(object):
    chains = {}

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""
        result = " "
        for one_file in filenames:
            one_file = open(one_file)
            for line in one_file:
                line_in_file = line.strip()
                result += line_in_file
                self.make_chains(result)

            


    def make_chains(self, corpus):
        """Takes input text as string; stores chains."""

        words = corpus.split()
        for i in range(len(words) - 2):
                key = (words[i], words[i + 1])
                value = words[i + 2]

                if key not in self.chains:
                    self.chains[key] = []

                self.chains[key].append(value)

            # or we could say "chains.setdefault(key, []).append(value)"

        return self.chains


    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""
        key = choice(self.chains.keys())
        words = [key[0], key[1]]
        while key in self.chains:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text)
        #
        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

            word = choice(self.chains[key])
            words.append(word)
            key = (key[1], word)

        print " ".join(words)


if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x
    file_list = sys.argv[1:]
    print file_list
    generator = SimpleMarkovGenerator()
    generator.read_files(file_list)
    for i in range(5):
        generator.make_text()
        print i
