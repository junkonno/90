Q = int(input())
l = [list(map(int, input().split())) for l in range(Q)]
deck = []
Answer = []

for i in range(Q):
  if l[i][0] == 1:
    deck.append(l[i][1])
  if l[i][0] == 2:
    deck.insert(0, l[i][1])
  if l[i][0] == 3:
    Answer.append(deck[-l[i][1]])
  
for item in Answer:
  print(item)