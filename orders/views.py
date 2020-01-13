from django.shortcuts import render, redirect
from .models import Order
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def order(request):
    if request.method == 'POST':
        project_title = request.POST['project_title']
        project_category = request.POST['project_category']
        project_id = request.POST['project_id']
        project_slug = request.POST['project_slug']
        name = request.POST['name']
        email = request.POST['email']
        price = request.POST['price']
        photo_card = request.POST['photo_card']
        user_id  = request.POST['user_id']

        #submitting form to the database
        order = Order(
            project_title = project_title,
            project_category = project_category,
            project_id = project_id,
            project_slug = project_slug,
            name = name,
            email = email,
            price  = price,
            photo_card = photo_card,
            user_id = user_id
        )
        
        order.save()
        messages.success(request, 'Your purchase of '+ project_title +' is completed successfully. You can watch now.  ')
        return redirect('/projects/'+project_slug)
