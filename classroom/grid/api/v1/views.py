from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from classroom.grid.models import Grid
from .serializers import GridSerializer


class GridList(APIView):
    """
    List all Grid, or create a new grid.
    """

    def get(self, request, format=None):
        grids = Grid.objects.all()
        serializer = GridSerializer(grids, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GridSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GridDetail(APIView):
    """
    Retrieve, update or delete a grid instance.
    """

    def get_object(self, pk):
        try:
            return Grid.objects.get(pk=pk)
        except Grid.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        grid = self.get_object(pk)
        serializer = GridSerializer(grid)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        grid = self.get_object(pk)
        serializer = GridSerializer(grid, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        grid = self.get_object(pk)
        grid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)