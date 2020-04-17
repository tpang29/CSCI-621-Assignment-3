# CSCI-621: Programming Languages | Assignment 3

- Using the provided pseudo-code in [assignment-3-description](https://github.com/tpang29/CSCI-621-Assignment-3/blob/master/assignment-3-description.pdf), implement a non-recursive predictive parser in Python.

# Usage

## Setup
- Python 3.x required
- Download the folder titled `src`
- Navigate into the `src` directory
- Verify that `driver.py`, `parser.py`, and `errors.py` exist

## Run
- `python driver.py "input_string"` or `python3 driver.py "input_string"`
- You must specify an input string as a command line argument(#Demo) below.

# Understanding
- This program implements the parse table in the [assignment-3-description](https://github.com/tpang29/CSCI-621-Assignment-3/blob/master/assignment-3-description.pdf) through an adjacency list of nested dictionaries. 
- The outer key represents the row (nonterminal) from the parse table
- The inner key represents the column (terminal) from the parse table
- The value of each inner key is a particular cell in the parse table, where outer key (nonterminal) is the left-hand side of a production rule and the value (zero or more terminals and nonterminals) is the right-hand side of a production rule
- The output for this program will be the series of production rules applied to the given input string.
- An empty list represents a production rule in which epsilon is the only terminal on the right-hand side

# Demo
- Given incorrect arguments
```
User-MacBook-Pro:src username$ python3 driver.py 
Usage: python3 driver.py "input_string"
```
- Given correct arguments
```
User-MacBook-Pro:src username$ python3 driver.py "2^2^3"
elist -> ['e', 'elist`']
e -> ['n', 'e`']
n -> ['2', 'n`']
n` -> []
e` -> ['^', 'e']
e -> ['n', 'e`']
n -> ['2', 'n`']
n` -> []
e` -> ['^', 'e']
e -> ['n', 'e`']
n -> ['3', 'n`']
n` -> []
e` -> []
elist` -> []
```