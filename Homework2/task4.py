# Using input function ask user to enter a song name.
# 1. Print the first charachter of given song name.
# 2. Print the last charachter of given song name.
# 3. Print the length of the given song name.
# 4. Print the index number of "k" in this song name. 
# 5. Print the charachter from an index number of 3.
# 6. Print the song name in upper case.
# 7. Print the song name in lower case.

print("Please your favorite song name")
song=input()
first_ch=song[0]
print(first_ch)
last_ch=song[-1]
print(last_ch)
length=len(song)
print(length)
k=song.find("k")
print(k)
num3=song[3:4]
print(num3)
print(song.lower())
print(song.upper())