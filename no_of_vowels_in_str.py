#Without using control flow statements
string = input("Enter a string: ")
vowels = "a e i o u A E I O U"
count = sum(map(string.count, vowels))
print("Number of vowels =", count)
