import math
from functools import reduce

# This function is used to populate the dictionary with all possible words that can be generated from the set of words
def recurseOver(wordDictionary, words, cur_distance):
  
  # For each position in the dictionary, we are adding/subtacting all possible words that can be generated from the set of words
  for positions in list(wordDictionary.keys()):
    for word in words:

      # Adding the word from the set to the current word
      if positions + word not in wordDictionary:
        wordDictionary[positions + word] = cur_distance

      # Make sure we aren't adding a negative distance to the dictionary
      if positions - word not in wordDictionary and positions - word >= 0:
        wordDictionary[positions - word] = cur_distance

# X is a set of integers
def wordMetric(words, n):

  # If the greatest common divisor of the words is not 1, then it is not possible to generate all numbers and is not the case we care about
  if reduce(math.gcd, words) != 1:
    return -1

  # We are adding all the words in our set with a distance of 1
  wordDictionary = {y: 1 for y in words}

  # Start out by having an initial distance of 2 (we already added all possible word of distance 1)
  cur_distance = 2

  # M is the highest possible unique distance that doesn't just take the max step back to calculate. This was proved in our research paper
  # lastWord is the last word we added to the dictionary
  M, lastWord = 0, -1

  # maxWord is the maximum word in the set. i.e. words = {2, 7} maxWord = 7
  maxWord = max(words)
  
  # Calculating M
  for x in words:
    if lastWord == -1:
      lastWord = x
    else:
      M += lastWord * (lastWord + x) / 2
      lastWord = x
  M += lastWord
  counter = n

  # Populating the dictionary until we have all the distances <= M
  while (len(wordDictionary) < M):
    recurseOver(wordDictionary, words, cur_distance)
    cur_distance += 1
    counter -= maxWord + 1

  # Taking the distance of the biggest word to just above M
  total_steps = math.floor(n - M) % maxWord
  n -= (total_steps * maxWord)

  # If the number is one step outside of the word dictionary take a step into the dictionary
  while (n not in wordDictionary):
    n = n - maxWord
    total_steps += 1

  # Return the excess steps calculated added to the distance of the current number (n) in the word dictionary
  return wordDictionary[n] + total_steps

# Test cases
print(wordMetric({2, 4, 5, 7}, 18023))
