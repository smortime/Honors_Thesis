library(tm)
library(topicmodels)

stop_words <- stopwords("SMART")

setwd("/home/schuyler/Desktop/testing")

filenames <- list.files(getwd(), pattern="*.txt")
files <- lapply(filenames, readLines)
tweets <- Corpus(VectorSource(files))

#preprocessing
tweets <- tm_map(tweets, content_transformer(tolower))
tweets <- tm_map(tweets, removePunctuation)
tweets <- tm_map(tweets, removeNumbers)
tweets <- tm_map(tweets, removeWords, stopwords("english"))
#Removes ampersand from data set, since isn't encoded as &
tweets <- tm_map(tweets, removeWords, c("amp"))
tweets <- tm_map(tweets, stripWhitespace)


#make a table of terms
dtm <- DocumentTermMatrix(tweets)
rownames(dtm) <- filenames
dtms <- removeSparseTerms(dtm, .997)
freq <- colSums(as.matrix(dtms))
ord <- order(freq, decreasing=TRUE)
write.csv(freq[ord], "/home/schuyler/Documents/Honors_Thesis/data_sets/HICSS/results/oct/word_freq.csv")
rowTotals <- apply(dtms, 1, sum)
dtms_new <- dtm[rowTotals> 0, ]

#Parameters
k <- 5
burnin <- 4000
iter <- 2000
thin <- 500
seed <- list(2003,5,63,1000001,765)
nstart <- 5
best <- TRUE

#run the model... run time around 57 mins
start = Sys.time()
start
lda_out <- LDA(dtms_new, k, method="Gibbs", control=list(nstart=nstart, seed=seed, best=best, burnin=burnin, iter=iter, thin=thin))
end = Sys.time()
end - start

#write model to csv
lda_out_topics <- as.matrix(topics(lda_out))
write.csv(lda_out_topics, file="/home/schuyler/Documents/Honors_Thesis/data_sets/HICSS/results/oct/tweets_to_topics_5k.csv")

lda_out_terms = as.matrix(terms(lda_out, 6))
write.csv(lda_out_terms, file="/home/schuyler/Documents/Honors_Thesis/data_sets/HICSS/results/oct/topics_terms_5k.csv")

#probabilities of each topic assignment
topic_probabilities = as.data.frame(lda_out@gamma)
write.csv(topic_probabilities, file="/home/schuyler/Documents/Honors_Thesis/data_sets/HICSS/results/oct/probabilities_5k.csv")
