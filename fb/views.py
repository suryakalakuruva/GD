from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment,Friend
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import generics
from .serializers import PostSerializer,CommentSerializer

# Create your views here.


# To display all posts  
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


# View for start page

def start(request):
	return render(request,'fb/start.html',{})


# View for crreating new post

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



# View to add comment to post

def create_comment(request,pk):
	post = get_object_or_404(Post,pk=pk)
	me = request.user

	if request.method == "POST":
		commenttext = request.POST.get('comment')
		if (commenttext != ""):
			comment = Comment.objects.create(author=me,post=post,text=commenttext)

		return redirect('post_list')


# View to add friends 
def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('post_list')	


# View for REST api to display all posts in JSON
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# View for REST api to display particular post details
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# View for REST api to  display  all comments 
class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# View for REST api to display particular comment details
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

