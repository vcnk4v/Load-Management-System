import requests
from flask import Flask,render_template,request,url_for,redirect
import datetime
import matplotlib.pyplot as plt
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures



import json
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/status',methods=['GET','POST'])
def status():
    url = "http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Load1/Data/la"

    payload={}
    headers = {
    'X-M2M-Origin': 'admin:admin',
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = eval(response.text)
    data_cons_120 = data["m2m:cin"]
    Load1 = data_cons_120["con"][13:-1]
    url = "http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Load2/Data/la"

    payload={}
    headers = {
    'X-M2M-Origin': 'admin:admin',
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = eval(response.text)
    data_cons_120 = data["m2m:cin"]
    Load2 = data_cons_120["con"][13:-1]
    url = "http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Load3/Data/la"

    payload={}
    headers = {
    'X-M2M-Origin': 'admin:admin',
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = eval(response.text)
    data_cons_120 = data["m2m:cin"]
    Load3 = data_cons_120["con"][13:-1]

    url = "http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Solar/Data/la"

    payload={}
    headers = {
    'X-M2M-Origin': 'admin:admin',
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = eval(response.text)
    data_cons_120 = data["m2m:cin"]
    Solar = data_cons_120["con"][13:-1]

    url = "http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/LDR/Data/la"

    payload={}
    headers = {
    'X-M2M-Origin': 'admin:admin',
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = eval(response.text)
    data_cons_120 = data["m2m:cin"]
    LDR = data_cons_120["con"][13:-1]

    url = "http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Conventional/Data/la"

    payload={}
    headers = {
    'X-M2M-Origin': 'admin:admin',
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = eval(response.text)
    data_cons_120 = data["m2m:cin"]
    Conventional = data_cons_120["con"][13:-1]

    return render_template('status.html',Load1=Load1, Load2=Load2,Load3=Load3,Solar=Solar,Conventional=Conventional, LDR=LDR)

@app.route('/notifications',methods=['GET','POST'])
def notifications():
    
    import requests
    import json


    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Load3/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataLoad3=data2['m2m:cin']

    ############################################
    # for i in data3:
    #     print((i['con']))
    # print(type(data3))
        
    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Load2/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataLoad2=data2['m2m:cin']

    ############################################


    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Load1/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataLoad1=data2['m2m:cin']

    ############################################


    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/LDR/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataLDR=data2['m2m:cin']

    ##########################################

    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Solar/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataSun=data2['m2m:cin']

    ##########################################

    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Conventional/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataCon=data2['m2m:cin']


    # print((dataCon))
    # print((dataSun))
    # print((dataLDR))
    # print((dataLoad1))
    # print((dataLoad2))
    # print((dataLoad3))

    rCon=[]
    rSun=[]
    rLoad1=[]
    rLoad2=[]
    rLoad3=[]
    rLDR=[]
    rtime=[]
    Conventional = 0
    Solar = 10
    Load2 = 1
    Load1 = 20
    Load3 = 1

    for i in range(len(dataLDR)):
        dCon=(dataCon[i]['con'])
        dSun=(dataSun[i]['con'])
        dL1=(dataLoad1[i]['con'])
        dL2=(dataLoad2[i]['con'])
        dL3=(dataLoad3[i]['con'])
        dLDR=(dataLDR[i]['con'])
        dL1=dL1.strip('[]').split(',')
        tim=dL1[0].strip()
        dL1=dL1[1].strip()

        dL2=dL2.strip('[]').split(',')
        dL2=dL2[1].strip()

        dL3=dL3.strip('[]').split(',')
        dL3=dL3[1].strip()

        dSun=dSun.strip('[]').split(',')
        dSun=dSun[1].strip()

        dCon=dCon.strip('[]').split(',')
        dCon=dCon[1].strip()

        dLDR=dLDR.strip('[]').split(',')
        dLDR=dLDR[1].strip()

        rCon.append(float(dCon))
        rSun.append(float(dSun))
        rLoad1.append(float(dL1))
        rLoad2.append(float(dL2))
        rLoad3.append(float(dL3))
        rLDR.append(float(dLDR))
        rtime.append(float(tim))
        Conventional = float(dCon)
        Solar = float(dSun)
        Load2 = float(dL2)
        Load1 = float(dL1)
        Load3 = float(dL3)
    
    if(float(Conventional)==0 and float(Solar)!=0):
        message1="Ideal conditions, loads are being powered only through solar"
    elif(float(Solar)==0 and float(Conventional)!=0):
        message1="No solar energy, buildings powered only through Conventional."
    elif(float(Solar)==0 and float(Conventional)==0):
        message1="No power!"
    else:
        message1="Optimal balance between solar and conventional power"

    if((Load1)==0):
        message_hosp = "No Power supply in Hospital"
    else:
        message_hosp=""
        
    if((Load2)==0):
        message_house = "No Power supply in Shop"
    else:
        message_house=""
    if(Load3==0):
        message_fact = "No Power supply in Factory"
    else:
        message_fact=""
    
    if(message_fact=="" and message_hosp=="" and message_house==""):
        message2 = "None. Sufficient power for all buildings"
    else:
        message2=""


    if(float(Conventional)>float(Solar) and Solar!=0):
        message3= "Load's solar limit is reached. Please switch off some appliances to reduce load."
    elif(float(Load1)+float(Load2)+float(Load3)>10):
        message3= "Please switch off some appliances to reduce load."
    else:
        message3="Safe consumption"

    current_time = datetime.datetime.now()
    current_hour = current_time.hour

    if (6 <= current_hour < 20 and float(Solar)==0):
        message4 = "No solar output! Either your solar panel is faulty or there aer chances of heavy rain."
    else:
        message4 = ""
    if (float(Load1)+float(Load2)+float(Load3)>10):
        message5 = "Current overload!"
    else:
        message5=""
    if(message4=="" and message5==""):    
        message4="No Abnormal Alerts!!"
        message5=""
    


    return render_template('notifications.html', message1=message1, message2=message2, message3=message3, message4=message4,message_fact=message_fact,message_hosp=message_hosp,message_house=message_house,message5=message5)

@app.route('/analysis',methods=['GET','POST'])
def analysis():
    import requests
    import json


    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Load3/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataLoad3=data2['m2m:cin']

    ############################################
    # for i in data3:
    #     print((i['con']))
    # print(type(data3))
        
    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Load2/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataLoad2=data2['m2m:cin']

    ############################################


    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Load1/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataLoad1=data2['m2m:cin']

    ############################################


    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/LDR/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataLDR=data2['m2m:cin']

    ##########################################

    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Solar/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataSun=data2['m2m:cin']

    ##########################################

    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Conventional/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataCon=data2['m2m:cin']


    # print((dataCon))
    # print((dataSun))
    # print((dataLDR))
    # print((dataLoad1))
    # print((dataLoad2))
    # print((dataLoad3))

    rCon=[]
    rSun=[]
    rLoad1=[]
    rLoad2=[]
    rLoad3=[]
    rLDR=[]
    rtime=[]


    for i in range(len(dataLDR)):
        dCon=(dataCon[i]['con'])
        dSun=(dataSun[i]['con'])
        dL1=(dataLoad1[i]['con'])
        dL2=(dataLoad2[i]['con'])
        dL3=(dataLoad3[i]['con'])
        dLDR=(dataLDR[i]['con'])
        dL1=dL1.strip('[]').split(',')
        tim=dL1[0].strip()
        dL1=dL1[1].strip()

        dL2=dL2.strip('[]').split(',')
        dL2=dL2[1].strip()

        dL3=dL3.strip('[]').split(',')
        dL3=dL3[1].strip()

        dSun=dSun.strip('[]').split(',')
        dSun=dSun[1].strip()

        dCon=dCon.strip('[]').split(',')
        dCon=dCon[1].strip()

        dLDR=dLDR.strip('[]').split(',')
        dLDR=dLDR[1].strip()

        rCon.append(float(dCon))
        rSun.append(float(dSun))
        rLoad1.append(float(dL1))
        rLoad2.append(float(dL2))
        rLoad3.append(float(dL3))
        rLDR.append(float(dLDR))
        rtime.append(float(tim))

    count_below_2000 = 0
    count_2000_to_2500 = 0
    count_2500_to_3000 = 0
    count_above_3000 = 0

    for value in rLDR:
        if value < 2000:
            count_below_2000 += 1
        elif 2000 <= value <= 2500:
            count_2000_to_2500 += 1
        elif 2500 < value <= 3000:
            count_2500_to_3000 += 1
        elif value > 3000:
            count_above_3000 += 1

    print("Entries below 2000:", count_below_2000)
    print("Entries between 2000 and 2500:", count_2000_to_2500)
    print("Entries between 2500 and 3000:", count_2500_to_3000)
    print("Entries above 3000:", count_above_3000)
        

    

    avg_load1=sum(rLoad1)/len(rLoad1)
    avg_load2=sum(rLoad2)/len(rLoad2)
    avg_load3=sum(rLoad3)/len(rLoad3)
    avgs=[avg_load1,avg_load2,avg_load3]

    rCon, rSun, rLDR, rLoad1, rLoad2, rLoad3, rtime = zip(*sorted(zip(rCon, rSun, rLDR, rLoad1, rLoad2, rLoad3, rtime), key=lambda x: x[2]))
    intervals = [(0, 2000), (2000, 2500), (2500, 3000), (3000, float('inf'))]
    graphInteval=[1,2,3,4]
    Conavg=[]
    Sunavg=[]
    Load1avg=[]
    Load2avg=[]
    Load3avg=[]
    for interval in intervals:
        values = [con for con, ldr in zip(rCon, rLDR) if interval[0] <= ldr < interval[1]]
        average = sum(values) / len(values) if values else 0
        Conavg.append(average)
    
    for interval in intervals:
        values = [con for con, ldr in zip(rSun, rLDR) if interval[0] <= ldr < interval[1]]
        average = sum(value for value in values if (value<0.8 or interval!=(2000, 2500))) / len(values) if values else 0
        Sunavg.append(average)

    for interval in intervals:
        values = [con for con, ldr in zip(rLoad1, rLDR) if interval[0] <= ldr < interval[1]]
        average = sum(value for value in values if (value<0.8 or interval!=(2000, 2500))) / len(values) if values else 0
        Load1avg.append(average)

    for interval in intervals:
        values = [con for con, ldr in zip(rLoad2, rLDR) if interval[0] <= ldr < interval[1]]
        average = sum(value for value in values if (value<0.8 or interval!=(2000, 2500))) / len(values) if values else 0
        Load2avg.append(average)

    for interval in intervals:
        values = [con for con, ldr in zip(rLoad3, rLDR) if interval[0] <= ldr < interval[1]]
        average = sum(value for value in values if (value<0.8 or interval!=(2000, 2500))) / len(values) if values else 0
        Load3avg.append(average)

    return render_template('analysis.html',labels=rLDR,load1=rLoad1,load2=rLoad2,load3=rLoad3,solar=rSun,conventional=rCon,time=rtime,avgs=avgs,graphInteval=graphInteval,Conavg=Conavg,Sunavg=Sunavg,Load1avg=Load1avg,Load2avg=Load2avg,Load3avg=Load3avg)

@app.route('/failure',methods=['GET','POST'])
def failure():
    return render_template('failure.html')

@app.route('/energy',methods=['GET','POST'])
def energy():
    return render_template('energy.html')

##################################################
msg=['']
@app.route('/process-form', methods=['POST','GET'])
def process_form():
    input1 = float(request.form['input1'])
    input2 = float(request.form['input2'])
    input3 = float(request.form['input3'])

    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Load3/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataLoad3=data2['m2m:cin']

    ############################################
    # for i in data3:
    #     print((i['con']))
    # print(type(data3))
        
    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Load2/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataLoad2=data2['m2m:cin']

    ############################################


    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Load1/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataLoad1=data2['m2m:cin']

    ############################################


    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/LDR/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataLDR=data2['m2m:cin']

    ##########################################

    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Solar/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataSun=data2['m2m:cin']

    ##########################################

    url="http://127.0.0.1:5089/~/in-cse/in-name/AE-TEST/Conventional/Data?rcn=4"
    payload={}
    headers={
        'X-M2M-Origin':'admin:admin',
        'Accept':'application/json'
    }
    response=requests.request("GET",url,headers=headers,data=payload)

    data=eval(response.text)
    data2=data['m2m:cnt']
    dataCon=data2['m2m:cin']


    # print((dataCon))
    # print((dataSun))
    # print((dataLDR))
    # print((dataLoad1))
    # print((dataLoad2))
    # print((dataLoad3))

    rCon=[]
    rSun=[]
    rLoad1=[]
    rLoad2=[]
    rLoad3=[]
    rLDR=[]
    rtime=[]


    for i in range(len(dataLDR)):
        dCon=(dataCon[i]['con'])
        dSun=(dataSun[i]['con'])
        dL1=(dataLoad1[i]['con'])
        dL2=(dataLoad2[i]['con'])
        dL3=(dataLoad3[i]['con'])
        dLDR=(dataLDR[i]['con'])
        dL1=dL1.strip('[]').split(',')
        tim=dL1[0].strip()
        dL1=dL1[1].strip()

        dL2=dL2.strip('[]').split(',')
        dL2=dL2[1].strip()

        dL3=dL3.strip('[]').split(',')
        dL3=dL3[1].strip()

        dSun=dSun.strip('[]').split(',')
        dSun=dSun[1].strip()

        dCon=dCon.strip('[]').split(',')
        dCon=dCon[1].strip()

        dLDR=dLDR.strip('[]').split(',')
        dLDR=dLDR[1].strip()

        rCon.append(float(dCon))
        rSun.append(float(dSun))
        rLoad1.append(float(dL1))
        rLoad2.append(float(dL2))
        rLoad3.append(float(dL3))
        rLDR.append(float(dLDR))
        rtime.append(float(tim))

    X=X = list(zip( rLoad1, rLoad2, rLoad3))
    y=rLDR
    cap=1000
    X = [sample for sample in X if max(sample) <= cap]
    y = [target for sample, target in zip(X, y) if max(sample) <= cap]


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    degree = 3

    poly_features = PolynomialFeatures(degree=degree)
    X_train_poly = poly_features.fit_transform(X_train)
    X_test_poly = poly_features.transform(X_test)

    model = LinearRegression()

    model.fit(X_train_poly, y_train)

    y_train_pred = model.predict(X_train_poly)
    y_test_pred = model.predict(X_test_poly)

    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)
    print("Training R-squared score:", train_r2)
    print("Testing R-squared score:", test_r2)



    X_new=[[input1, input2, input3]]

    for X_list in X_new:
        X_list.sort(reverse=True)

    X_new_poly = poly_features.transform(X_new)

    y_new_pred = model.predict(X_new_poly)

    msg.append(y_new_pred)
    return redirect(url_for('predictive'))

@app.route('/predictive',methods=['GET','POST'])
def predictive():
    predLDR=msg[-1]
    str=''
    if predLDR!='':
        predLDR=float(predLDR)
        if predLDR < 2000 and predLDR>0:
            str='''In the broad daylight solar energy would be able to run this by itself.
            During night time, Conventional alone can easily support this scenario, This can run the whole day.
            '''
        elif predLDR<=0 or predLDR>5000:
            str='Invalid Data'
        elif predLDR>=2000 and predLDR < 2500:
            str='''Conventional Energy and a bit of Solar Energy would be optimal for these load requirements,
            This can run for most parts of the day except night.'''
        elif predLDR>=2500 and predLDR<3000:
            str='''Moderate amount of Sunlight and Conventional Power is optimal for this Load,
            Conventional alone will not be able to satisfy this. This will run at times of medium to high sunlight.'''
        elif predLDR>=3000:
            str='''A lot of Energy is required for this load, This might work only when there is a large amount of sunlight. '''
        else:
            str=''
    return render_template('predictive.html',msg=str)

#####################################################################
if __name__=='__main__':
    app.run(debug=True,port=5100)