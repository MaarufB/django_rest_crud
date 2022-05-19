from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from  rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):

    # Get all the drinks
    # serialize them
    # return json
    if request.method == 'GET':

        # This part here will fetch the data from the database
        drinks = Drink.objects.all()

        # This will serialized the data
        serializer = DrinkSerializer(drinks, many=True)
        # We will put the serialized data to the dictionary
        context = {
            "drinks": serializer.data
        }

        print(f"GET: {drinks}")
        
        return JsonResponse(context)

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)

        if serializer.is_valid():
            print(f"POST DATA: {request.data}")
            # print(f"REQUEST: {request.status}")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):
    
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)        
    
    if request.method == 'GET':
        # Get request
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # PUT request
        # We will update the data
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid(): # is_valid() will return a boolean value
            serializer.save()
            print(f"Data is Updated!")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # DELETE Method
        # serializer = DrinkSerializer(drink, data=request.data)
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

