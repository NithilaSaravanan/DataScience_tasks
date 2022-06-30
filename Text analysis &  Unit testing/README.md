
NOTE:

1. Verbosity metric - Calculates the fraction of speech acts spoken by a pony over speech acts spoken by all ponies

2. Mention metric - Calculates the fraction of mentions of other ponies by a pony ( 1 mention per dialog if pony hs been properly mentioned - irrespective of # words referencing the pony - CONFIRMED on Oct 2 (Professor's Office Hours)

3. Follow On Comments metric - Calculates the fraction of the # times a pony speaks after another pony

4. Non Dictionary words - Finds out the top 5 words spoken by each pony that is not present in words_alpha.txt file

5. Unit Testing has been done by taking a random sample of the given dataset and then the columnvalues were shuffled randomly and then certain metrics were calculated using EXCEL and TABLEAU, which are then also calculated using the functions - ALL UNIT TESTS PASS

6. CLI Function assumes that the filename will be given with a proper extension
