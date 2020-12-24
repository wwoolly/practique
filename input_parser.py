import sys


def main():
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    all_words = open(input_file_path).read()
    words = ','.join(all_words.replace("(","").replace(")","").replace("-","").split())

    output = open(output_file_path, 'w')
    output.write(words)
    output.close()


if __name__ == "__main__":
    main()
