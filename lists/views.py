from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "home.xhtml", {"new_item_text": request.POST.get("item_text")})
