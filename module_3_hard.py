data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def count(i):
  if type(i) == int:
    current = i
  if type(i) == str:
    current = len(i)
  return current
def solution(data):
  for i in data:
    if not i:
      if len(data)>1:
        return solution(data[1:])
      else:
        return 0
    if type(i) == dict:
      temp = []
      for n in (i.items()):
        temp.append(n)
      if len(data)>1:
        return solution(temp) + solution(data[1:])
      else:
        return solution(temp)
    if isinstance(i, (tuple, list, set)):
      if len(data)>1:
        return solution(i) + solution(data[1:])
      else:
        return solution(i)
    else:
      if len(data)>1:
        return count(i) + solution(data[1:])
      else:
        return count(i)
result = solution(data_structure)
print(result)