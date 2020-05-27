# Disease Prediction through Symptoms
<br />

### Description:
    This project was developed to predict diseases (Prognosis) through the inputed symptoms.
    Developed a website for the same. ( Using HTML, CSS , Python - Flask )  
<br />

### Requirements:

     -  Python 3 or above
     -  Scikit Learn (library)
     -  Flask (library)
     
<br />

### Information about the dataset:
    The Original dataset contains the Disease and symptoms in the given form below:
    
              Hypertension  : headache , chest_pain , dizziness , loss_of_balance , lack_of_concentration
              Fungal infection : itching , skin_rash , nodal_skin_eruptions , dischromic _patches 
    
    
    This above dataset has been parsed and converted into csv for easement.
    Divided into training and testing set. See above files.
<br />

### How to Run:

    1. Download the zip from above. 
    2. Unzip and Go inside the folder.
    3. Open terminal and cd into the above folder.
    4. Run app.py in your terminal through the below command.
            $ python3 app.py

    5. The above command will output something like:
            Running on http://127.0.0.1:5000/

    6. Copy & paste the above link in your browser.
    7. Done. 
    Now you ready to go.
 
 <br />
 
### View the python notebook for information about preprocessing and model building [here. NOTEBOOK](../master/Symptom_Disease_Prediction.ipynb)    
    
    
<br /> 

### Algorithm:
    - Used tree model based on the data-set as it only  0 and 1 values. 
    - Tree models are consider the best for such kind of data.
    - They are found to be fastest and accurate for such data.
    - As they use splitting based on information gain.
    
    - Visualization of a decision tree is shown below.
    
![tree](https://user-images.githubusercontent.com/47252506/82969025-4364d000-9fec-11ea-98b1-662eef1897d1.png)

<br /> 

### Website Screenshots:

<br />

#### Home-page:

<br />

  ![screenshot-127 0 0 1_5000-2020 05 27-04_58_08](https://user-images.githubusercontent.com/47252506/82969334-0b11c180-9fed-11ea-8a9c-17765ee43261.png)


<br /><br />

#### Input:

<br />

  ![Screenshot from 2020-05-27 04-32-15](https://user-images.githubusercontent.com/47252506/82969193-aeaea200-9fec-11ea-8d86-8a61ab523431.png)
  
  
 <br /> 
 
  ![Screenshot from 2020-05-27 04-32-39](https://user-images.githubusercontent.com/47252506/82969196-b2dabf80-9fec-11ea-988f-52e03a35451b.png)
  
  
  
  
 <br /><br /><br />
 
#### Output:

  ![screenshot-127 0 0 1_5000-2020 05 27-05_10_34](https://user-images.githubusercontent.com/47252506/82969287-ed445c80-9fec-11ea-83cb-6eeea8641087.png)


