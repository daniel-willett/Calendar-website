from django.urls import path

from . import views

urlpatterns = [
    path("", views.calendar_view, name="calendar"),
    path("events/data/", views.calendar_events_view, name="calendar_events"),
    path("events/new/", views.event_create_view, name="event_create"),
    path(
        "events/<int:event_id>/edit/",
        views.event_edit_view,
        name="event_edit",
    ),
    path(
        "events/<int:event_id>/delete/",
        views.event_delete_view,
        name="event_delete",
    ),
]

