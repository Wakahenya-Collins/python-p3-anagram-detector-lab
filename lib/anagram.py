# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        anagrams = []
        for candidate in word_list:
            if self.is_anagram(candidate.lower()):
                anagrams.append(candidate)
        return anagrams

    def is_anagram(self, candidate):
        return sorted(candidate) == sorted(self.word) and candidate != self.word
