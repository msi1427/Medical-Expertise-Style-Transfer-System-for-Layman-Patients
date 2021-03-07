# Medical Expertise Style Transfer System for Layman Patients

## Introduction

This is our academic project for Human Computer Interaction course [Course Code : CSE 4829]. We designed a webapp in aid for layman patients to get a better understanding on expert texts by medical experts.  We used two Transformer-based deep learning models for inference. Details about the models will be published later after all the training and testing phases which is our ongoing research.

## Contributors

<ul>
    <li> Mohammad Sabik Irbaz (ID : 160041004, Email : sabikirbaz@iut-dhaka.edu ) </li>
    <li> Abir Azad (ID : 160041024, Email : abirazad@iut-dhaka.edu ) </li>
    <li> Anika Tasnim Preoty (ID : 160041044) </li>
    <li> Tani Barkat Shalanyuy (ID : 160041083) </li>
</ul>

## Affiliation

Computer Science and Engineering
Islamic University of Technology (IUT)
Gazipur, Dhaka, Bangladesh

## Build from sources

1. Clone the Git Repo

  ```
  $ git clone https://github.com/msi1427/Medical-Expertise-Style-Transfer-System-for-Layman-Patients.git
  $ cd Medical-Expertise-Style-Transfer-System-for-Layman-Patients
  ```

2. Initialize and activate a virtualenv

  ```
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  
  # For Windows
  $ source .\env\Scripts\activate.bat
  ```

3. Install the dependencies

  ```
  $ pip install -r requirements.txt
  ```

4. Download the trained model from the following link : <br/>

   https://drive.google.com/drive/folders/1Be8e5smeDiSN12VUzlScKvHXxj6D-zwn?usp=sharing <br/>

   Create a folder named 'trained_models' and put the downloaded models in the folder. <br/>

5. Run the development server

  ```
  $ python app.py
  ```

6. Navigate to [http://localhost:5000](http://localhost:5000)

<br/>

## Features

- Expertise Classifier
- Expertise Style Transfer [Expert to Layman]

<br/>

## Low Fidelity Prototype

[Done using Balsamiq]



## Walkthrough

### Video Walkthrough

YouTube Link : *link will be added here.*

### Homepage

After building from sources, navigate to [http://localhost:5000](http://localhost:5000)  <br/>

There we land on the homepage

<img src = "snaps\homepage.png" width="1000" height="500">

<br/>

<br/>

### Expertise Style Classifier

If we click on 'Expertise Classifier' we land on the following page where we can put any text to classify.

<img src = "snaps\classifier_input.png" width="1000" height="500">

<br/>

If we click on 'Check Expertise Style' we get the expertise score and the style as output.

<img src = "snaps\classifier_results.png" width="1000" height="500">

<br/><br/>

### Expert to Layman Style Transfer

If we click on 'Expertise to Layman' we land on the following page where we can put any expert text to transfer.

<img src = "snaps\transfer_input.png" width="1000" height="500">

<br/>

If we click on 'Transfer to Layman' we get the generated layman text as output.

NB: If we put a layman text there, we will get a layman text as output. 

<img src = "snaps\transfer_results.png" width="1000" height="500">

<br/><br/>

## Look into the Trained Models

We are using two trained models. <br/>

1. style-classifier.pkl => given a text this model, it can classify the expertise of that sentence in medical domain. <br/>
2. maskedlm-model.pkl => given a text with gaps, it can generate layman terms in the gaps. <br/>

NB : For now, treat these models as black-box, since the the methodology is still our ongoing research. We will publish the details as soon as we finish all our training and testing. <br/>

## Future Works

We have plans to build a more robust and scalable medical aid system with many more features in future incrementally.