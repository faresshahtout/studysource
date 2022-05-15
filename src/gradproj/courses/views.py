from django.shortcuts import render





# def java_view(request):
#     context={'':''}
#     context={
#         'description':'',
#         'course_name':'c++',
#         'link':'https://www.youtube.com/embed/?listType=playlist&list=change this'
#
#     }
#     return render(request=request, template_name=r"coursesList.html", context=context)
# Create your views here.
def c_view(request):
    context={'':''}
    context={
        'description':'',
        'course_name':'c++',
        'link':'https://www.youtube.com/embed/?listType=playlist&list=PL1DUmTEdeA6IUD9Gt5rZlQfbZyAWXd-oD'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)
def java_view(request):
    context={'':''}
    context={
        'description':'',
        'course_name':'Java',
        'link':'https://www.youtube.com/embed/?listType=playlist&list=PL1DUmTEdeA6Icttz-O9C3RPRF8R8Px5vk'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)
def ds_view(request):
    context={'':''}
    context={
        'description':'',
        'course_name':'Data Structure',
        'link':'https://www.youtube.com/embed/?listType=playlist&list=PLE_E4BccYnp3vpaLpNTQYZYvdxZViD0vs'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)
def vs_view(request):
    context={'':''}
    context={
        'description':'',
        'course_name':'Visual Basic',
        'link':'https://www.youtube.com/embed/?listType=playlist&list=PLdUHNiwJgn86zVowX6MklKqa2_6SnY1CX'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def java_view(request):
    context={'':''}
    context={
       'description':'',
       'course_name':'c++',
        'link':'https://www.youtube.com/embed/?listType=playlist&list=change this'
     }
    return render(request=request, template_name=r"coursesList.html", context=context)