import os, json

longestWord = { "word": "", "length": 0 }
alphabeticalWords = []

for root, dirs, files in os.walk("../datasets"):
    for filename in files:
        with open(f"../datasets/{filename}") as file:
            words = file.readlines()

            for word in words:
                trimmedWord = word.strip()
                splitWord = []

                for char in trimmedWord:
                    splitWord.append(char)
                splitWord.sort()
                sortedWord = "".join(splitWord)

                if trimmedWord == sortedWord:
                    alphabeticalWords.append(trimmedWord)
                    if len(trimmedWord) > len(longestWord["word"]):
                        longestWord["word"] = trimmedWord
                        longestWord["length"] = len(trimmedWord)
                        
            print(f"{filename} \n - # of words searched: {len(words)} | # of alphabetical words: {len(alphabeticalWords)} | Longest word data: {json.dumps(longestWord)}")
        outputFile = open(f"../out/{filename.split('.')[0]}.PY.log", "w")
        # Gives error: f-string expression part cannot include a backslash... why python why
        # output = f"{'\n'.join(alphabeticalWords)}\n{longestWord['word']} | {longestWord['word']}"
        output = "\n".join(alphabeticalWords) + "\n" + f"{longestWord['word']} | {longestWord['length']}"
        outputFile.write(output)