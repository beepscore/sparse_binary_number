# Purpose
Given a "sparse number", find the next bigger one.

# References
Supposedly this was an interview question at Amazon.
http://www.careercup.com/question?id=5186975457869824

# Results

## Background
Define a "sparse number" as an integer whose binary digit 1s have no adjacent 1s.
See unit tests for example sparse numbers and expected next sparse numbers.

## Assumptions
Assume number is >= 0.
Initially, ignore integer maximum size and potential rollover.

0b1 is an edge case, could choose to define it either way.
Per problem statement define it as sparse.

## How to run unit tests
In terminal, cd to top level directory that contains subdirectory test

    $ python3 -m unittest discover test
    ............
    Ran 12 tests in 0.003s
