from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import PostModel, CategoryModel, StarModel, CommentModel
from .bot import send_news
from .forms import AddCommentFormUsername, AddCommentForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


def home_view(request):
    """
    Render the home view.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered home view as an HTTP response.
    """
    post = PostModel.objects.all().order_by('-id')
    name = ''
    categories = CategoryModel.objects.all()
    context = {
        'post': post,
        'categories': categories,
        'name': name
    }

    return render(request, 'nv/home.html', context)


def cotegories_view(request, pk):
    """
    Render and return the 'home.html' template with the appropriate context.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the category.

    Returns:
        HttpResponse: The rendered 'home.html' template with the context.
    """
    post = PostModel.objects.filter(category=pk)
    categories = CategoryModel.objects.all()
    cat = CategoryModel.objects.get(id=pk)
    name = 'cat'
    context = {
        'post': post,
        'categories': categories,
        'name': name,
        'cat': cat,
    }

    return render(request, 'nv/home.html', context)


def article_detail(request, pk):
    """
    Retrieves the details of an article.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the article to retrieve.

    Returns:
        HttpResponse: The HTTP response object containing the rendered article page.

    Raises:
        PostModel.DoesNotExist: If no post with the given primary key exists.
    """
    post = PostModel.objects.get(id=pk)
    categories = CategoryModel.objects.all()
    star = StarModel.objects.filter(post=pk)
    count = 0
    ball = 0
    for i in star:
        count += 1
        ball += i.num_star
    
    rating = 0
    if count == 0:
         rating = 0
    else:
        rating = round(ball / count)
    
    comment = CommentModel.objects.filter(post=pk)
    
    
    context = {
        'post': post,
        'categories': categories,
        'count': count,
        'ball': ball,
        'comment': comment,
        'rating': rating,
    }

    return render(request, 'nv/article.html', context)


def add_star(request, id_post, id_user, ball):
    """
    Updates the number of stars for a post.

    Parameters:
        - request: The HTTP request object.
        - id_post: The ID of the post to update.
        - id_user: The ID of the user who is updating the post.
        - ball: The new number of stars for the post.

    Returns:
        - A redirect to the 'article' view, displaying the updated post.
    """
    ball = int(ball)
    post = PostModel.objects.get(id=id_post)
    user = User.objects.get(id=id_user)
    if StarModel.objects.filter(post=post, username=user).exists():
        star = StarModel.objects.get(post=post, username=user)
        star.num_star = ball
        star.save()
    else:
        star = StarModel.objects.create(post=post, username=user, num_star=ball)
        star.save()
        
    return redirect('article', pk=post.id)



def comment_view(request, id_post, id_user):
    """
    Creates a comment for a post with the given post ID and user ID.

    Parameters:
        - request: The HTTP request object.
        - id_post: The ID of the post to add the comment to.
        - id_user: The ID of the user adding the comment.

    Returns:
        - A redirect to the 'article' page for the post if the comment is successfully created.
        - Otherwise, renders the 'add_comment_username.html' template with the 'AddCommentFormUsername' form and the 'PostModel' object.

    Raises:
        - PostModel.DoesNotExist: If the post with the given ID does not exist.
        - User.DoesNotExist: If the user with the given ID does not exist.
    """
    post = PostModel.objects.get(id=id_post)
    if request.method == 'POST':
        form = AddCommentFormUsername(request.POST)
        if form.is_valid():
            username = User.objects.get(id=id_user).username
            content = form.cleaned_data['content']
            comment = CommentModel.objects.create(post=post, username=username, content=content)
            comment.save()
            return redirect('article', pk=post.id)
    else:
        form = AddCommentFormUsername()
    post = PostModel.objects.get(id=id_post)
    return render(request, 'nv/add_comment_username.html', {'form': form, 'post': post})


class AddComment(CreateView):
    model = CommentModel
    form_class = AddCommentForm
    template_name = 'nv/add_comment.html'
        
    def form_valid(self, form):
        """
        Sets the post_id attribute of the form instance to the value specified in the `id_post` key of `self.kwargs`.

        Parameters:
            form (Form): The form instance to be validated.

        Returns:
            HttpResponse: The result of calling the `form_valid` method of the parent class with the validated form.
        """
        form.instance.post_id = self.kwargs['id_post']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Retrieves the context data for the view.

        Parameters:
            **kwargs (dict): Arbitrary keyword arguments.

        Returns:
            dict: The context data for the view.
        """
        context = super().get_context_data(**kwargs)
        context["post"] = PostModel.objects.get(id=self.kwargs['id_post'])
        return context
    
        
    success_url = reverse_lazy('home')
    