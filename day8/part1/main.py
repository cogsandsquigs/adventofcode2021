inputs = open("input.txt", "r")
ans = sum(
  len(chars) in (2, 3, 4, 7)
  for line in inputs
  for chars in line.split('|')[1].strip().split()
)
print(f'Times do digits 1, 4, 7, or 8 appear: {ans}')