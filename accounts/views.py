from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate , logout
from .forms import RegistrationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from friendship.models import FriendshipRequest
from .models import FriendRequest, Message
from friendship.models import FriendshipRequest, Friend
from django.db.models import Q

# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('realtor:home')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form' : form}) 


def register(request):  
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = RegistrationForm()
    return render(request,'accounts/register.html', {'form' : form})  

def logout_view(request):
    logout (request)
    if request.method == "POST":
        return JsonResponse({'success': True})
    return redirect ('accounts:login')     

def delete_view(request):
    request.user.delete() 
    return redirect('accounts:login')

@login_required
def send_friend_request(request, receiver_id):
    # Get the recipient user based on the receiver_id
    recipient = User.objects.get(id=receiver_id)

    # Check if a friend request already exists
    existing_request = FriendshipRequest.objects.filter(from_user=request.user, to_user=recipient).first()

    if existing_request:
        # A request already exists, so you can render a template with a message
        return render(request, 'accounts/friend_request_already_sent.html')

    # Create a new friend request
    FriendshipRequest.objects.create(
        from_user=request.user,
        to_user=recipient,
        message="Let's be friends!"
    )

    return redirect('accounts:users_list')


@login_required
def users_list(request):
    users = User.objects.exclude(id=request.user.id)  # Exclude the current user from the list
    return render(request, 'accounts/users_list.html', {'users': users})

@login_required
def accept_friend_request(request, request_id):
    if request.user.is_authenticated:
        friend_request = FriendRequest.objects.get(id=request_id)
        if request.user == friend_request.receiver:
            friend_request.status = 'accepted'
            friend_request.save()
    return redirect('accounts:friend_requests')

@login_required
def decline_friend_request(request, request_id):
    if request.user.is_authenticated:
        friend_request = FriendRequest.objects.get(id=request_id)
        if request.user == friend_request.receiver:
            friend_request.status = 'declined'
            friend_request.save()
    return redirect('accounts:friend_requests')

def friend_request_list_view(request):
    # Retrieve friend requests for the logged-in user
    friend_requests = FriendshipRequest.objects.filter(to_user=request.user)
    
    context = {
        'friend_requests': friend_requests
    }
    return render(request, 'accounts/friend_request_list.html', context)

def accepted_friends_list_view(request):
    # Retrieve accepted friends for the logged-in user
    accepted_friends = Friend.objects.friends(request.user)
    
    context = {
        'accepted_friends': accepted_friends
    }
    return render(request, 'accounts/accepted_friends_list.html', context)

@login_required
def send_message(request, recipient_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        recipient = User.objects.get(id=recipient_id)
        message = Message(sender=request.user, recipient=recipient, content=content)
        message.save()
        return redirect('accounts:chat_with', recipient_id=recipient_id)

    return render(request, 'accounts/send_message.html')

@login_required
def chat_with(request, recipient_id):
    recipient = User.objects.get(id=recipient_id)
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=recipient)) | (Q(sender=recipient) & Q(recipient=request.user))
    ).order_by('timestamp')

    return render(request, 'accounts/chat_with.html', {'messages': messages, 'recipient': recipient})

