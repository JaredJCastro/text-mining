# Project Writeup and Reflection 

## 1. Project overview

For this assignment, I used three different books in the Horror genre sourced from the Gutenberg Project: 'The Yellow Wallpaper', 'Wendigo', and 'Strange Case of Dr. Jekyll and Mr. Hyde'. My goal was to use natural language processing to analyze if the most common words in these horror books swayed towards a negative sentiment. My theory was that the most common words would be more likely to be negative instead of positive, because of the fact that these are horror books. Through this analysis I would be able to see if the authors are intentionally using 'negative' words to set a tone in their books.

## 2. Implementation 

The major components of this project were: sourcing the texts, cleaning up the data, finding the most common words, and then conducting the sentiment analysis. The data was sourced from Gutenberg. Data cleaning consisted of removing headers, and footnotes by Gutenberg, leaving only the actual text from the book. After finding the most common words of each text, these words were inputted in to their respective sentiment analysis functions. 

One decision was choosing how many words I wanted included in the sentiment analysis. Originally, I considered using a mix of the 20 most common from each list (instead of using all 20 from each, I'd pull some words from each to reach a total of 20 instead of 60.) However, I ended up to use all 20 most common words from each text because a larger sample size would likely result in a more accurate conclusion.

## 3. Results 
The results of the sentiment analysis did not support my theory. I thought there would be a noticable number of words with a 'negative' sentiment in these texts but this was not the case. The vast majority of the common words used returned 'neutral' sentiment.

Sample of some of the analysis:
{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

This leads me to the conclusion that, for horror stories, it isn't necessarily the individual words that are used that set the tone of the story, but instead how to words are crafted together in sentences that set the tone. 

## 4. Reflection 

All in all, my second attempt at this project went much smoother than my first go around. This time I spent more time debugging, more time cleaning data to get rid of unnecessary functions, and generally got rid of redundancies in my code to make it cleaner and more efficient. I also had a plan BEFORE I started coding, whereas last time I started coding and then just followed whatever worked. This meant my scope was defined and I knew the steps I needed to take, which made the whole process much more efficient and pretty much stress free. This project has taught me the importance of creating a plan before coding, and also allowing myself enough time so that I can thoroughly think about a problem and take breaks when needed, instead of cramming last minute. 
