import json

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from apps.property_management.forms import UploadJsonForm
from apps.property_management.utils import extract_info_from_json


@method_decorator(csrf_exempt, name='dispatch')
class UploadJsonView(View):

    def post(self, request, *args, **kwargs):
        form = UploadJsonForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                content = json.load(request.FILES['file'])
                data = extract_info_from_json(content)
                return JsonResponse(data)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON file'}, status=400)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
