from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RoadReportForm


def report_road_condition(request):
    if request.method == 'POST':
        form = RoadReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for reporting the road condition!')
            return redirect('report_road')
    else:
        form = RoadReportForm()
    return render(request, 'road_report.html', {'form': form})
