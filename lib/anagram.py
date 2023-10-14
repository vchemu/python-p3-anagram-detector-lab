# your code goes here!
class Anagram:
  def __init__(self, word):
    self.word = sorted([character for character in word])

  def match(self, words):
    match_list = []
    for word in words:
      if sorted([character for character in word]) == self.word:
        match_list.append(word)
    return match_list