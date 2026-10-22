from .decorators import approved_user_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Event
from .forms import EventForm

# Create your views here.
@approved_user_required
def calendar(request):
    return render(request, "events/calendar.html")

@approved_user_required
def calendar_view(request):
    events = Event.objects.order_by("start_time")

    return render(
        request,
        "events/calendar.html",
        {"events": events},
    )

@approved_user_required
def event_create_view(request):
    if request.method == "POST":
        form = EventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()

            return redirect("calendar")
    else:
        form = EventForm()

    return render(
        request,
        "events/event_form.html",
        {"form": form},
    )

@approved_user_required
def event_edit_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method=="POST":
        form = EventForm(request.POST, instance=event)

        if form.isValid():
            form.save()
            return redirect("calendar")
    else:
        form = EventForm(instance=event)

    return render(
            request,
            "events/event_form.html",
            {"form": form, "event":event},
    )


@approved_user_required
def event_delete_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method=="POST":
        event.delete()
        return redirect("calendar")

    return render(
            request,
            "events/event_confirm_delete.html",
            {"event":event},
    )

