# Create your views here.
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

appName = 'dataaggregator'


@require_http_methods(["POST"])
@csrf_exempt
def aggregate_data(request):

    data = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    return HttpResponse(json.dumps(data), content_type="application/json")









