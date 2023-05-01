#!/usr/bin/env python3

import os
import argparse
import random as rd

class SplitterParser(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(
            prog="Splitter",
            description="Split flist in train, test, val",
        )
        self.define_args()

    def define_args(self):
        self.add_argument(
            "-t",
            "--train",
            default=0.7,
            action="store",
            type=float,
            help="Set the proportion of train files",
        )

        self.add_argument(
            "-T",
            "--test",
            default=0.15,
            action="store",
            type=float,
            help="Set the proportion of test files",
        )

        self.add_argument(
            "-v",
            "--val",
            default=0.15,
            action="store",
            type=float,
            help="Set the proportion of val files",
        )

        self.add_argument(
            "-f",
            "--file",
            action="store",
            type=str,
            help="Emplacement of the flist file",
            required=True,
        )

        self.add_argument(
            "-o",
            "--output",
            action="store",
            type=str,
            help="Folder for flist output",
            required=True,
        )



def splitter():
    args = SplitterParser().parse_args()

    with  open(args.file, "r") as f:
        lines = f.readlines()

    n = len(lines)

    n_train = int(args.train * n)
    n_test = int(args.test * n)
    n_val =  int(n - n_train - n_test)

    assert n > 0
    assert n_train >= 0
    assert n_test >= 0
    assert n_val >= 0

    l_train = []
    l_test = []
    l_val = []

    for _ in range(n_train):
        l_train.append(lines.pop(rd.randint(0, len(lines) - 1)))

    for _ in range(n_test):
        l_test.append(lines.pop(rd.randint(0, len(lines) - 1)))

    for _ in range(n_val):
        l_val.append(lines.pop(rd.randint(0, len(lines) - 1)))

    with open(f"{args.output}/train.flist", "w") as f:
        print(*l_train, sep="\n", file=f)

    with open(f"{args.output}/test.flist", "w") as f:
        print(*l_test, sep="\n", file=f)

    with open(f"{args.output}/val.flist", "w") as f:
        print(*l_val, sep="\n", file=f)


if __name__ == "__main__":
    splitter()
