Assume that words.txt has the following content:

the day is sunny the the
the sunny is is

Your script should output the following, sorted by descending frequency:

the 4
is 3
sunny 2
day 1

# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s ' ' '\n'| sort | uniq -c | sort -r| awk '{print $2,$1}'