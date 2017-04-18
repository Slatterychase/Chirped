from django.contrib import admin

# Register your models here.
from .forms import TweetModelForm
from .models import Chirp

#admin.site.register(Chirp)



class TweetModelAdmin(admin.ModelAdmin):
	#form = TweetModelForm
	class Meta:
		model = Chirp
		
#admin.site.unregister(Chirp)
admin.site.register(Chirp, TweetModelAdmin)		