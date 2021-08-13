InstituteForComputingInResearch
# LEXRANK
Lexrank is an unsupervised approach to text summarization based on graph-based centrality scoring of sentences. It strives for sentences to recommend other similar sentences to the reader; therefore, a sentence similar to many others will be a centrality. In other words, to get ranked highly and placed in a summary, a sentence must be similar to many sentences that are also similar to many others, instigating intuitive sense.
## INSTALLATION
use the package manager [pip](https://pypi.org/project/pip/) to install lexrank
```bash 
pip install lexrank
```
## PURPOSE
EVALUATING NLP SUMMARIZATION BIAS (ETHNICITY) IN TWITTER (AE (AMERICAN ENGLISH) & AAE (AFRICAN AMERICAN ENGLISH))
## DESCRIPTION
### BACKGROUND
Natural language processing (NLP) is a beautiful subfield of computer science, linguistics, and artificial intelligence. Its focus on human and computer language interaction through manipulating and analyzing massive quantities of natural language data aims to understand contents like a regular human being, further advancing the daily lives of many with technology. With technology promptly progressing, it is typical that people overlook the withholdings that follow, especially dialect bias in summarization. Everybody's voice deserves to be heard, but when it comes to natural language processing, popular summarization methods such as lexrank disappoints.
### FEATURES
The suggested bias evaluation metric is simple and efficient- it calculates the percentage of the extracted tweets from each dialect that ends up in the summary through the following equation: (the number of tweets from AE or AAE dataset) divided by (total number of tweets in the summarization). Also, you can switch between three potential datasets: including AEAAE.csv (Tweets ordered from American English to African American English), AAEAE.csv (Tweets ordered from African American English to American English), and RANDOM.csv (Tweets randomly ordered). They should give the same results because they are all using the same algorithm (cosine similarity).
## STEPS
```python 
# make sure you are in the TWEET folder before running the code
cd ../
# sample size
5
# threshold
0.02
# file (you can choose from three options)
RANDOM.csv
AEAAE.csv
AAEAE.csv
```
## ACKNOWLEDGEMENT
Thank you for running our code and feel free to contact us with suggestions!
## SUPPORT
Stuck? Feel free to contact irisyjchang@gmail.com if you have run into any issues!
