from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404
from books.models import Book

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
	errors = []
	if 'q' in request.GET:
    		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q)>20:
			errors.append('Please enter at most 20 characters')
        	else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html',{'books':books,'query':q})
	return render_to_response('search_form.html',{'errors': errors})        

from django.core.mail import send_mail
from django.http import HttpResponseRedirect


def contact_form(request):
	errors = []
	if request.method =='POST':
		if not request.POST.get('subject',''):
			errors.append('Enter a subject')
		if not request.POST.get('message',''):
			errors.append('Enter a messagt')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid e-mail address.')
		if not errors:
			send_mail(
				request.POST['subject'],
				request.POST['message'],
				request.POST.get('email','noreply@example.com'),
				['siteowner@example.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	return render_to_response('contact_form.html',{
		'errors':errors,
		'subject':request.POST.get('subject',''),
		'message':request.POST.get('message',''),
		'email':request.POST.get('email',''),
	})	

from books.forms import ContactForm

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email','noreply@example.com'),
				['siteowner@example.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial={'subject':'I love your site!'}
		)

	return render_to_response('contact_form.html',{'form':form})