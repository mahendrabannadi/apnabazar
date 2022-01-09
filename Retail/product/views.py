from re import A
import re
from django.http import response
from django.shortcuts import redirect, render, HttpResponseRedirect
from rest_framework import serializers,status
from rest_framework.views import APIView
import product
from product.middlewares.auth import auth_middleware
from product.serializers import CategorySerializer, CustomerSerializer,ProductSerializer
from rest_framework.response import Response
from product.models import Customer, Order, Product, Category
from rest_framework.decorators import api_view 
from django.contrib.auth.hashers import make_password, check_password
# from django.utils.decorators import method_decorator

# @api_view(['GET'])
# def hello_world(self):
#     #return Response({'msg':'Hello World'})
#     self.String1 = "Hello"

#Create your views here.
class Products(APIView):
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products = None
        allcategory = Category.objects.all()
        allcategories = CategorySerializer(allcategory, many = True).data
        # print("Category: ",request.GET)
        # print(request.GET.get('category'))
        # products = Product.objects.all()
        # products = ProductSerializer(products, many=True).data

        categoryId = request.GET.get('category')
        if categoryId is not None:
            categoryproduct = Product.objects.filter(category = categoryId)
            products = ProductSerializer(categoryproduct, many=True).data
        else:
            categoryproduct = Product.objects.all()
            products = ProductSerializer(categoryproduct, many = True).data
        data = {}
        data['allproducts'] = products
        data['allcategories']=allcategories
        return render(request,'index.html',data)
        # return render(request,'index.html',{'product':serializer.data})
    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        print(type(product))
        print(type(cart))
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart']=cart
        print('cart', request.session['cart'])
        return redirect('homepage')

    # def get(self , request):
    #     # print()
    #     return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

class Signup(APIView):
    def get(self, request):
        # if request.method == 'GET':
            print(request.method)
            return render(request,'signup.html')
        
    def post(self,request):
        postData = request.POST
        print(request.method)
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        value = {
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email
        }
        #Validation
        #email_value = Customer.objects.filter(email)
        #print(email_value)
        error_message = None
        if(not first_name):
            error_message = "First name required"
        elif len(phone)!=10:
            error_message = "Enter a valid phone number"
        elif(Customer.objects.filter(phone = phone)):
            error_message = "Mobile number already exist"
        elif(not password):
            error_message = "Please enter password"
        elif(not email):
            error_message = "Email is required"
        elif(Customer.objects.filter(email = email)):
            error_message = "Email already exist"
        if not error_message:
            print(first_name,last_name,phone,email,password)
            password = make_password(password)
            print(password)
            Customer_detail = Customer.objects.create(firstname = first_name, lastname = last_name, phone = phone, email = email, password = password)
            return redirect('homepage')
        else:
            data = {
                'error':error_message,
                'values':value
            }
            return render(request, 'signup.html',data)

class Login(APIView):
    return_url = None
    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        print(Login.return_url)
        return render(request,'login.html')

    def post(self,request):
        reqData = request.POST
        user_email = reqData.get('email')
        pass_word = reqData.get('password')
        value = {
            'email':user_email,
            'password':pass_word
        }
        try:
            customer = Customer.objects.get(email = user_email,password = pass_word)
            #customerId = Customer.objects.filter(pk=id)
            request.session['customer'] = customer.id
            # request.session['email'] = customer.email
            # print("Customer :",request.session['customer_id'])
            # print("EMAIL :",request.session['email'])

            if Login.return_url:
                return HttpResponseRedirect(Login.return_url)
            else:
                Login.return_url=None
                return redirect('homepage')            
        except Customer.DoesNotExist:
            error_message = "Incorrect credentials"
            data = {
                'error':error_message,
                'values':value
            }
            return render(request,'login.html',data)

def logout(request):
    request.session.clear()
    return redirect('login')

class Cart(APIView):
   def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )

class CheckOut(APIView):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        
        for product in products:
            order = Order(customer = Customer(id=customer), product = product,price = product.price, quantity = cart.get(str(product.id)),address = address, phone = phone)
            print(order.placeOrder())
            order.save()
            request.session['cart']={}
        return redirect('cart')


class Orders(APIView):
    # @method_decorator(auth_middleware)
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        #orders = orders.reverse()
        return render(request, 'orders.html', {'orders':orders})

    
         






 