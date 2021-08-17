from django.http import HttpResponse
from django.shortcuts import render
import pickle
import numpy as np
from keras.models import load_model
from PIL import Image

def home(request):
    return render(request,'home.html')

def cancer(request):    
    return render(request,'cancer.html')

def heart(request):    
    return render(request,'heart.html')


def kidney(request):    
    return render(request,'kidney.html')

def malaria(request):    
    return render(request,'malaria.html')

def pneumonia(request):    
    return render(request,'pneumonia.html')

def cancerresult(request):
    model=pickle.load(open('models/cancer.pkl','rb'))
    lis=[]
    lis.append(request.POST['texture_mean'])
    lis.append(request.POST['area_mean'])
    lis.append(request.POST['smoothness_mean'])
    lis.append(request.POST['compactness_mean'])
    lis.append(request.POST['concavity_mean'])
    lis.append(request.POST['symmetry_mean'])
    lis.append(request.POST['area_se'])
    lis.append(request.POST['smoothness_se'])
    lis.append(request.POST['compactness_se'])
    lis.append(request.POST['concavity_se'])
    lis.append(request.POST['concave points_se'])
    lis.append(request.POST['fractal_dimension_se'])
    lis.append(request.POST['smoothness_worst'])
    lis.append(request.POST['compactness_worst'])
    lis.append(request.POST['concavity_worst'])
    lis.append(request.POST['symmetry_worst'])
    lis.append(request.POST['fractal_dimension_worst'])
    lis=np.asarray(lis)
    pred=int(model.predict(lis.reshape(1,-1)))
    if pred==0:
         return render(request,'result.html',{'pred':'The cancer is Benign'})
    elif pred==1:
        return render(request,'result.html',{'pred':'The cancer is Malignant'})

def heartresult(request):
    model=pickle.load(open('models/heart.pkl','rb'))
    lis=[]
    lis.append(request.POST['age'])
    lis.append(request.POST['sex'])
    lis.append(request.POST['cp'])
    lis.append(request.POST['trestbps'])
    lis.append(request.POST['restecg'])
    lis.append(request.POST['thalach'])
    lis.append(request.POST['exang'])
    lis.append(request.POST['oldpeak'])
    lis.append(request.POST['slope'])
    lis.append(request.POST['ca'])
    lis.append(request.POST['thal'])
    lis=np.asarray(lis)
    pred=int(model.predict(lis.reshape(1,-1)))
    if pred==0:
         return render(request,'result.html',{'pred':'No presence of heart disease'})
    elif pred==1:
        return render(request,'result.html',{'pred':'Presence of heart disease'})

def kidneyresult(request):
    model=pickle.load(open('models/kidney.pkl','rb'))
    lis=[]
    lis.append(request.POST['age'])
    lis.append(request.POST['bp'])
    lis.append(request.POST['sg'])
    lis.append(request.POST['al'])
    lis.append(request.POST['su'])
    lis.append(request.POST['rbc'])
    lis.append(request.POST['pc'])
    lis.append(request.POST['pcc'])
    lis.append(request.POST['ba'])
    lis.append(request.POST['bgr'])
    lis.append(request.POST['bu'])
    lis.append(request.POST['sc'])
    lis.append(request.POST['sod'])
    lis.append(request.POST['pot'])
    lis.append(request.POST['hemo'])
    lis.append(request.POST['pcv'])
    lis.append(request.POST['wc'])
    lis.append(request.POST['rc'])
    lis.append(request.POST['htn'])
    lis.append(request.POST['dm'])
    lis.append(request.POST['cad'])
    lis.append(request.POST['appet'])
    lis.append(request.POST['pe'])
    lis.append(request.POST['ane'])
    lis=np.asarray(lis)
    pred=int(model.predict(lis.reshape(1,-1)))
    if pred==0:
         return render(request,'result.html',{'pred':'Chronic kidney disease'})
    elif pred==1:
        return render(request,'result.html',{'pred':'Disease is not Not chronic'})

def malariaresult(request):
    model = load_model("models/malaria.h5")
    if request.method == 'POST':
        img= Image.open(request.FILES['image']).convert('L')
    img = img.resize((64,64)) 
    img = np.asarray(img) 
    img = img.reshape((1,64,64,1))
    img = img / 255.0
    pred = np.argmax(model.predict(img)[0])
    if pred==0:
         return render(request,'result.html',{'pred':'The cell is Parasitized'})
    elif pred==1:
        return render(request,'result.html',{'pred':'The cell is Uninfected'})

def pneumoniaresult(request):
    model = load_model("models/pneumonia.h5")
    if request.method == 'POST':
        img= Image.open(request.FILES['image']).convert('L')
    img = img.resize((150,150)) 
    img = np.asarray(img) 
    img = img.reshape((1,150,150,1))
    img = img / 255.0
    pred = np.argmax(model.predict(img)[0])
    if pred==0:
         return render(request,'result.html',{'pred':'The person is normal'})
    elif pred==1:
        return render(request,'result.html',{'pred':'The person have Pneumonia'})
