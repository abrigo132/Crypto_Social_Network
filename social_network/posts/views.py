from django.forms import model_to_dict
from django.shortcuts import render
from requests import Response
from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Posts


class CreatePost(APIView):
    def post(
        self,
        request,
    ):
        queryset = Posts.objects.create(
            title=request.data["title"], body=request.data["body"]
        )
        return Response({"message": model_to_dict(queryset)})

    def get(self, request):
        return Response({"message": "Метод GET не разрешён"})
