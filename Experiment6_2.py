text = input("Enter a string: ")

if text:
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    max_char = max(freq, key=freq.get)
    print(f"The most frequent character is '{max_char}' appearing {freq[max_char]} times.")
else:
    print("Empty string entered.")
