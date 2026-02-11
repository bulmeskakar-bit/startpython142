# print('пример1')
# for x in 0, 1:
#  for y in 0, 1:
#   for z in 0, 1:
#    for w in 0, 1:
#     F = (x or y) and not(y == z) and not(w)
#     if F == 1:
#      print(x, y, z, w, F)
#
# print(f'Пример 2')
# for x in 0, 1:
#  for y in 0, 1:
#   for z in 0, 1:
#    for w in 0,1:
#     F = (x or y) and not(y == z) and not(w)
#     print(x, y, z, w, F)

print('пример 3')
for a in 0, 1:
 for b in 0, 1:
  for c in 0, 1:
    F = not (a or b) and c
    if F == 1:
     print(a, b, c, F)

print('пример 4')
for x in 0, 1:
 for y in 0, 1:
  for z in 0, 1:
      F = not(x) or not(y) <= z
      if F == 1:
          print(x, y, c, F)

print('пример 5')
for s1 in 0, 1:
 for s2 in 0, 1:
  for s3 in 0, 1:
      F = s1 and not(s2) or s3
      if F == 1:
          print(s1, s2, s3, F)

print('пример 6')
for x in 0, 1:
 for y in 0, 1:
  for z in 0, 1:
      F = not(x) == y or z
      if F == 1:
          print(x, y, c, F)

print('пример 7')
for a in 0, 1:
 for b in 0, 1:
  for c in 0, 1:
      F = a <= b or not(c)
      if F == 1:
          print(a, b, c, F)

print('пример 8')
for x1 in 0, 1:
 for x2 in 0, 1:
  for x3 in 0, 1:
      F = not(x1) and not(x2) or x1 and x3
      if F == 1:
          print(x1, x2, x3, F)

print('пример 7')
for a in 0, 1:
 for b in 0, 1:
  for c in 0, 1:
      F = a and not(c) == not(a and b)
      if F == 1:
          print(a, b, c, F)
