# Django imported.
from django.core.exceptions import (
    BadRequest,
    ObjectDoesNotExist,
)
# Rest-Framework imported.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import (
    ValidationError,
    PermissionDenied,
    NotAuthenticated,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
)
# Models imported.
from catalog.models.author import Author


class DestroyAuthorView(APIView):
    """
    View to delete one Author in the system.

    * Require token authentication.
    *
    """

    permission_classes = (
        IsAuthenticated
    )

    def delete(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            author_to_delete_id = int(kwargs.get("pk", None))

            delete_book = Author.objects.get(id=author_to_delete_id)
            delete_book.delete()

            response = Response(
                status=HTTP_200_OK,
            )

        except Author.DoesNotExist as e:
            response = Response(
                {
                    "error_code": "ELEMENT_NOT_FOUND",
                    "detail": str(e),
                },
                status=HTTP_404_NOT_FOUND,
            )
        except ObjectDoesNotExist as e:
            response = Response(
                {
                    "error_code": "ELEMENT_NOT_FOUND",
                    "detail": str(e),
                },
            )
        except BadRequest as e:
            response = Response(
                {
                    "error_code": "BAD_REQUEST",
                    "detail": str(e),
                },
                status=HTTP_400_BAD_REQUEST,
            )
        except ValidationError as e:
            response = Response(
                {
                    "error_code": "UNAUTHORIZED",
                    "detail": str(e),
                },
                status=HTTP_401_UNAUTHORIZED,
            )
        except NotAuthenticated as e:
            response = Response(
                {
                    "error_code": "UNAUTHORIZED",
                    "detail": str(e),
                },
                status=HTTP_401_UNAUTHORIZED,
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
