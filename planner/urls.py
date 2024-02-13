from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token
#need to be able to upload images
from django.conf.urls.static import static
from django.conf import settings

from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    #path("createTrip", views.createTrip, name="createTrip"),
    path("saveTrip", views.saveTrip, name="saveTrip"),
    path("createPost", views.createPost, name="createPost"),
    path("submitPost", views.submitPost, name="submitPost"),
    path("blogs", views.blogs, name="blogs"),
    path("<str:userName>/userProfile", views.userProfile, name="userProfile"),
    path('<str:userName>/editProfile', views.editProfile, name='editProfile'),
    path("<int:blog_id>/readBlog", views.readBlog, name="readBlog"),
    path("planner/<int:postID>/likePost", views.likePost, name="likePost"),
    path("<int:postID>/aframe", views.aframe, name="aframe"),
    path("<int:postID>/comment_detail", views.comment_detail, name="comments"),
    path("<int:blog_id>/editBlogg", views.editBlog, name="editBlog"),
    path("<int:blog_id>/deleteBlog", views.deleteBlog, name="deleteBlog"),
    path("search", views.search, name="search"),
    #path("<str:userName>/editProfile", views.editProfile, name="editProfile"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)