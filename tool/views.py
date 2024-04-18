from django.shortcuts import render
import re

# Create your views here.

def home(request):
    return render(request, 'tool/home.html')

def check_regex(request):
    regex = request.POST.get('regex')
    text = request.POST.get('string')
    matches = re.finditer(regex, text)
    result = ()
    for match in matches:
        print("Match found:", match.group())
        result = result + (match.group(),)

    if matches:
        return render(request, 'tool/home.html', {'results': result})
    else:
        return render(request, 'tool/home.html')

    