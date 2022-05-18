from django.shortcuts import render
from .models import rating
# Create your views here.
def faq_view(request):
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('subject'):
            post = rating()
            post.user = request.POST.get('firstname')
            post.submission = request.POST.get('subject')
            post.save()

            return render(request,'about-us.html')

    else:
        return render(request,'about-us.html')

    return render(request=request, template_name="about-us.html", context={"":""})