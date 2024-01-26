from rest_framework.response import Response
from rest_framework.decorators import api_view

#GET 요청이 오면 함수를 호출
@api_view(['GET'])
def hello(request) :
    return Response("Hello REST API")


from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def booksAPI(request):
    if request.method == 'GET':
        books = Book.objects.all()
        #출력하기 위해서 브라우저 형식으로 데이터 변환
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        #클라이언트에서 전송된 데이터를 가지고 Model 인스턴스 생성
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
