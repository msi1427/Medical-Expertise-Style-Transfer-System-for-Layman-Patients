# Medical Expertise Style Transfer System for Layman Patients

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



## Look into the Trained Models

We are using two trained models. <br/>

1. style-classifier.pkl => given a text this model, it can classify the expertise of that sentence in medical domain. <br/>
2. maskedlm-model.pkl => given a text with gaps, it can generate the layman terms in the gaps. <br/>

NB : For now, treat these models as black-box, since the the methodology is still our ongoing research. We will publish the details as soon as we finish all our training and testing. <br/>

## Future Works

We have plans to build a more robust and scalable medical aid system with many more features in future incrementally.