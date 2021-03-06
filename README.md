# Medical Expertise Style Transfer System for Layman Patients

## Build from sources

1. Clone the repo

  ```
  $ git clone https://github.com/msi1427/Medical-Expertise-Style-Transfer-System-for-Layman-Patients.git
  $ cd Medical-Expertise-Style-Transfer-System-for-Layman-Patients
  ```

2. Initialize and activate a virtualenv

  ```
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

3. Install the dependencies

  ```
  $ pip install -r requirements.txt
  ```

4. Download the trained model and put them in 'trained_models' folder

```
	https://drive.google.com/drive/folders/1Be8e5smeDiSN12VUzlScKvHXxj6D-zwn?usp=sharing 
```

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

### Homepage

After building from sources, navigate to [http://localhost:5000](http://localhost:5000)  <br/>

There we land on the homepage

![](snaps\homepage.png)

<br/>

<br/>

### Expertise Style Classifier

If we click on 'Expertise Classifier' we land on the following page where we can put any text to classify.

![](snaps\classifier_input.png)

<br/>

If we click on 'Check Expertise Style' we get the expertise score and the style as output.

![](snaps\classifier_results.png)

<br/><br/>

### Expert to Layman Style Transfer

If we click on 'Expertise to Layman' we land on the following page where we can put any expert text to transfer.

![](snaps\transfer_input.png)

<br/>

If we click on 'Transfer to Layman' we get the generated layman text as output.

NB: If we put a layman text there, we will get a layman text as output. 

![](snaps\transfer_results.png)



## Future Works

We have plans to build a more robust and scalable medical aid system with many more features in future incrementally.