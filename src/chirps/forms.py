from django import forms



from .models import Chirp

class TweetModelForm(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': "Your message", "class": "form-control"}))
	class Meta:
		model = Chirp
		fields = [
			#"user",
			"content"
		]
#	def clean_content(self, *arg, **kwargs):
		#content = self.cleaned_data.get("content")
		#if content == "abc":
		#	raise forms.ValidationError("Cannot be ABC")
		#return content	