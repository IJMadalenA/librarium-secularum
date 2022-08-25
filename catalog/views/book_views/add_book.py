# Django imported.
from django.core.exceptions import FieldError
# Rest-Framework imported.
from rest_framework.views import APIView
from rest_framework.exceptions import (
    ValidationError,
    PermissionDenied,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)
from rest_framework.response import Response

# Serializers imported.
from catalog.serializers.input.book_serializer_in import BookSerializerIn
from catalog.serializers.output.book_serializer_out import BookSerializerOut

import logging
logger = logging.getLogger(__name__)


class PostBookView(APIView):
    """

    """
    permission_classes = (
        IsAuthenticated,
    )

    def post(self, request):
        try:
            serializer = BookSerializerIn(
                data=request.data,
                context={
                    "request": request
                }
            )
            serializer.is_valid(raise_exception=True)
            new_book = serializer.save()

            response = Response(
                BookSerializerOut(new_book).data,
                status=HTTP_201_CREATED,
            )
        except ValidationError as e:
            response = Response(
                {
                    "error_code": "BAD_REQUEST",
                    "detail": str(e),
                },
                status=HTTP_400_BAD_REQUEST,
            )
        except FieldError as e:
            response = Response(
                {
                    "error_code": "FIELD_ERROR",
                    "detail": str(e),
                },
                status=HTTP_400_BAD_REQUEST,
            )
        except PermissionDenied as e:
            response = Response(
                {
                    "error_code": "UNAUTHORIZED",
                    "detail": str(e),
                },
                status=HTTP_401_UNAUTHORIZED,
            )

        return response
