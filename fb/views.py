from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment,Friend
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def post_list(request):
	posts_list = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
	page = request.GET.get('page', 1)
	paginator = Paginator(posts_list, 5)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)


	# import ipdb;
	# ipdb.set_trace();

	users = User.objects.exclude(id=request.user.id)
	friend = Friend.objects.get(current_user=request.user)
	friends = friend.users.all()
	
	return render(request, 'fb/post_list.html', {'posts': posts,'users':users,'friends':friends})




def start(request):
	return render(request,'fb/start.html',{})



def create_post(request):
	me=request.user
	if request.method == 'POST':
		posttext = request.POST.get('post')
		postimage=request.FILES.get('myfile')
		if (posttext != ""):
			post = Post.objects.create(author=me,title=posttext,post_pics=postimage)

		# if (postdetail != ""):
		# 	post = Post.objects.create(author=me,title=postdetail,post_pics=post_image)
		# post =Post.objects.create(author=me,title=postdetail)
		return redirect('post_list')


# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":

#         form = CommentForm(request.POST)
#         if form.is_valid():

#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.post = post
#             comment.save()
#             return redirect('post_list')
#     else:
#         form = CommentForm()
#     return render(request, 'fb/add_comment_to_post.html', {'form': form})




def create_comment(request,pk):
	post = get_object_or_404(Post,pk=pk)
	me = request.user

	if request.method == "POST":
		commenttext = request.POST.get('comment')
		if (commenttext != ""):
			comment = Comment.objects.create(author=me,post=post,text=commenttext)

		return redirect('post_list')


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('post_list')	


