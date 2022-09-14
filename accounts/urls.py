from django.urls import path


from .views import SignUpView, AccountView


urlpatterns = [
    path('', AccountView.as_view()),
    path('signup/', SignUpView.as_view(), name='signup'),
]
