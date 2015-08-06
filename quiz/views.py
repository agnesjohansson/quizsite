from django.shortcuts import render

# Create your views here.
def startpage (request):
	return render (request, "quiz/startpage.html")

def startpage (request):
	return render (request, "quiz/quiz.html")

def startpage (request):
	return render (request, "quiz/question.html")

def startpage (request):
	return render (request, "quiz/completed.html")