from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report

def index(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)  # create a new report object
            report.save()  # save the report to the database
            return redirect('index')
    else:
        form = ReportForm()
    return render(request, 't_form/index.html', {'form': form})
