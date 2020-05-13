# Import Packages
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.externals import joblib as jb
from builtins import list
import os.path

# To save basic modal test record
if os.path.isfile("corna_result_basic.csv") == False :
    f= open("corna_result_basic.csv","w+")
    f.write("Name,Gender,Age,Body_temperature,Dry_cough,weakness,Breathing_problem,Pain_in_chest,Travel_to_prone_area,losing_sense_of_smell,submitted,basic_result\n")
    f.close()

# To save basic+advance modal test record
if os.path.isfile("corna_result_advance.csv") == False :
    f= open("corna_result_advance.csv","w+")
    f.write("Name,Gender,Age,Body_temperature,Dry_cough,weakness,Breathing_problem,Pain_in_chest,Travel_to_prone_area,losing_sense_of_smell,submitted,basic_result,sour_throat,drowziness,diabetes,heart_disease,lung_disease,reduced_immunity,High_Blood_Pressure,Kidney_disease,Submitted,Advance_result\n")
    f.close()

# To save or count the no of visitors
if os.path.isfile("No_of_visitors.txt") == False :
    f= open("No_of_visitors.txt","w+")
    f.write('0')
    f.close()

# write no. to visitors in file 
def add_visitor():
    f=open("No_of_visitors.txt",'r')            # read last data
    num=int(f.read())                           # convert string data to integer
    num += 1                                    # increment visitor
    f.close()
    f=open("No_of_visitors.txt",'w+')           # open and write visitors no to file
    f.write(str(num))                           
    f.close()

# global list
list=[]

# to add symptoms list to last list
def addlist(a):
    global list
    list=list+a

# to print data in list
def printlist():
    global list
    print(list)

# wtite list data to modals record
def write_result(a):
    global list
    if a==0 :
        f= open("corna_result_basic.csv","a+")    # to write data to basic modal record
        for i in range(len(list)):
            f.write(str(list[i]))
            if i== (len(list)-1):
                f.write('\n')
            else:
                f.write(',')
    else :
        
        f= open("corna_result_advance.csv","a+")   # to write data to advance modal record
        for i in range(len(list)):
            f.write(str(list[i]))
            if i== (len(list)-1):
                f.write('\n')
            else:
                f.write(',')
    
    f.close()



app = Flask(__name__)                   # flask start
model = jb.load(open('Classical_Basic_Model1.pk1', 'rb'))               # basic modal load
model2 = jb.load(open('Advance_Model_Corona.pk1', 'rb'))                # advance modal load

# move to start page 
@app.route('/')
def home():
    return render_template('index.html')   

# predict basic modal result as per symptoms and direct page according to predict result
@app.route('/predict',methods=['POST'])
def predict(): 
    '''
    For rendering results on HTML GUI
    '''
   
    int_features = [x for x in request.form.values()]           # fetch data from index.html form 
    addlist(int_features)                                       # data added to list
    printlist()                                                 # print the list data
    if int(int_features[3])>100:                                # convert body temperature into binary 
        int_features[3]=1
    else:
        int_features[3]=0
    int_features=[int(int_features[x]) for x in range(3,(len(int_features)-1))]         # convert required data to integer and make list
    final_features = [np.array(int_features)]                   # convert to 2-d array
    prediction = model.predict(final_features)                  # predict the result
    addlist([prediction])                                       # add predictin result to list
    write_result(0)                                             # write whole data to basic modal record
    add_visitor()                                               # add visitor to vistors record

    if prediction == 1 :                                        # direct to page according to result
        return render_template('detail.html')
    else :
        global list
        list = [ ]
        return render_template("result_good.html")

# predict advance modal result as per symptoms and direct page according to predict result
@app.route('/advance_predict',methods=['POST'])
def advance_predict(): 
    '''
    For rendering results on HTML GUI
    '''
   
    features = [x for x in request.form.values()]               # fetch data from detail.html form
    addlist(features)                                           # data added to list
    global list
    final_features_advance = [ ]                
    for i in [3,4,12,5,6,13,7,8,14,15,16,17,18,19,9] :          # rearrange data as per modal input from both modal form data
         final_features_advance.append(list[i])
    
    if int(final_features_advance[0])>100:                      # convert body temperature into binary
        final_features_advance[0] = 1
    else:
        final_features_advance[0] = 0
    final_features_advance=[int(final_features_advance[x]) for x in range((len(final_features_advance)))]       # convert required data to integer and make list
    final_features = [np.array(final_features_advance)]         # convert to 2-d array
    predict_advance=model2.predict(final_features)              # predict the result
    addlist([predict_advance])                                  # add predictin result to list
    write_result(1)                                             # write whole data to basic modal record
    printlist()
    list = [ ]                                                  # initialize list
    
    # direct to page according to result
    if predict_advance == 1 :                               
        return render_template('result.html')           
    else :
        return render_template("result_good.html")

#  diect to result
@app.route('/result')
def result():
    return render_template('result.html')   

# direct back to Menu
@app.route('/back')
def back():
    return render_template('index.html')  
 
if __name__ == "__main__":              # run whole setup
    app.run(debug=True)