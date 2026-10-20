from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q,Count
from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .forms import SignUpForm,ProfileForm,PostForm,CommentForm
from .models import Post,Follow,Like
def signup(request):
    form=SignUpForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        u=form.save(); login(request,u); return redirect("feed")
    return render(request,"social/signup.html",{"form":form})
@login_required
def feed(request):
    ids=Follow.objects.filter(follower=request.user).values_list("following_id",flat=True)
    posts=Post.objects.filter(Q(author=request.user)|Q(author_id__in=ids)).select_related("author","author__profile").prefetch_related("comments__author","likes")
    suggestions=User.objects.exclude(id=request.user.id).exclude(id__in=ids)[:5]
    return render(request,"social/feed.html",{"posts":posts,"suggestions":suggestions})
@login_required
def explore(request):
    q=request.GET.get("q","").strip()
    posts=Post.objects.select_related("author").annotate(like_count=Count("likes"))
    people=User.objects.exclude(id=request.user.id)
    if q: posts=posts.filter(Q(caption__icontains=q)|Q(author__username__icontains=q)); people=people.filter(Q(username__icontains=q)|Q(profile__bio__icontains=q))
    return render(request,"social/explore.html",{"posts":posts[:36],"people":people[:12],"query":q})
@login_required
def create_post(request):
    form=PostForm(request.POST or None,request.FILES or None)
    if request.method=="POST" and form.is_valid():
        p=form.save(commit=False); p.author=request.user; p.save(); messages.success(request,"Your moment is live!"); return redirect("feed")
    return render(request,"social/create_post.html",{"form":form})
@login_required
@require_POST
def like(request,post_id):
    p=get_object_or_404(Post,id=post_id); obj,created=Like.objects.get_or_create(post=p,user=request.user)
    if not created: obj.delete()
    return redirect(request.POST.get("next") or "feed")
@login_required
@require_POST
def comment(request,post_id):
    p=get_object_or_404(Post,id=post_id); f=CommentForm(request.POST)
    if f.is_valid():
        c=f.save(commit=False); c.post=p; c.author=request.user; c.save()
    return redirect(request.POST.get("next") or "feed")
@login_required
def profile(request,username):
    person=get_object_or_404(User.objects.select_related("profile"),username=username)
    return render(request,"social/profile.html",{"person":person,"posts":person.posts.all(),"following":Follow.objects.filter(follower=request.user,following=person).exists(),"followers":person.follower_links.count(),"following_count":person.following_links.count()})
@login_required
def edit_profile(request,username):
    if request.user.username!=username: return redirect("profile",username=username)
    f=ProfileForm(request.POST or None,request.FILES or None,instance=request.user.profile)
    if request.method=="POST" and f.is_valid(): f.save(); messages.success(request,"Profile saved."); return redirect("profile",username=username)
    return render(request,"social/edit_profile.html",{"form":f})
@login_required
@require_POST
def follow(request,username):
    person=get_object_or_404(User,username=username)
    if person!=request.user:
        rel,created=Follow.objects.get_or_create(follower=request.user,following=person)
        if not created: rel.delete()
    return redirect("profile",username=username)
