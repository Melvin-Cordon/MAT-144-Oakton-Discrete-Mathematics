def noThreeOsStrings(length):
  
  s = [ "0", "1"]
  o = []

  if length > 1:
    s = noThreeOsStrings(length-1)

  if length > 1:
    for item in s:

      p = str(item) + "0"
      if not "000" in p:
        o.append(str(item) + "0")

      o.append(str(item) + "1")

    s = o
    o = []
    
  return s


#test cases
print(noThreeOsStrings(3))
print('\n')
print(noThreeOsStrings(4))
print('\n')
print(noThreeOsStrings(6))
print('\n')
print(noThreeOsStrings(8))
