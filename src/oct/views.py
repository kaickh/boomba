from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET"], permission_classes=[AllowAny])
def oct_info(request):
    """OCT platform info - West Africa OCR extension. Public endpoint."""
    return Response(
        {
            "name": "OCT",
            "tagline": "Premier OCR platform for West Africa",
            "foundation": "Paperless-ngx",
            "stakeholders": ["banking", "politics", "fine_arts"],
        }
    )
