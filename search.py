import sys


def get_sentences_with_word(file_path, search_text):
    all_text = open(file_path).read()
    sentences = all_text.lower().split('.')

    founded_sentences = []

    for s in sentences:
        # .replace("\n", " ").replace("\r", " ")
        sentence = s.replace("\n", " ").replace("\r", " ").lstrip()
        sentence = sentence.rstrip()
        if sentence.find(search_text) != -1 and 2 <= sentence.count(' ') <= 10:
            founded_sentences.append(sentence.capitalize())

    return founded_sentences


def main():
    data_file_path = sys.argv[1]
    words_file_path = sys.argv[2]
    output_file = sys.argv[3]

    all_words = open(words_file_path).read()
    words = all_words.lower().split(',')

    dictionary = {}
    for word in words:
        dictionary[word] = get_sentences_with_word(data_file_path, word)

    output = open(output_file, 'w')
    for word, result in dictionary.items():
        # print(word + ':\n')
        # print("____________________________\n")
        output.write("____________________________\n")
        output.write(word + ':\n')
        # print(result)
        for r in result:
            # print(r + '.' + '\n')
            output.write(r + '.' + '\n')

    output.close()


if __name__ == "__main__":
    main()
