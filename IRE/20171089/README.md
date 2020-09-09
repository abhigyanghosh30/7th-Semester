# IRE Mini Project 
## Phase 2
***Abhigyan Ghosh- 20171089***

### Conventions
#### Making the index
- To make the index, I first run the index.py code on each of the individual part-data files. To increase the parallel processing, I have used the UNIX command `&` to create multiple forks of a process each working on a different file
- It is a bit resource internsive but can be made less painful by reducing the number of processes we run in parallel.
- At the end we have __ind1.txt__ to __ind34.txt__ for each of the individual files. We also get __ind1.txtindex__ to __ind32.txtindex__ as a index for storing the title for each document id. To get the final totaltitle.txt, we can simply run `cat *title > totaltitle.txt`
- Note that each of __ind1.txt__ to __ind32.txt__ is a sorted index file. 

#### Merging the index
- We run `merge.sh` to merge the 34 ind files to one large 11GB index file first before splitting it. What it essentially does is use the merge algorithm for two sorted arrays to merge two files. `merge.py` does this for 2 files and `merge.sh` calls this function repeatedly to keep merging in a _mergesort_ like fashion.
- Then it runs `mergewords.py` to remove duplicate words from the final 11GB index

#### Splitting the index
- To make searching easier, we split the large 11GB index file into __1225 (35*35)__ index files  according to the starting 2 letters of each word in the vocab. We get 35 letters as we have 0-9 and a-z as the words. This is done by `split.py`