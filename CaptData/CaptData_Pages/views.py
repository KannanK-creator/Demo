from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CaptData_Form

# Create your views here.

def about_page(request, *args, **kwargs):
	return HttpResponse("<h1>About Page</h1>")

def home_page(request, *args, **kwargs):
	user_nam_blk = { 'User_Nam' : 'Kannan Kathiresan' }
	return render(request,'Home_Page.html',user_nam_blk)

def captdata_page(request, *args, **kwargs):
	CaptData_Frm = CaptData_Form()
	if request.method == "POST" and "Submit" in request.POST:
		CaptData_Frm = CaptData_Form(request.POST)
		print("here")
		if CaptData_Frm.is_valid():
			print(CaptData_Frm.cleaned_data)
			CaptData_Frm.save()
			return redirect('/captdata/')		
	CaptData_Blk_frm = { 'CaptData_Blk' : CaptData_Frm }
	return render(request,'CaptData_Pages.html',CaptData_Blk_frm)

