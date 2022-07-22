from django.shortcuts import  render, redirect


def faq_view(request):
    return render(request=request, template_name=r"about-us.html", context={'':''})


def handler(request,exception):
    return render(request=request, template_name=r"nof-found.html", )