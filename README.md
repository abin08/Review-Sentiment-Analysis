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
        Download amazon_reviews dataset from the first link and keep it in the directory 'datasets' in root of the project.
#### 2. prepare_dataset.ipynb
        Prepares the datasets from csv files, filter outs unwanted columns, etc.
#### 3. feature_extraction.ipynb
        Extracts features from the prepared dataset, creates training and testing datasets
#### 4. MulinomialNB.ipynb
        Creates a Multinomial Naive Bayes model from the training data
#### 5. sentiment_analyser.ipynb
        Performs sentiment analysis on the given text using the model created.
        The function sentiment_analysis(text) gives the sentiment of the text argument passed
