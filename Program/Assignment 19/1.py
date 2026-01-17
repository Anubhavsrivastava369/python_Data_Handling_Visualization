s = input('Enter a string:')
for e in s:
   print(e,' ',ord(e))

vowel = "AEIOUaeiou"

count = 0
for ch in s:
   if ch in vowel:
    count+=1
print('vowel is',count)