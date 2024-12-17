from django.template import loader
from django.shortcuts import render
from .models import reference
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
@csrf_protect
def references(request):
    return render(request,"refer.html",{'request':request})

def reference_insert(request):
    
    vrefer= request.POST['reference']
    vcourse =request.POST['coursecode']
    vacademic=request.POST['academic_yr']
    
    ap = reference(referencesis=vrefer,coursecode=vcourse,academic_yr=vacademic)
    ap.save()
    return render(request, 'refer.html',{})