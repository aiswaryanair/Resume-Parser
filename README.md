# Resume-Parser

Resume Parsing in Python Project Objective
This project uses Python's library, SpaCy to implement various NLP (natural language processing) techniques like tokenization, lemmatization, parts of speech tagging, etc., for building a resume parser in Python. And, considering all the resumes are submitted in PDF format, you will learn how to implement optical character recognition (OCR) for extracting textual data from the documents. The resulting application will require minimum human intervention to extract crucial information from a resume, such as an applicant's work experience, name, geographical location, etc. It is one of the most exciting NLP projects for beginners, so make sure you attempt it.
To solve this, our resume parser application can take in millions of resumes, parse the needed fields and categorise them. This resume parser uses the popular python library - SpaCy for OCR and text classifications. First, we train our model with these fields, then the application can pick out the values of these fields from new resumes being input.
The dataset of resumes has the following fields:
•	Location
•	Designation
•	Name
•	Years of Experience
•	College
•	Degree
•	Graduation Year
•	Companies worked at
•	Email address

NLP Tools and Techniques
Tokenization
It is the process of splitting textual data into different pieces called tokens. One can either break a sentence into tokens of words or characters; the choice depends on the problem one is interested in solving. It is usually the first step that is performed in any NLP project, and the same will be the case with this resume parser using NLP project. Tokenization helps in further steps of an NLP pipeline which usually involves evaluating the weights of all the words depending on their significance in the corpus.
Lemmatization
The larger goal of this resume parsing python application is to decode the semantics of the text. For that, the form of the verb that is used does not have a significant impact. Therefore, lemmatization is used to convert all the words into their root form, called 'lemma.' For example, 'drive,' 'driving, 'drove' all have the same lemma 'drive.'
Parts-of-Speech Tagging
If you consider the word "Apple," it can have two meanings in a sentence. Depending on whether it has been used as a proper noun or a common noun, you will understand whether one is discussing the multinational tech company or the fruit. This CV parser python project will understand how POS Tagging is implemented in Python.
Stopwords Elimination
Stopwords are the words like 'a', 'the,' 'am', 'is', etc., that hardly add any meaning to a sentence. These words are usually deleted to save on processing power and time. In their CV, an applicant may submit their work experience in long paragraphs with many stopwords. For such cases, it becomes essential to know how to extract experience from a resume in python, which you will learn in this project.
SpaCy
SpaCy is a library in Python that is widely used in many NLP-based projects by data scientists as it offers quick implementation of techniques mentioned above. Additionally, one can use SpaCy to visualize different entities in text data through its built-in visualizer called displacy. Furthermore, SpaCy supports the implementation of rule-based matching, shallow parsing, dependency parsing, etc. This NLP resume parser project will guide you on using SpaCy for Named Entity Recognition (NER).
OCR using TIKA
You will use Apache Tika, an open-source library for implementing OCR in this project. OCR stands for optical character recognition. It involves converting images into text and will be used in this resume extraction python project for decoding text information from the PDF files. The textual data is processed using various NLP methods to extract meaningful information.
Machine Learning Pipeline
As this project is about resume parsing using machine learning and NLP, you will learn how an end-to-end machine learning project is implemented to solve practical problems. Different machine learning algorithms Neural Networks using SpaCy library are used in this project to build a model that can pull out relevant fields like location, name, etc., from different resumes of different formats.

# Execution Instructions
* Install requirements with "pip install -r requirements.txt"
* Run engine.py
