def analyze_text(text):
    vowel = "aeiou"

    count_vowel = 0
    count_consonant = 0
    count_upper = 0
    count_lower = 0

    # word list
    words_list = text.lower().split()

    freq = {}

    # character analysis
    for ch in text:
        if ch.isalpha():
            if ch.lower() in vowel:
                count_vowel += 1
            else:
                count_consonant += 1

            if ch.isupper():
                count_upper += 1
            elif  ch.islower():
                count_lower += 1

    # word frequency
    for word in words_list:
        word = word.strip()

        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return count_vowel, count_consonant, count_upper, count_lower, freq


def show_report(vowel, consonant, upper, lower, freq):
    print("\n TEXT ANALYZER REPORT")
    print("------------------------")
    print("Vowels:", vowel)
    print("Consonants:", consonant)
    print("Uppercase Letters:", upper)
    print("Lowercase Letters:", lower)

    # top 3 frequent words
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    print("\n Top 3 Frequent Words:")
    for word, count in sorted_freq[:3]:
        print(word, ":", count)


# MAIN PROGRAM
text = input("Enter text: ")

vowel, consonant, upper, lower, freq = analyze_text(text)

show_report(vowel, consonant, upper, lower, freq)