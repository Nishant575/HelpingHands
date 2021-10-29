from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView
from django.http import HttpResponse
from .models import Transaction
from .forms import Transform
from django.contrib import messages
from hh.models import Post
from users.models import Profile


def transfer(request,pk):
    if request.method == 'POST':
        amt = request.POST.get('amt')
        user1 = request.user
        post = Post.objects.filter(id=pk).first()
        user2 = User.objects.filter(username=post.author).first()
        if int(amt) <= user1.profile.funds:
            user1.profile.funds -= int(amt)
            user1.profile.save()
            user2.profile.funds += int(amt)
            user2.profile.save()
            post.curr_amt += int(amt)
            post.save()
            trans = Transaction(sender=user1.username, receiver=user2.username, amount=int(amt), event=post)
            trans.save()
            messages.success(request, f'Funds transferred!')
            return redirect('hh-home')
        else:
            messages.warning(request, f'Insufficient Funds!!')
            return redirect('hh-home')
  
    return render(request, 'fundtrans/donate.html')


class TransListView(ListView):
    model = Transaction
    context_object_name = 'trans'
    ordering = ['-date']        

