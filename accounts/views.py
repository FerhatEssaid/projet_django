from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login ,logout,authenticate
from django.contrib import messages  # Pour afficher les messages d'erreur

User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Vérification si le nom d'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
            return redirect('signup')  # Redirige vers la même page avec un message

        # Créer un nouvel utilisateur
        user = User.objects.create_user(username=username, password=password)

        # Connecter automatiquement l'utilisateur
        login(request, user)
        
        return redirect('index')

    return render(request, 'accounts/signup.html')


def logout_user (request):
    logout(request)
    return redirect('index')


def login_user(request) :

    if request.method=="POST" :
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')



    return render(request,'accounts/login.html')


    

