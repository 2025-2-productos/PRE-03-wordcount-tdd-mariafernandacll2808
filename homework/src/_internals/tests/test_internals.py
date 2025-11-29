import os
import shutil
import subprocess
import sys

from ...wordcount import parse_args
from ..count_words import count_words
from ..preprocess_lines import preprocess_lines
from ..read_all_lines import read_all_lines
from ..split_into_words import split_into_words
from ..write_word_counts import write_word_counts


# Función test_parse_args
def test_parse_args():
    try:
        subprocess.run(
            [sys.executable, "-m", "homework", "data/input", "data/output"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")

    input_folder, output_folder = parse_args(["data/input", "data/output"])

    assert input_folder == "data/input/"
    assert output_folder == "data/output/"


# Función test_read_all_lines
def test_read_all_lines():
    input_folder = "data/input/"
    lines = read_all_lines(input_folder)
    assert len(lines) > 0
    assert any(
        "Analytics refers to the systematic computational analysis of data" in line
        for line in lines
    )


# Función test_preprocess_lines
def test_preprocess_lines():
    lines = [" Hello, World!  ", "This is a Test.", " Preprocess THIS line! "]
    processed_lines = preprocess_lines(lines)
    expected_lines = ["hello, world!", "this is a test.", "preprocess this line!"]
    assert processed_lines == expected_lines


# Función test_split_into_words
def test_split_into_words():
    lines = ["hello, world!", "this is a test."]
    words = split_into_words(lines)
    expected_words = ["hello", "world", "this", "is", "a", "test"]
    assert words == expected_words


# Función test_count_words
def test_count_words():
    words = ["hello", "world", "hello", "test"]
    counter = count_words(words)
    assert counter["hello"] == 2
    assert counter["world"] == 1
    assert counter["test"] == 1


# Funcón test_write_word_counts
def test_write_word_counts():
    output_folder = "data/output/"
    word_counts = {"hello": 2, "world": 1, "python": 1}

    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)

    write_word_counts(word_counts, output_folder)

    output_file = os.path.join(output_folder, "wordcount.tsv")
    assert os.path.exists(output_file), "Output file was not created"

    with open(output_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert lines == ["hello\t2\n", "world\t1\n", "python\t1\n"]

    shutil.rmtree(output_folder)
