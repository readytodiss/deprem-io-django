from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from .models import GidaIhtiyaci



def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def gida_ihtiyacim_var(request):
    return render(request, 'gidaihtiyacimvar.html')

def gidaihtiyacimvar(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullName', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        human_count = request.POST.get('humanCount', '')
        address = request.POST.get('address', '')
        address_description = request.POST.get('address_description', '')
        physical_info = request.POST.get('physicalInfo', '')
        tweet_link = request.POST.get('tweetLink', '')
        
        gidaihtiyaci = GidaIhtiyaci(
            fullname=fullname,
            email=email,
            phone=phone,
            human_count=human_count,
            address=address,
            address_description=address_description,
            physical_info=physical_info,
            tweet_link=tweet_link
        )
        gidaihtiyaci.save()
        
        return redirect('members')  # Kaydedildikten sonra yönlendirilecek URL'yi buraya yazın
    
    return render(request, 'gidaihtiyacimvar.html')

def gidaihtiyaciolanlar(request):
    gidaihtiyaci_listesi = GidaIhtiyaci.objects.all()
    return render(request, 'gidaihtiyaciolanlar.html', {'gidaihtiyaci_listesi': gidaihtiyaci_listesi})