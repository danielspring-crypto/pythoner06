from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'app/index.html')

def daniel(request):
	return render(request, 'app/daniel.html')

def swe(request):
	return render(request, 'app/swe.html')

def theresa(request):
	return render(request, 'app/theresa.html')

def aye(request):
	return render(request, 'app/aye.html')

def kyi(request):
	return render(request, 'app/kyi.html')

def henry(request):
	return render(request, 'app/henry.html')
