**Team Members**

- Giovanni Scalzotto
- Akshat Goel
- Francesco Forner
- Kevin Shah

**How to use API**

1. Go to link : http://3.88.104.79:8000/
2. Click on "Check out the NLP services"
3. Select a service. Descriptions of all the services is given below
4. Enter a text or use default placeholder text
5. Click submit to view results

**Services Description**

Wikipedia Scraping The objective of our project is to scrape wikipedia and provide a variety of useful services that would help one quickly understand the information. The services we have provided collectively inform users of key increments of data from a large chunk of text. Please see our services listed below:

Polarity - Polarity is a float which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement. Polarity is commonly used for sentiment analysis as it provides users with a quantitative value for how positive, negative, or neutral a text is.

Subjectivity - Subjectivity ranges from [0,1] and measures the amount of personal opinion and factual information is contained in the text. Subjective sentences generally refer to personal opinion, emotion or judgment whereas objective refers to factual information. A score of 1 means that the text is more subject while a 0 means that the text is more factual.

Similarity - Similarity measures tells us how close two words are. Our service allows you to enter two words and find how closely related the words in your text are similar to those 2 key words.

Frequency & WordCloud - Frequency measures how often a word occurs in a given level of text. WordCloud organizes that count and displays it such that the words that occur more are greater in size.

Summarization & Keywords - The text summary features summarizes the given text into a few sentences. In order for it to work, users MUST input 10 or more sentences and have a total word count of greater than 100. Keywords returns the words that are most significant in the given body of text.

POS Tagging - Tells the users what part-of-speech indicated words are (i.e. nouns, verbs, adjectives, etc.).

**Known Issues**

- Wikipedia scraper does not work for all wikipedia pages. It works best for famous people profiles like the ones below: 
1.https://en.wikipedia.org/wiki/Donald_Trump
2.https://en.wikipedia.org/wiki/Barack_Obama
3.https://en.wikipedia.org/wiki/Cristiano_Ronaldo
- Summarization service works for more than 10 sentences. Ideally for best results, if you enter a long text or use the default text provided it gives the best results
