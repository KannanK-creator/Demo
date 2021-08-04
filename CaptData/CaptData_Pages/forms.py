from django import forms
from CaptData_DB.models import CaptData_Tbl

class CaptData_Form(forms.ModelForm):
	class Meta:
		model 	= 	CaptData_Tbl
		fields 	=	['CaptData_ID', 'CaptData_Val']