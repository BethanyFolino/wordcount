# Word Count
Word Count is a program that opens a txt file and counts the number of times each word appears in it. The --count flag does a basic count of how many times each word appears in a txt file. The --topcount flag prints a list of the top 20 most frequent words in a txt file in descending order based on frequency of appearance. I made it as part of Kenzie Academy's software engineering program. The txt files and tests were supplied by Kenzie Academy staff.

## Usage
```python
python wordcount.py --count books/alice.txt
# prints each word in order it appears in alice.txt next to the number of times it appeared

python wordcount.py --topcount books/alice.txt
# prints the top 20 most frequent words in alice.txt in descending order based on frequency
# of appearance
```
