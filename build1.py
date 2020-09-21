#!/usr/bin/env python

import random

head = ["head of a bear",
        "head of a cat",
        "head of a stork",
        "head of an elephant",
        "head of a roswell alien",
        "head of a fish",
        "head of a dragon",
        "head of a dog",
        "head of a cow",
        "head of a human female",
        "head of a human male",
        "head of an indescribable void",
        "head of a shark"
        ]

arms = ["clawed arms",
        "lobster pinchers",
        "tentacle arms",
        "bat wings",
        "eagle wings",
        "beefy human arms",
        "scrawny human arms",
        "praying mantis arms",
        "three pairs of arms"
        ]

body = ["body of a fish",
        "cephalothorax of an insect",
        "body of an octopus",
        "body of a female human",
        "body of a male human",
        "body of a bird",
        "body of a horse",
        "body of a giraffe",
        "body of a turtle",
        "body of a frog"
        ]

extra = ["and has a fish tail",
        "and is covered with fur",
        "and is covered with feathers",
        "and wearing a top coat and tails",
        "with huge antennae",
        "and is covered in slime",
        "and is doing their taxes"
        ]

print("Creature has a {0}, {1}, the {2}, {3}.".format(random.choice(head),random.choice(arms),random.choice(body),random.choice(extra)))
