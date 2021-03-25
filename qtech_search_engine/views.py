from django.shortcuts import render, redirect
from django.http import HttpResponse

from qtech_search_engine.models import KeywordDescriptionModel, AllUsers

# Create your views here.

def HomeView(request):

    keywords = KeywordDescriptionModel.objects.all()

    context = {
        'keywords': keywords,
    }
    return render(request, "qtech_search_engine/home.html", context)


def SearchView(request):
    
    try:
        print("Trying")
        print(request.COOKIES['device'])
        customer, created = AllUsers.objects.get_or_create(user_sid = request.COOKIES['device'])
        if created is True:
            print("creating")
            counter = AllUsers.objects.all().count()
            customer.username = "User " + str(counter)
            customer.save()

        if "keyword_submit_button" in request.POST:
            print("Searching: ", request.POST['keyword_query'])
            try:
                keyword_instance = KeywordDescriptionModel.objects.get(keyword=request.POST['keyword_query'])
                keyword_searched_counter = keyword_instance.times_searched + 1
                print(keyword_searched_counter)
                keyword_instance.times_searched = keyword_searched_counter
                keyword_instance.save()
                
                print("Updated counter")
                
                keyword_instance.user.add(customer)
                keywords = KeywordDescriptionModel.objects.all()
                searches = KeywordDescriptionModel.objects.filter(keyword=request.POST['keyword_query'])
                
                

                context = {
                    'keywords': keywords,
                    'searches': searches
                }
                return render(request, "qtech_search_engine/results.html", context)
            except:
                print("")
    except:
        print("No cookie found")

    context = {

    }

    return render(request, "qtech_search_engine/search.html", context)

def TestView(request):
    keywords = KeywordDescriptionModel.objects.all()

    context = {
        'keywords': keywords,
    }
    return render(request, "qtech_search_engine/test.html", context)