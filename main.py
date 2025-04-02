from collections import Counter, deque

def find_unique_char(string):
  if not string:
    return "Invalid string"

  char_counter = Counter(string)
  
  for k, v in char_counter.items():
    if v == 1:
      return k
    
  return -1

def merge_intervals(intervals):
  if not intervals:
      return []
    
  intervals.sort(key=lambda x: x[0])
  merged = [intervals[0]] 

  for start, end in intervals[1:]:
    last_end = merged[-1][1]

    if start <= last_end:
        merged[-1][1] = max(last_end, end)  
    else:
        merged.append([start, end])

  return merged

def ladder_length(first_word, second_word, word_list):
    word_set = set(word_list)

    if second_word not in word_set: 
        return 0

    queue = deque([(first_word, 1)]) 

    while queue:
        word, steps = queue.popleft()

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]

                if new_word == second_word:
                    return steps + 1
                
                if new_word in word_set:  
                    queue.append((new_word, steps + 1))
                    word_set.remove(new_word)

    return 0 
   

if __name__ == "__main__":
  #Exercise 1
  print("Exercise 1\n")
  print(find_unique_char("")) #Expected: Invalid string
  print(find_unique_char("abacabad")) #Expected: c
  print(find_unique_char("aaabb")) #Expected: -1
  print(find_unique_char("cccccccccccbd")) #Expected: b
 
  #Exercise 2
  print("-------------------------------------------------")
  print("Exercise 2\n")
  print(merge_intervals([[1,3], [8,10], [15,18], [2,6]])) #Expected: [[1, 6], [8, 10], [15, 18]]
  print(merge_intervals([[1,4], [4,5]])) #Expected: [[1, 5]]
  print(merge_intervals([[5, 10], [1, 3], [2, 6], [15, 18], [12, 14], [8, 11]])) #Expected: [[1, 11], [12, 14], [15, 18]]

  #Exercise 3
  print("-------------------------------------------------")
  print("Exercise 3\n")
  print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"])) #Expected: 5
  print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log"])) #Expected: 0