from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
# Model -> View -> Template
# Model -> View -> React.js / Vue.js

from .forms import EmailEntryForm
from .models import EmailEntry


html_str = "<!doctype html><html><body><h1>{email}</body></html>"

# @login_required
@staff_member_required(login_url='/login')
def email_entry_get_view(request, id=None, *args, **kwargs):
    # get a single item stored in the database
    # print(args, kwargs)
    # obj = EmailEntry.objects.get(id=id)
    # if not request.user.is_staff:
    #     return render(request, "not-allowed.html")
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404
    # my_html = html_str.format(email=obj.email)
    # return HttpResponse(f"<h1>Hello {obj.email}</h1>")
    return render(request, "get.html", {"object": obj, "email": "abc@gmail.com"})

# def email_entry_list_view():
#     return

def email_entry_create_view(request, *args, **kwargs):
    context = {}
    if request.user.is_authenticated:
        context['some_cool_stuff'] = "Whatever"
    print(request.user, request.user.is_authenticated) # is_authenticated()
    # if request.method == "POST":
    #        DONT DO THIS!
    #     print(dict(request.POST))
    #     data = dict(request.POST)
    #     try:
    #         del data['csrfmiddlewaretoken']
    #     except:
    #         pass
    #     obj = EmailEntry(**data)
    #     obj.save()
    form = EmailEntryForm(request.POST or None)
    context['form'] = form
    if form.is_valid():
        '''
        obj = form.save(commit=False) # Model Instance
        # obj.name = "Justin"
        obj.save()
        new_id = obj.id
        '''
        form.save()        
        form = EmailEntryForm()
        # return HttpResponseRedirect(f"/email/{new_id}")
    return render(request, "form.html", context)

# def email_entry_update_view():
#     return

# def email_entry_destroy_view():
#     return