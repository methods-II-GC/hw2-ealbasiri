#!/usr/bin/env python
"""One-line description of the program goes here."""

 
import argparse
import random
from typing import Iterator, List

def main(args):
    def read_tags(path: str) -> Iterator[List[List[str]]]:
        with open(path, "r") as source:
            lines = []
            for line in source:
                line = line.rstrip()
                if line:  # Line is contentful.
                    lines.append(line.split())
                else:  # Line is blank.
                    yield lines.copy()
                    lines.clear()
# Just in case someone forgets to put a blank line at the end...
        if lines:
            yield lines
    corpus = list(read_tags(args.input_data))

    random.shuffle(corpus)
    random.seed(2010) 
    with open(args.train_path, "w") as sink1:
        train_set= corpus[:int(len(corpus)*0.80)]
        for listitem1 in train_set:
            for listitem2 in listitem1: 
                str1 = ''.join(listitem2)
                sink1.write('%s\n' % str1) 

    with open(args.dev_path, "w") as sink2:
        dev_set= corpus[int(len(corpus)*0.80):int(len(corpus)*0.9)]
        for listitem1 in dev_set:
           for listitem2 in listitem1:
               str2 = ''.join(listitem2)
               sink2.write('%s\n' % str2)
    
    with open(args.test_path, "w") as sink3:
        test_set= corpus[int(len(corpus)*0.9):] 
        for listitem1 in test_set:
           for listitem2 in listitem1:
               str3 = ''.join(listitem2) 
               sink3.write('%s\n' % str3)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_data",
    )
    parser.add_argument(
        "train_path",
        help="path to write the training set"
    )
    parser.add_argument(
        "dev_path",
        help="path to write the development set"
    )
    parser.add_argument(
        "test_path",
        help="path to write the testing set"
    )
    main(parser.parse_args())
