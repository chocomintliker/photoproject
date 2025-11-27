from django.urls import path
from . import views

app_name = 'gameblogapp'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),

    path('blog-detail/<int:pk>/',
         views.GameBlogDetail.as_view(),name='gameblog_detail'),

    path('rule-list/',views.RuleView.as_view(),name='rule_list'),

    path('tips-list/',views.TipsView.as_view(),name='tips_list'),

    path('other-list/',views.OtherView.as_view(),name='other_list'),

    path('contact/',views.ContactView.as_view(),name='contact'),

    path('post/',views.CreatePostView.as_view(),name='post'),

    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
]