from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from .models import *


def loginPage(request):
    context={}
    if request.method == "POST":
        submit = request.POST.get("submit")
        if submit == "login":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect ("dashboardPage")
            else:
                messages.warning(request,"kullanıcı adı veya şifre yanlış")
                return redirect ("loginPage")
        
        if submit == "register":
            fname = request.POST.get("fname")
            username_register = request.POST.get("username_register")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            
            password_bool = email_bool = username_register_bool = True

            if password1 != password2:
                password_bool = False
                messages.warning(request,"Şifreler aynı değil")
            if User.objects.filter(email = email).exists():
                email = False
                messages.warning(request,"Bu email zaten kullanılmakta")
            if User.objects.filter(username = username_register).exists():
                username_register_bool = False

            if password_bool and email_bool and username_register_bool:
                user = User.objects.create_user(first_name = fname,email = email,username=username_register,password=password1)
                user.save()
                
                Profile.objects.create(user=user,loginUser=False)

                return redirect("dashboardPage")
    return render(request, 'login-register.html', context)


def logoutUser(request):
    logout(request)
    return redirect("dashboardPage")


# comment
def postDetail(request,pk):
    subject = Subject.objects.get(slug=pk)
    comments = Comment.objects.filter(subject_brand__subjectBrand =subject)
    
    if request.method == 'POST':
        text = request.POST.get("text")
        comment = Comment(text=text,subject_brand=subject)
        comment.save()
        return redirect('/postDetail/'+ pk )
    
    context = {
        "comments":comments,
        "subject":subject
        }
    
    return render(request,'postDetail.html',context)
    
    
    
    
def messagePost(request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        subject_brand = request.POST.get("subject")
        text = request.POST.get("text")
        comment = Comment(text=text, subject_brand__subjectBrand=subject_brand)
        comment.save()
        return redirect('/forumDetail')
    print("comment", comments )
    context={
        "comments":comments,
    }
    return render (request, 'messagePost.html', context)

<<<<<<< HEAD
# def messagePost(request, pk):
#     games = GameCard.objects.get(slug=pk)
#     comments = Comment.objects.filter(game_cate__slug=games.slug)
    
#     if request.method == 'POST':
#         subject_brand = request.POST.get("subject")
#         text = request.POST.get("text")
#         comment = Comment(text=text, subject_brand=subject_brand, game_cate=games)
#         comment.save()
#         return redirect(reverse('forumDetail', args=[pk]))  # Dinamik URL oluşturma
    
#     context = {
#         "comments": comments,
#         "game": games
#     }
#     return render(request, 'messagePost.html', context)


# def messagePost(request, pk):
#     print("asdsasad",pk)
#     games = GameCard.objects.get(slug=pk)
#     # subjects = Subject.objects.all()  # Tüm konu başlıklarını alın
    
#     if request.method == 'POST':
#         subject_id = request.POST.get("subject")  # Formdan seçilen konu başlığının ID'sini alın
#         text = request.POST.get("text")
#         subject = Subject.objects.get(id=subject_id)  # ID'ye göre ilgili konu başlığını alın
#         comment = Comment(text=text, subject_brand=subject, game_cate=games)
#         comment.save()
#         return redirect(reverse('forumDetail', args=[pk]))
    
#     context = {
#         # "subjects": subjects,
#         "game": games
#     }
#     return render(request, 'messagePost.html', context)


=======
def accountUser(request):
    context = {}
    return render(request, 'accountUser.html', context)
>>>>>>> 2ad1e8399229d28aac620cc915ff77d690f71f68
