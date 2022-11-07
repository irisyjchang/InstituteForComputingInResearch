InstituteForComputingInResearch
# LEXRANK
Lexrank is an unsupervised approach to text summarization based on graph-based centrality scoring of sentences. Sentences recommend other similar sentences to the reader; therefore, a sentence similar to many others will be a centrality. In other words, to get ranked highly and placed in a summary, a sentence must be similar to many sentences that are also similar to many others, instigating an intuitive sense.
## INSTALLATION
use the package manager [pip](https://pypi.org/project/pip/) to install lexrank
```bash 
pip install lexrank
```
## PURPOSE
EVALUATING NLP SUMMARIZATION BIAS (DIALECT) IN TWITTER (AE (AMERICAN ENGLISH) & AAE (AFRICAN AMERICAN ENGLISH)) & HAE (HISPANIC AMERICAN ENGLISH)
## DESCRIPTION
### BACKGROUND
Natural language processing (NLP) is a subfield of computer science, linguistics, and artificial intelligence. Its focus on human and computer language interaction through manipulating and analyzing massive quantities of natural language data aims to understand contents like a regular human. With social bias being a prevalent issue alongside the rapid advancements of technology, the bias in modern-day technology need to be brought to prominent and prompt attention. One being, the dialect bias in summarization. 
### FEATURES
The suggested bias evaluation metric is simple and efficient- it calculates the percentage of the extracted tweets from each dialect that ends up in the summary through the following equation: (the number of tweets from AE or AAE or HAE dataset) divided by (total number of tweets in the summarization).
## STEPS
```python 
# run the following in the terminal
python3 code.py
# type the datasets you want to run out of ae, aae, and hae and press enter after typing each one
# type enter when you are done
# type in a sample size (has to be an integer)
```
you can edit input.txt to the file names and sample numbers you want
## ACKNOWLEDGEMENT
Thank you for running our code and feel free to contact us with suggestions.
## SUPPORT
Feel free to contact us if you run into any issues.
