def visokosniy(got):
  if (got % 4 == 0 and got % 100 != 0) or (got % 400 == 0):
    return True
  else:
    return False
got = int(input()) 
if visokosniy(got):
  print("YES")
else:
  print("NO")