

from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.index, name='index'),

    # topics
    path('topics/', views.topics, name='topics'),

    # individual topic
    path('topics/<int:topic_id>/', views.topic, name="topic"),

    # newtopic
    path('new_topic', views.new_topic, name="new_topic"),

    # new_entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
