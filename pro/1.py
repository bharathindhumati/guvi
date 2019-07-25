number=int(input())
starts=input()
for i in range(number-1):
  end=input()
  lengths=len(end)
  if len(starts)<len(end):
      lengths=len(starts)
  for j in range(lengths):
      if(starts[j] != end[j]):
          starts=starts[:j]
          break
print(starts)
