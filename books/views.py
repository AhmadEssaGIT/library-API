from django.shortcuts import render
from .models import Book, borrow
from .serializers import BookSerializer, BorrowSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from .serializers import RegisterSerializer
from rest_framework import generics

@api_view(['POST'])
@permission_classes([])
def create_auth(request):
    if request.method == "POST":    	
 	   serializer = RegisterSerializer(data=request.data)
 	   if serializer.is_valid():
 	   	serializer.validate(attrs=request.data)
 	   	user = serializer.create(validated_data=request.data)
 	   	
 	   	return Response(serializer.data, status=status.HTTP_201_CREATED)
 	   	
 	   else:	   	
 	   	return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


#class RegisterView(generics.CreateAPIView):
#    queryset = User.objects.all()
#    permission_classes = (AllowAny,)
#    serializer_class = RegisterSerializer
    
# Create your views here.
@api_view(['GET', 'POST'])	
@permission_classes([IsAuthenticated])
def list_books(request):

	if request.method == 'GET':
	       books = Book.objects.all()
	       serializer = BookSerializer(books, many=True)
	       return Response(serializer.data)
	       
	if request.method == 'POST':
	       serializer = BookSerializer(data=request.data)
	       if serializer.is_valid():
	           serializer.save()
	           return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, id, format=None):

    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

@api_view(['GET', 'POST'])
def borrow_book(request):
	      
	if request.method == 'GET':
	       borrows =  borrow.objects.all()
	       serializer = BorrowSerializer(borrows, many=True)
	       return Response(serializer.data)
	       
	if request.method == 'POST':
	       serializer = BorrowSerializer(data=request.data)
	       if serializer.is_valid():
	           serializer.save()
	           return Response(serializer.data, status=status.HTTP_201_CREATED)
	                         	 
@api_view(['GET', 'PUT', 'DELETE'])
def user_books(request, id, format=None):

    try:
        user = User.objects.get(pk=id)
        borrow_books = user.customer.all()
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BorrowSerializer(borrow_books, many=True)
        return Response(serializer.data)

    #elif request.method == 'PUT':
#        serializer = BookSerializer(book, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    elif request.method == 'DELETE':
#        book.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
#        
        	                    	                    
        	                    	                            	                    	                            	                    	                    
