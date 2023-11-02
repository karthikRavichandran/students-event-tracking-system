from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """ 
Hi, instructos, 

I'm not sure how to set up the parameters in the batch query JSON files for No Smoothing scenario?

For JM smoothing, we can set the parameters like 

"scorer": "jm",
"lambda": 0.5,
For JM smoothing, we can set the parameters like 

"scorer": "dirichlet",
 "mu": 1000,
However, for NO smoothing, should we set up the parameters as

"scorer": "jm",
"lambda": 0 ,
 or 

"scorer": "dirichlet",
"mu": 0,
I'm asking this, because I find the 2 ways of setup would yield different MAP results for the NO smoothing scenario.

Appreciate your advice.
"""
print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))


