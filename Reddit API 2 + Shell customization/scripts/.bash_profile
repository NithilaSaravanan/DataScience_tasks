#!/bin/bash

head -$((${RANDOM} % `wc -l < ~/.data/quotes.csv` + 2)) ~/.data/quotes.csv | tail -1 > quotefile

author=$(cut -d, -f1 quotefile)

blank=''
signquote=\"
signcomma=,
signspace=' '

quote=$(head -n 1 quotefile)
quote=${quote/$author/}
quote=${quote/$signcomma/$signspace}

author=${author/$signquote/}
author=${author/$signquote/}

echo -e "\n"$quote
echo -e "\t~" $author"\n"
rm quotefile
