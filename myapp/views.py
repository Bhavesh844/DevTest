from django.shortcuts import render,redirect
from myapp.models import upload_file
from django.http import FileResponse
import pandas as pd


# Create your views here.

import pandas as pd

def home(request):
    f = upload_file.objects.all()
    try:
        if request.method == "POST":
            file = request.FILES.get('file')
            u = upload_file(file=file)
            u.save()
            
        return render(request, 'emp/home.html', {'f': f})
    except Exception as e:
        print(e)
    return render(request, 'emp/home.html', {'f': f})

def download_file(request,id):
    u=upload_file.objects.get(id=id)
    return FileResponse(u.file,as_attachment=True)

def process_file(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        return "Unsupported file format"

    summary = {
        'total_rows': len(df),
        'columns': df.columns.tolist(),
        'first_rows': df.head(5).values.tolist()  # Convert the first few rows to a list of lists
    }

    return summary


def file_summary(request, id):
    u = upload_file.objects.get(id=id)
    summary_report = process_file(u.file)
    return render(request, 'emp/file_summary.html', {'summary_report': summary_report})

def delete_file(request,id):
    u=upload_file.objects.get(id=id)
    u.delete()
    return redirect('home')
