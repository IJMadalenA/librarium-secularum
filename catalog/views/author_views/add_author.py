# Imported from Rest-Framework.
from rest_framework import status, generics
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Serializers.
from catalog.serializers.input import AuthorSerializerIn
from catalog.serializers.output import AuthorSerializerOut


class AddAuthorView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        try:
            serializer = AuthorSerializerIn(
                data=request.data,
                context={'request': request}
            )
            serializer.is_valid(raise_exception=True)
            author = serializer.save()

            response = Response(
                AuthorSerializerOut(author).data,
                status=status.HTTP_201_CREATED,
            )
        except ValidationError as e:
            response = Response(
                {'error_code': 'BAD_REQUEST', 'detail': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except PermissionDenied as e:
            response = Response(
                {'error_code': 'UNAUTHORIZED', 'detail': str(e)},
                status=status.HTTP_403_FORBIDDEN
            )
        return response
