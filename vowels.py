##WAP to input string and print the count how many elements are greater than the average of the array


string =input("Enter Any String") 
vowels = "aeiouAEIOU"
 
count = sum(string.count(vowel) for vowel in vowels)
print("Occurance of Vowels",count)