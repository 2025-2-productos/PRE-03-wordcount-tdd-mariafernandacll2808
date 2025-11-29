import sys

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_into_words import split_into_words
from ._internals.write_word_counts import write_word_counts


def parse_args(args=None):
    if args is None:
        args = sys.argv[1:]

    if len(args) != 2:
        raise ValueError(
            "Must provide exactly 2 arguments: input_folder and output_folder"
        )

    input_folder, output_folder = args

    # Asegurar slash final
    if not input_folder.endswith("/"):
        input_folder += "/"
    if not output_folder.endswith("/"):
        output_folder += "/"

    return input_folder, output_folder


def main():
    input_folder, output_folder = parse_args()
    ## read all lines
    all_lines = read_all_lines(input_folder)

    ### preprocess lines
    all_lines = preprocess_lines(all_lines)

    ### split in words
    words = split_into_words(all_lines)

    ### count words
    counter = count_words(words)

    ### write word counts
    write_word_counts(counter, output_folder)


if __name__ == "__main__":
    main()
