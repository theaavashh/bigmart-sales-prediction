from django.shortcuts import render
import pandas as pd

# Create your views here.
def createDB(file_path):
    df_train=pd.read_csv(file_path,delimiter=',')
    val=df_train.describe()
    print(val)


def dataset(request):
    if request.method == "POST":
        file=request.FILES['file']
        obj=File.objects.create(file=file)
        createDB(obj.file)

    return render(request,"dataset.html")

