
class Counter:

    @staticmethod
    def count_words(words):
        result = []
        for i in range(len(words)):
            count = 0
            for j in range(len(words)):
                if words[i] == words[j]:
                    count += 1
                if j == len(words)-1:
                    tmp = [words[i], count]
                    result.append(tmp)
        return result

    @staticmethod
    def count_letters(letters):
        result = []
        for i in range(len(letters)):
            count = 0
            upper_count = 0
            for j in range(len(letters)):
                if letters[i].lower() == letters[j].lower():
                    count += 1
                    if letters[j].isupper():
                        upper_count += 1
                if j == len(letters) - 1:
                    tmp = [letters[i], count, upper_count, str(count/len(letters)*100)+"%"]
                    result.append(tmp)
        return result