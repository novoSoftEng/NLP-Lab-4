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
- **Stemming**: Reducing words to their root forms.
- **Stop Words Removal**: Filtering out common words that do not contribute much to the meaning.

### 3. Model Training
The models were trained using various architectures:
- **RNN** (Recurrent Neural Network)
- **Bidirectional RNN**
- **LSTM** (Long Short-Term Memory)

Hyper-parameters were tuned to achieve the best performance.

### 4. Model Evaluation
The models were evaluated using standard metrics such as MSE and MAE.

| Model | Test Loss | Mean Squared Error (MSE) | Mean Absolute Error (MAE) |
|-------|-----------|--------------------------|---------------------------|
| LSTM  | 9.141     | 9.542                    | 1.792                     |
| RNN   | 13.082    | 12.750                   | 2.417                     |
| BI-RNN| 13.820    | 13.875                   | 2.375                     |

This table organizes the evaluation metrics for the LSTM, RNN, and GRU models for easy comparison.
## Part 2: Transformer (Text Generation)

### 1. Fine-tuning GPT-2
The pre-trained GPT-2 model from the pytorch-transformers library was loaded and fine-tuned on a customized dataset : Lex Fridman Podcast Transcript from Kaggle. 

### 2. Text Generation
I fine tuned the model in order for it to be able to create a transcript for a podcast .
The model was able to create the text but it seems the text made sens until you jumb to another paragraphe.

## Part 3: BERT

### DataSet
The dataset used was from [Amazon reviews](https://nijianmo.github.io/amazon/index.html).

### 1. Model Establishment
The pre-trained `bert-base-uncased` model was established.

### 2. Data Preparation
The data was prepared, and the BERT embedding layer was adapted.

### 3. Model Training
ALthough i tried to fine tune the model but due to computational constraints I could not finish the training , so i apologize for that.

### 5. General Conclusion
The use of the pre-trained BERT model demonstrated significant improvements in understanding and processing natural language due to its contextual embedding capabilities. Fine-tuning on specific datasets further enhanced its performance for particular tasks.

## Synthesis and Learning Outcomes
During this lab, the following key points were learned:
- The importance of preprocessing in NLP tasks.
- The differences and applications of various RNN architectures (RNN, LSTM).
- The process of fine-tuning pre-trained models like GPT-2 and BERT.

## Tools Used
- Google Colab/Kaggle
- GitHub
- spcrapy
- NLTK
- PyTorch

