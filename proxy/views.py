from django.http import HttpResponse, HttpResponseBadRequest
from uuid import UUID
from proxy.models import User, Inbound
from v2config.sub import links_to_sub


def subscription(request):
    uid = request.GET.get('id', '')
    try:
        uuid = UUID(uid)
        user = User.objects.get(uuid=uuid)
    except (ValueError, User.DoesNotExist):
        return HttpResponseBadRequest("Invalid id")

    links = list()
    for inbound in Inbound.objects.all():
        links.append(inbound.get_link(user))

    return HttpResponse(links_to_sub(links), content_type='text/plain')
