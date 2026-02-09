from rest_framework import viewsets
from .models import Comments
from .serializers import CommentsSerializer
from rest_framework.permissions import IsAuthenticated

class CommentsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer