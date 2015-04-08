# Purpose
Given a "sparse number", find the next bigger one.

# References
Supposedly this was an interview question at Amazon.
http://www.careercup.com/question?id=5186975457869824

# Results

## Background
Define a "sparse number" as an integer whose binary digit 1s have no adjacent 1s.

## Assumptions
Assume number is >= 0.
Initially, ignore integer maximum size and potential rollover.

0b1 is an edge case, could choose to define it either way.
Per problem statement define it as sparse.

## Manually list sparse numbers to observe pattern.

binary
power of 2
543210        as sum         decimal
------------------------------------
     0                0         0
     1              2^0         1
    10              2^1         2
   100              2^2         4
   101        2^2 + 2^0         5
  1000              2^3         8
  1001                          9
  1010                         10
 10000                         16
 10001        2^4 + 2^0        17
 10010        2^4 + 2^1        18
 10100        2^4 + 2^2        20
 10101  2^4 + 2^2 + 2^0        21
100000        2^5              32
100001
100010
100100
100101
101000
101001
101010
...

## Solution strategy
Add method is_sparse() to take an integer argument and return boolean.
Add tests.

### Brute force solution
Start with starting sparse number, increment until is_sparse.

### More efficient solution
Write method to generate sparse numbers.
Write method to take a sparse number and return the next sparse number.

## Run unit tests
To run tests in terminal, cd to top level directory that contains subdirectory test

    ➜  sparse_binary_number git:(master) ✗ python3 -m unittest discover test
    ........
    Ran 8 tests in 0.001s
