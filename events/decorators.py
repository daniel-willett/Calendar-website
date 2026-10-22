
from functools import wraps

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


APPROVED_USERNAMES = {"danielw", "Kt"}


def approved_user_required(view_func):
    @wraps(view_func)
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.username not in APPROVED_USERNAMES:
            return HttpResponseForbidden(
                "You do not have permission to access this calendar."
            )

        return view_func(request, *args, **kwargs)

    return wrapper

