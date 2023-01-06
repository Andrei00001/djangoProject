from datetime import datetime

from django.db.models import Q
from rest_framework import views
from rest_framework.response import Response

from app.api import serializer
from app.api.utils import valid_data, type_data
from app.models import Form


class ProductsView(views.APIView):
    serializer_class = serializer.FormSerializer

    def post(self, request, *args, **kwargs):
        if not request.query_params:
            return Response("Json-No, Query params - Yes")
        data = valid_data(dict(request.query_params))

        query = Form.objects
        if isinstance(data['date'], datetime):
            query = query.filter(date=data['date'])
        query_any = query.filter(Q(phone=data['phone']) | Q(email=data['email']))

        if query_any:
            return Response(query_any.last().name)
        if query:
            return Response(query.last().name)

        data = type_data(data)
        return Response(data)
