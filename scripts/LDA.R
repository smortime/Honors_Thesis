#Loading libraries
library(tm)

#load the data
setwd("/home/schuyler/Desktop/Honors_Thesis/data_sets/model_data/testing")
filenames <- list.files(getwd(), pattern="*.txt")
files <- lapply(filenames, readLines)
docs <- Corupus(VectorSource(files))

#preprocessing
docs <- tm_map(docs, content_transformer(tolower))
toSpace <- content_transformer(function(x, pattern) {return (gsub(pattern, " ", x))})
docs <- tm_map(docs, toSpace, "-", "'", '"', "@")
docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, removeWords, stopwords("english"))
docs <- tm_map(docs, stripWhitespace)
docs <- tm_map(docs, stemDocument)

dtm <- DocumentTermMatrix(docs)
rownames(dtm) <- filenames
freq <- colSums(as.matrix(dtm))
length(freq)
ord <- order(freq, decreasing=TRUE)
freq[ord]
write.csv(freq[ord], "word_freq.csv")