def count_pronouns():
    book = open("Pride_and_prejudice .txt", "r")
    words = []
    for line in book:
        words.append(line.split())
    book.close()
    pronouns = {
        "he": 0,
        "she": 0,
        "him": 0,
        "her": 0,
        "his": 0,
        "himself": 0,
        "herself": 0
    }
    for line_of_words in words:
        for word in line_of_words:
            compare = word.lower()
            if (compare in pronouns):
                pronouns[compare] = pronouns.get(compare) + 1

    male_total = pronouns.get("he") + pronouns.get("him") + pronouns.get("his") + pronouns.get("himself")

    female_total = pronouns.get("she") + pronouns.get("her") + pronouns.get("herself")
    
    print(male_total)
    print(female_total)


count_pronouns()