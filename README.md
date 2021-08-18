# Multiple_disease_detection

## About

This webapp was developed using Django Framework and was deployed on Heroku server. All the links for datasets and the python notebooks used for model creation are mentioned below in this readme.You can access the website live at: (https://multiple-disease-detection-irs.herokuapp.com/) The webapp can predict following Diseases:

* Breast Cancer
* Heart Disease
* Kidney Disease
* Malaria
* Pneumonia

## Steps to run the WebApp in local Computer
**Step-1**: Download the files in the repository.
**Step-2**: Get into the downloaded folder, open command prompt in that directory and install all the dependencies using following command
```
pip install -r requirements.txt
```
**Step-3**: After successfull installation of all the dependencies, run the following command
```
python manage.py runserver
```

## Dataset links
* [Breast Cancer Dataset](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data)
* [Heart Disease Dataset](https://www.kaggle.com/ronitf/heart-disease-uci)
* [Kidney Disease Dataset](https://www.kaggle.com/mansoordaku/ckdisease)
* [Malaria Dataset](https://www.kaggle.com/iarunava/cell-images-for-detecting-malaria)
* [Pneumonia Dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

## Links for Python Notebooks used for model creation
* [Breast Cancer](https://github.com/irshad256/Multiple_disease_detection/blob/main/notebooks/Breast%20Cancer.ipynb)
* [Heart Disease Dataset](https://github.com/irshad256/Multiple_disease_detection/blob/main/notebooks/Heart%20Disease.ipynb)
* [Kidney Disease](https://github.com/irshad256/Multiple_disease_detection/blob/main/notebooks/Kidney%20Disease.ipynb)
* [Malaria](https://github.com/irshad256/Multiple_disease_detection/blob/main/notebooks/malaria.ipynb)
* [Pneumonia](https://github.com/irshad256/Multiple_disease_detection/blob/main/notebooks/pneumonia.ipynb)
