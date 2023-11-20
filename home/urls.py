from django.urls import path
from . import views
from home.dash_apps_conte import l_chart
from home.dash_apps_conte import B_chart
from home.dash_apps_conte import Area_c
from home.dash_apps_conte import D_table
from home.dash_apps_conte import P_chart
from home.dash_apps_conte import Dash_Board
from home.dash_app_country import Bub_chart
from home.dash_app_country import Line_chart
from home.dash_app_country import Data_table
from home.dash_app_country import Scat_plot
from home.dash_app_country import Pie_chart

urlpatterns = [
    path('',views.home, name='home'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('country/',views.country, name='country'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]