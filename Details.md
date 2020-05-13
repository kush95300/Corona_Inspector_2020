# About Corona Inspector 2020 Android Application features details
## Introduction

Corona Inspector is an android application which is used to detect whether a person is having Corona or not with more than 85 % accuracy. This application is useful for detecting corona positive patients. It is based on Machine Learning model with Python-3. It has two model: model -1 is basic model and model-2 is advanced model, which is select own by application as per patient symptoms. Every one can use this application whether it is belongs to technical background or not. It has also added government and other corona information site for COVID latest details.
## Instructions to Install COVID Inspector:
1.	Click on the apk file
2.	<b> Click to the install option          :       </b><img src="images/Open.jpeg" width=400 align="center"/>
<br>
3.	<p><b> Click to the install         :      </b><img src="images/Install.jpeg" width=400 align="center"/></p>
<br>
4.  <b> click on the Install Anyway     :     </b><img src="images/.jpeg" width=400 align="center"/>


# Menu Description:

## About Corona Instructor 2020 Mobile app :  (Detailed information about application is provided in Detail.md file)

### Starting Splash Screen of Application :


<b> Starting Splash Screen of App           :       </b><img src="images/Splash-Screen1.jpeg" width=400 align="center"/>
<br>
<p><b> Starting Splash Screen of App    :       </b><img src="images/Splash-screen2.jpeg" width=400 align="center"/></p>
<br>

### Menu of this application shown below :


<div>

<b> Main Menu of App            :   </b><img src="images/Menu_1.jpeg" width=400 align="center"/>
<br>
<p><b> Clicked Main Menu of App      :            </b><img src="images/Menu_2.jpeg" width=400 align="center"/></p>

### Main menu brief discription :
<dl>
  <dt>Corona test - </dt>
  <dd> By clicking on corona test the user will redirect to the site where there is a symptom checker form which is required to fill by user. If on first page modal predict user vulnerable than  the user will be  redirected to the second page which is created using advanced model for better prediction. Then user will fill the second form and hit submit button than model will predict whether it is COVID positive or not.</dd>
  <dt>Corona Image</dt>
  <dd>- where you can search for Corona related images. This is corona images on google. </dd>
    <dt>Corona Information and Tips </dt>
    <dd>- by clicking on this option the user will redirect to the ministry of health and family welfare site for checking COVID related updates. This also contain tips, song and worldinfo site also for more corona updates.</dd>
    
   <dt>Lockdown @21 </dt>
   <dd>- by clicking on this option the user will redirect to the site lockdown@21 which is a blog site of us. This  contain post related to corona and lockdown.</dd>
    
   <dt> About Us </dt>
   <dd>- This contain basic information about application.</dd>
    
   <dt> Exit </dt>
   <dd>- to exit out of the application.</dd>
</dl>

</div>

## Brief Description of Model :

1. By using csv file of COVID Symptoms we trained a binary classification  model using Logistic Regression Method with more than 85% accuracy .
2. packages used are numpy,pandas,os,sklearn,seaborn and matplotlib (for feature elimination y graph), ols methon for feature selection.
3. This modal is based only on 127 data entry. Soon we are uploading model with nearly 7000 people dataset trained model.
