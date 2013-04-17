Running LDA
./lda est 0.5 3 settings.txt ap/ap.dat random ap
python topics.py ap/final.beta ap/vocab.txt 10

Questions during presentation:
1) Word-word co occurance matrix is huge. What do you do about it?
Ans:  There are two techniques for handling this kind of situation:
1) We discard the elements with very low TFIDF score.
2) Random projection on k dimensional sub space:

Q(N*N) * X(N*k) = Qbar(N*k)

Based on Johnson-Lindenstrauss lemma: If points in a vector space are projected onto a randomly selected subspace of suitably high dimension, then the distances between the points are approximately preserved.

The choice of the random matrix R is one of the key points of interest. The elements rij of R are often Gaussian distributed, but this need not be the case. Achlioptas [1] has recently shown that the Gaussian distribution can be replaced by a much simpler distribution such as



References:
Experiments with random projections
Random projection in dimensionality reduction: applications to image and text data