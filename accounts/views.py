from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordResetView
from .forms import UserUpdateForm
from orders.models import Order
from django.db.models import Sum, Count, Max
from django.http import JsonResponse, HttpResponse
from django.core import serializers
# from django.utils.timezone import datetime 
from datetime import datetime



# Create your views here
def register(request):
    #if user is authenticated already and try to use login url, this will redirect to another page
    if request.user.is_authenticated :
        return redirect('dashboard')

    #user registration
    if request.method == 'POST':
        #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if password match
        if password == password2:
            #checks username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken, Please try different username')
                return redirect('register')
            else:
                #checks email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email already exists, Please use  different email')
                    return redirect('register')
                else:
                    #looks good
                    # user registered as a new user, now user can log in...
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )

                    #login after registered // if you want user to automatically login
                    # // after registered, use this code below,

                    # auth.login(request, user)
                    # messages.success(request, 'Welcome ! You are now logged in')
                    # return redirect('index')

                    #redirect to login page after registered // if you want user to manually login
                    # // after registered, use this code below,

                    user.save();
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):

    #if user is authenticated already and try to use login url, this will redirect to another page
    if request.user.is_authenticated :
        return redirect('dashboard')

    #login authentication

    if request.method == 'POST':
        #login user
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request, 'You are now logged out')
        return render(request,'accounts/logout.html')   

@login_required
def dashboard(request):

    user_orders = Order.objects.order_by('order_date').filter(user_id=request.user.id)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('dashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)

    videos_count = Order.objects.filter(user_id=request.user.id).count()
    money_spent = Order.objects.filter(user_id=request.user.id).aggregate(Sum('price'))

    print(money_spent)

    context = {
        'u_form':u_form,
        'orders':user_orders,
        'videos_count':videos_count,
        'money_spent':money_spent,
    }
    
    return render(request, 'accounts/dashboard.html', context)
    
@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    orders = Order.objects.order_by('-order_date')
    total_revenue = Order.objects.all().aggregate(Sum('price'))
    total_orders = Order.objects.count()
    counts = Order.objects.values("project_id","project_title","price","project_category").annotate(Count("project_id")).order_by('-price')[:5]
    theatre_revenue = Order.objects.filter(project_category="THEATRE").aggregate(Sum('price'))
    theatre_orders = Order.objects.filter(project_category="THEATRE").count()
    movie_revenue = Order.objects.filter(project_category="MOVIE").aggregate(Sum('price'))
    movie_orders = Order.objects.filter(project_category="MOVIE").count()
    today_date = datetime.now()
    today = Order.objects.filter(order_date__date=datetime.date(today_date)).values('order_date__date').order_by('-order_date__date').annotate(sum=Sum('price')).annotate(Count("project_id"))
    daily = Order.objects.filter().values('order_date__date').order_by('-order_date__date').annotate(sum=Sum('price')).annotate(Count("project_id"))
    videos = Order.objects.values("project_id","project_title","price","project_category").annotate(Count("project_id")).order_by('-price')
    users = User.objects.all()

    print(today)

    context = {
        'orders':orders,
        'revenue':total_revenue,
        'total_orders':total_orders,
        'counts':counts,
        'theatre_revenue':theatre_revenue,
        'theatre_orders':theatre_orders,
        'movie_revenue':movie_revenue,
        'movie_orders':movie_orders,
        'today':today,
        'daily':daily,
        'videos':videos,
        'users':users,
    }

    return render(request, 'accounts/admin_dashboard_1.html',context)

