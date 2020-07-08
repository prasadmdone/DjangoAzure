from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
# Create your views here.
from sklearn.externals import joblib

#classifier=joblib.load('./models/RFModelforMPG.pkl')


def home(request):
  
    context ={'temp':'Welcome!'}
    return render(request,'index.html',context)

def inputindex(request):

    return render(request,'input.html')

