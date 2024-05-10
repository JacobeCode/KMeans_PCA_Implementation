# ML-AI
## KMeans/PCA Implementation
## Also this branch contains some experiments, new things and revisions connected to AI/ML field.
### MAIN: Manual implementation of - KMeans Clustering / PCA
Also - here you can find:
- some scripts and files containing manual (w/o sklearn) implementation of clustering algorithm (KMeans) with manual PCA analysis and implementation
- some test and exemplary scripts about SQL Connections and Manipualtion (with connection to Python (pyodbc))
- some scripts with sklearn various Trees algorithms (researched and tested usage of MLFlow)

## Used datasets
For implementation purposes and testing there were used two databases:
- For emotions/sentiment based approach - [Emotions dataset for NLP](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp/data)
- For implementing KMeans and PCA - [Loan Predticiton Dataset](https://drive.google.com/file/d/1ZzEouo7lRJvajxK6jLM2K_p9xAwGw1tS/view?pli=1) from [Loan Predition Practice Problem](https://datahack.analyticsvidhya.com/contest/practice-problem-loan-prediction-iii/?utm_source=blog&utm_medium=comprehensive-guide-k-means-clustering)

## Content
In this repository you can find files and experiments connected to:
- additinal_files - all the files that helps process the data
    - standard_scaler.py - manual scaler like in sklearn
    - data_processing.py - simple CSV-like data processing with categorical-to-numerical encoding
    - pca.py - manual PCA for reducing dismensionality of data
- colab_files - all files connected to some tests including Google Colab usage
    - conx_test.py/ipynb - testing connections to local SQL Databases and MLFlow from Colab level - also with use of tunneling services like [ngrok](https://github.com/inconshreveable/ngrok)
- exp_data - some of scripts saves relevant data. This is the directory where these files are stored. (Currently saving used and labeled features from KMeans)
- kmeans - files connected to KMeans algorithm
    - kmeans.py - manually implemented KMeans clustering with PCA reducion algorithm (with additional plotting features and adjusted for diffrent sizes of data)
    - sql_connector.py - at hand file for examplatory SQL Server (local) connection
- trees - files connected to Tree-like algorithms
    - trees.py - small project connected to Decision Tree Classifier - created mainly to experiment and learn working with MLFlow
- requirements.txt/requirements.yml - files with required libs for this repository