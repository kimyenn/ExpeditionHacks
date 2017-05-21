# Expeditionhacks Seattle 2017 [~36 hours]

### Team GitNews Members

 * [Vanessa Davila](https://github.com/vadavila) [Developer] 
 * [Jair Castillo](https://github.com/jcastillohand) [Developer] 
 * [Kimyen Nguyen](https://github.com/kimyenn) [Data Scientist] 


### The Problem
How to curate (refine, prioritize, & suggest) news stories/summaries for top national advisors with little time to spend. Also, how should feedback to specific stories be handled if any are given? 

### Our Solution

Utilizing RSS Feeds, NLP, and a specific machine learning algorithm for each advisor, we are able to truly suggest the top news stories in an easy to read format catered to the target audience. Feedback is implemented by two simple icons for each news articles presented which someone can click on to indicate if the article was useful. The models are then retrained utilizing the additional feedback.

In the end, we are able to present the top 10 (configurable) news snippet for any specific advisor in a clean and intuitive UI :+1:


Props to Mr. Doob and his [code editor](http://mrdoob.com/projects/code-editor/), from which
the inspiration to this, and some handy implementation hints, came.

### What we used:

 * [nltk](http://www.nltk.org/) processing news contect
 * [scikit-learn](http://scikit-learn.org/) creating models for each adivsor
 * [pandas](http://pandas.pydata.org/) exploring, analyzing, cleaning data

![alt](http://i2.kym-cdn.com/photos/images/facebook/000/011/296/success_baby.jpg)


