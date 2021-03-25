from django.shortcuts import render, redirect
from django.http import HttpResponse

from qtech_search_engine.models import KeywordDescriptionModel, AllUsers

# Create your views here.

def HomeView(request):

    searches = KeywordDescriptionModel.objects.all()
    try:
        print(request.COOKIES['device'])
    except:
        print("No cookie found")

    context = {
        'searches': searches
    }

    return render(request, "qtech_search_engine/home.html", context)


def SearchView(request):

    # searches = KeywordDescriptionModel.objects.all()
    try:
        print("Trying")
        print(request.COOKIES['device'])
        customer, created = AllUsers.objects.get_or_create(user_sid = request.COOKIES['device'])
        if created is True:
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
                print("Updating counter")
                keyword_instance.save()
                print("Saving instance")
                for i in KeywordDescriptionModel.objects.filter(keyword=request.POST['keyword_query']):
                    customer.keyword.add(keyword_instance)
                customer.save()
                users = AllUsers.objects.all()
                keywords = KeywordDescriptionModel.objects.filter(times_searched=0)
                searches = KeywordDescriptionModel.objects.filter(keyword=request.POST['keyword_query'])

                context = {
                    'users': users,
                    'keyword': keywords,
                    'searches': searches
                }
                return render(request, "qtech_search_engine/results.html", context)
            except:
                print("")
    except:
        print("No cookie found")

    # customer, created = Customer.objects.get_or_create(device=device)

    context = {

    }

    return render(request, "qtech_search_engine/search.html", context)

def TestView(request):
    users = AllUsers.objects.all()
    keywords = KeywordDescriptionModel.objects.filter(times_searched=0)

    context = {
        'users': users,
        'keyword': keywords,
    }
    return render(request, "qtech_search_engine/test3.html", context)