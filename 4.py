def reverse(a):

  if len(a) <= 1:
    return a
  else:
    return reverse(a[1:]) + a[0]

b = input()
c = reverse(b)
print(c)