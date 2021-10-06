strikacky = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."
all_freq = {}
def charFrequency(veta):

    for i in veta:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
charFrequency(strikacky)
print ("Count of all characters in GeeksforGeeks is :\n " + str(all_freq))