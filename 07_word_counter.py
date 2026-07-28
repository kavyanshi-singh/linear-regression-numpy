x=input("What's the sentence? ")

print(len(x.split()))
print(len(x))
vowel=0

for letter in x.lower():
    if letter in "aeiou":

        vowel+=1

print("number of vowels:",vowel)

   
    
       




