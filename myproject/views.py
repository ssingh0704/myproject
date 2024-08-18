from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    # Some view logic to fetch data or perform operations
    context = {
        'variable1': 'value1',
        'variable2': 'value2',
    }
    # Render the template 'my_template.html' with the context data
    return HttpResponse("welcome to my world")


def user_input(request):
    temp = "template/form.html"
    context = {
        'variable1': 'value1',
        'variable2': 'value2',
    }
    if request.method =="POST":
        import ipdb;ipdb.set_trace()
        data = request.POST.dict()
        insert(data)
        return HttpResponse("submit sucessfull")

    # Render the template 'my_template.html' with the context data
    return render(request, temp, context)



import boto3

def insert(data):
    import boto
    table_name = 'login_data'

    # Define the data to be inserted
    item = {
        'username': {'S': data.get('username')},
        'password': {'S': data.get('password')},  # Assuming 'password' is a string attribute
        # Add more attributes as needed
    }
    # import ipdb;ipdb.set_trace()
    # Key = {'username': {'S': data.get('username')}}

    # response = dynamodb.get_item(
    #     TableName=table_name,
    #     Key=Key)
    # Insert the item into the table
    response = dynamodb.put_item(
        TableName=table_name,
        Item=item
    )

    print("Data inserted successfully:", response)
data =  {'username': 'mickykumar725@gmail.com', 'password': 'micky'}
from myproject.views import *
insert(data)