from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView

from .models import GameBlogPost

from django.views.generic import FormView

from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

from .forms import ContactForm

from django.contrib import messages

from django.core.mail import EmailMessage

from .forms import GamePostForm

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

class IndexView(ListView):
    template_name ='index.html'
    context_object_name = 'orderby_records'
    queryset = GameBlogPost.objects.order_by('-posted_at')
    paginate_by = 6


class GameBlogDetail(DetailView):
    template_name='post.html'
    model = GameBlogPost

class RuleView(ListView):
    template_name = 'rule_list.html'
    model = GameBlogPost
    context_object_name = 'rule_records'
    queryset = GameBlogPost.objects.filter(category='rule').order_by('-posted_at')
    paginate_by = 3

class TipsView(ListView):
    template_name = 'tips_list.html'
    model = GameBlogPost
    context_object_name = 'tips_records'
    queryset = GameBlogPost.objects.filter(category='tips').order_by('-posted_at')
    paginate_by = 3

class OtherView(ListView):
    template_name = 'other_list.html'
    model = GameBlogPost
    context_object_name = 'other_records'
    queryset = GameBlogPost.objects.filter(category='other').order_by('-posted_at')
    paginate_by = 3

class ContactView(FormView):
    template_name='contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('gameblogapp:contact')
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)

        message = '送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:{3}'.format(name,email,title,message)

        from_email = 'utm2577203@stu.o-hara.ac.jp'

        to_list = [email]

        message = EmailMessage(subject = subject,
                               body=message,
                               from_email = from_email,
                               to = to_list,
                               )
        
        message.send()
        messages.success(
            self.request,'お問い合わせは正常に送信されました'
        )

        return super().form_valid(form)
    
@method_decorator(login_required,name='dispatch')
class CreatePostView(CreateView):
    form_class = GamePostForm
    template_name = 'post_game.html'
    success_url = reverse_lazy('gameblogapp:post_done')
    def form_valid(self,form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
    
class PostSuccessView(TemplateView):
    template_name = 'post_success.html'
    