s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")


s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print("Not Anagram")
else:
    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch not in freq:
            print("Not Anagram")
            break
        freq[ch] -= 1
    else:
        print("Anagram")