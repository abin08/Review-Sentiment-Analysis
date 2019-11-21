# Review-Sentiment-Analysis

Uses Multinomial Naive Bayes algorithm to classify customer reviews into positive, negative and complaints.

Run sentiment_analyser.ipynb to see the results

Dataset is available at: 
  https://drive.google.com/open?id=1VfxUSRxRsEBt-thnU8ge7vnIlLmOHuSx

Obtained the dataset from: 
  https://www.kaggle.com/datafiniti/consumer-reviews-of-amazon-products
  https://www.kaggle.com/shitalkat/amazonearphonesreviews
      
## Instructions
#### 1. Download dataset
        Download 'amazon_reviews' dataset from the first link and paste it in the directory 'datasets'.
#### 2. Install requirements
        1. pip install -r requirements.txt
        2. Download spacy language model using the command 'python3 -m spacy download en'
        3. Download nltk vader_lexicon using the command 'python3 -m nltk.downloader vader_lexicon'
#### 3. Run the files
        1. prepare_dataset.ipynb
            Prepares the datasets from csv files, filter outs unwanted columns, etc.
        
        2. feature_extraction.ipynb
            Performs data cleaning, extracts features from the prepared dataset,and creates training and testing datasets
        
        3. MulinomialNB.ipynb
            Creates a Multinomial Naive Bayes model from the training data
        
        4. sentiment_analyser.ipynb
            Performs sentiment analysis on the given text using the model created.
            The function sentiment_analysis(text) gives the sentiment of the text argument passed
