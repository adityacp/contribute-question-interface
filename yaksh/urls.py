from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from interface import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.show_home,name="home"),

    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', views.logout_page,name="logout_page"),
    url(r'^register/$', views.register, name="register_page"),
    url(r'^register/success/$', views.register_success,name="register_success"),
    url(r'^dashboard/$',views.next_login,name="next_login"),

    url(r'^questions/$',views.show_questions_stu,name="stu_questions"),
    url(r'^questions/ratemcq/$',views.rate_mcq,name="rate_mcq"),
    url(r'^questions/postcomment/$',views.rate_post,name="rate_post_comment"),
    url(r'^questions/ratecq/$',views.rate_cq,name="rate_cq"),
    url(r'^questions/addmcq/$',views.add_mcquestion,name="add_mcq"),
    url(r'^questions/addcq/$',views.add_cquestion,name="add_cq"),

    url(r'^questions/(?P<id>\d+)/$',views.add_comment,name="question_comment"),
    url(r'^questions/(?P<id>\d+)/postcomment/$',views.post_comment,name="question_comment_post"),

    url(r'^moderator/$',views.next_login,name="mod_show"),
    url(r'^moderator/all/$',views.show_questions_mod_all,name="mod_show_all"),
    url(r'^moderator/mcq/$',views.show_questions_mod_mcq,name="mod_show_mcq"),
    url(r'^moderator/cq/$',views.show_questions_mod_cq,name="mod_show_cq"),
    url(r'^moderator/mcq_approved/$',views.show_questions_mod_approved_mcq,name="mod_show_approved_mcq"),
    url(r'^moderator/cq_approved/$',views.show_questions_mod_approved_cq,name="mod_show_approved_cq"),
    url(r'^moderator/(?P<id>\d+)/$',views.approve_questions,name="mod_questions"),
    url(r'^moderator/(?P<id>\d+)/approve/$',views.approve_questions_accept,name="mod_approve"),
    url(r'^moderator/(?P<id>\d+)/postcomment/$',views.post_comment,name="mod_approve_posted"),
                      
    url(r'^reviews/$',views.show_reviews,name="show_review"),
    url(r'^ratings/$',views.show_ratings,name="show_ratings"),

]
