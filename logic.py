import math
from functools import reduce

def recurseOver(wordDictionary, words, n, M):
  for x in list(wordDictionary.keys()):
    for y in words:
      added = x + y
      subtracted = x - y
      if added <= M and added not in wordDictionary:
        wordDictionary[added] = n
      if subtracted >= 0 and subtracted <= M and subtracted not in wordDictionary:
        wordDictionary[subtracted] = n

def calculateM(words):
  M = 0
  lastWord = -1
  for x in words:
    if lastWord == -1:
      lastWord = x
    else:
      M += lastWord * (lastWord + x) / 2
      lastWord = x
  return M + lastWord

def populateDictionary(wordDictionary, words, counter, maxWord):
  M = calculateM(words)
  i = 2
  while (counter > M or len(wordDictionary) <= math.ceil(M)):
    recurseOver(wordDictionary, words, i, M)
    i += 1
    counter = counter - maxWord + 1

# wordMetric takes in a set of integers, words, and a target number, n
# wordMetric returns the number of coefficients that add up to n (the number of steps)
def wordMetric(words, n):
  # If the gcd of the set of words is not equal to 1, we return -1 as it is not a group
  if reduce(math.gcd, words) != 1:
    return -1
  # maxWord is the maximum number of the set
  maxWord = max(words)
  # This is our base case where we put in all the integers of words into our wordDictionary. For each word it only takes one step
  wordDictionary = {y: 1 for y in words}

  populateDictionary(wordDictionary, words, n, maxWord)


  i = 0

  # We can potentially make this shorter by doing n % maxWord
  while (n not in wordDictionary):
    n = n - maxWord
    i += 1
  return wordDictionary[n] + i
# Example of the set {2, 7} and the target number 1203
print(wordMetric({2, 7}, 1203))