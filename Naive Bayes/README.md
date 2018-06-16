# Naive Bayes

Prediction accuracy for naïve bayes with unigrams are the following:
Hamlet accuracy:  91.3 %

Juliet accuracy:  20.0 %

Macbeth accuracy:  15.28 %

Romeo accuracy:  9.92 %

Total accuracy:  48.66 %

Prediction accuracy for naïve bayes with bigrams are the following:
Hamlet accuracy:  99.66 %

Juliet accuracy:  1.01 %

Macbeth accuracy:  0.0 %

Romeo accuracy:  0.0 %

Total accuracy:  44.48 %

Python 3 was used for both unigrams and bigrams, as well as the numpy module and the Counter method from the collections module. Accuracy for the bigrams was noticeably lower than that of the unigrams. This could be due to a need for more training data, or because of Shakespeare’s unique usage of the English language and his play on words. Log probabilities and pseudo counts were not used for the current implementation, however, would likely provide greater accuracy for both unigrams and bigrams. End of line tokens were removed, providing approximately 1% increase in accuracy across all class labels. Future implementations would also likely remove stop words and punctuation for greater accuracy.

