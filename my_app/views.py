from django.shortcuts import render
from rest_framework.generics import ListAPIView

from my_app.models import Comments
from my_app.serializers import CommentSerializer


# Create your views here.


class CountriesView(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer