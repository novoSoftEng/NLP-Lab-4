# NLP Lab Report

## Objective
The main purpose of this lab is to get familiar with NLP language models using the PyTorch library. The lab is divided into three parts: Classification Regression, Transformer (Text Generation), and BERT.

## Part 1: Classification Regression

### 1. Data Collection
Using web scraping libraries (Scrapy/BeautifulSoup), text data from various Arabic news websites on a specific topic (court decsion on israel) was collected. The dataset was prepared as follows:

| Text (Arabic Language) | Score |
|-------------------------|-------|
| Text 1                  | 6     |
| Text 2                  | 7.5   |

The score represents the relevance of each text on a scale from 0 to 10.

### 2. Preprocessing NLP Pipeline
The collected dataset was processed through an NLP pipeline which included the following steps:
- **Tokenization**: Splitting the text into individual words or tokens.
- **Stemming and Lemmatization**: Reducing words to their root forms.
- **Stop Words Removal**: Filtering out common words that do not contribute much to the meaning.
- **Discretization**: Converting continuous features into discrete bins.

### 3. Model Training
The models were trained using various architectures:
- **RNN** (Recurrent Neural Network)
- **Bidirectional RNN**
- **LSTM** (Long Short-Term Memory)

Hyper-parameters were tuned to achieve the best performance.

### 4. Model Evaluation
The models were evaluated using standard metrics such as MSE and MAE.

## Part 2: Transformer (Text Generation)

### 1. Fine-tuning GPT-2
The pre-trained GPT-2 model from the pytorch-transformers library was loaded and fine-tuned on a customized dataset. 

### 2. Text Generation
I fine tuned the model in order for it to be able to create a transcript for a podcast , as that is the dataset i used.

## Part 3: BERT

### DataSet
The dataset used was from [Amazon reviews](https://nijianmo.github.io/amazon/index.html).

### 1. Model Establishment
The pre-trained `bert-base-uncased` model was established.

### 2. Data Preparation
The data was prepared, and the BERT embedding layer was adapted.

### 3. Model Training
The model was fine-tuned and trained by selecting the optimal hyper-parameters to obtain an efficient model.

### 4. Model Evaluation
The model was evaluated using standard metrics such as Accuracy, Loss, F1 score, and additional metrics like the BLEU score and BERT metric.

### 5. General Conclusion
The use of the pre-trained BERT model demonstrated significant improvements in understanding and processing natural language due to its contextual embedding capabilities. Fine-tuning on specific datasets further enhanced its performance for particular tasks.

## Synthesis and Learning Outcomes
During this lab, the following key points were learned:
- The importance of preprocessing in NLP tasks.
- The differences and applications of various RNN architectures (RNN, LSTM).
- The process of fine-tuning pre-trained models like GPT-2 and BERT.
The completed work was pushed to a GitHub repository, and a brief report was written in the GitHub README file.

## Tools Used
- Google Colab/Kaggle
- GitLab/GitHub
- spcrapy
- NLTK
- PyTorch

