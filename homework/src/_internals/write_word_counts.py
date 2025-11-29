import os


def write_word_counts(counter, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # save the results using tsv format
    output_path = os.path.join(output_folder, "results.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
        for key, value in counter.items():
            # write the key and value to the file
            f.write(f"{key}\t{value}\n")

    output_path = os.path.join(output_folder, "wordcount.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
        for key, value in counter.items():
            # write the key and value to the file
            f.write(f"{key}\t{value}\n")
