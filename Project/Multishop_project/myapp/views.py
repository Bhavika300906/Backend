from django.shortcuts import render,redirect
from .models import User,Product,Wishlist,Cart
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import random
import requests
import json
import stripe

YOUR_DOMAIN = 'http://localhost:8000'
stripe.api_key = settings.STRIPE_PRIVATE_KEY
# Create your views here.
def get_logged_in_user(request):
    try:
        return User.objects.get(email=request.session['email'])
    except:
        return None

def is_seller(user):
    return user and user.usertype.strip().lower()=="seller"

def is_buyer(user):
    return user and user.usertype.strip().lower()=="buyer"

def set_login_session(request,user):
    request.session['email']=user.email
    request.session['fname']=user.fname
    request.session['profile_picture']=user.profile_picture.url
    request.session['usertype']=user.usertype.strip().lower()

def seller_required(request):
    user=get_logged_in_user(request)
    if user==None:
        return None,redirect('login')
    if not is_seller(user):
        return None,redirect('index')
    return user,None

def index(request):
    user=get_logged_in_user(request)
    if is_seller(user):
        return render(request,'seller-index.html')
    return render(request,'index.html')

def shop(request):
    products=Product.objects.all()
    return render(request,'shop.html',{'products':products})

def contact(request):
    return render(request,'contact.html')

def signup(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            msg="Email Already Exist"
            return render(request,'signup.html',{'msg':msg}) 
        except User.DoesNotExist:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                    profile_picture=request.FILES.get('profile_picture'),
                    usertype=request.POST['usertype']
                )
                msg="User Sign Up Successfully"
                return render(request,'login.html',{'msg':msg})
            else:
                msg="Password & Confirm Password doesn't matched"
                return render(request,'signup.html',{'msg':msg})
        
    else:
        return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session.flush()
                set_login_session(request,user)
                if is_buyer(user):
                    wishlists=Wishlist.objects.filter(user=user)
                    request.session['wishlist_count']=len(wishlists)
                    carts=Cart.objects.filter(user=user,payment_status=False)
                    request.session['cart_count']=len(carts)
                    return render (request,'index.html')
                else:
                    return render (request,'seller-index.html')                   
            else:
                msg="Incorrect Password"
                return render (request,'login.html',{'msg':msg})
        except User.DoesNotExist:
            msg="Email Not Registered"
            return render (request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')

def logout(request):
    request.session.flush()
    msg="User Logged Out Successfully"
    return render (request,'login.html',{'msg':msg})

def profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.address=request.POST['address']
        if request.FILES.get('profile_picture'):
            user.profile_picture=request.FILES['profile_picture']
        user.save()
        msg="Successfully Profile Updated"
        request.session['profile_picture']= user.profile_picture.url
        if is_buyer(user):
            return render(request,'profile.html',{'user':user,'msg':msg})
        else:
             return render(request,'seller-profile.html',{'user':user,'msg':msg})
    else:
        if is_buyer(user):
            return render(request,'profile.html',{'user':user})
        else:
             return render(request,'seller-profile.html',{'user':user})
        

def change_password(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        if user.password==request.POST['old_password']:
            if request.POST['new_password']==request.POST['cnew_password']:
                if user.password!=request.POST['new_password']:
                    user.password=request.POST['new_password']
                    user.save()
                    del request.session['email']
                    del request.session['fname']
                    del request.session['profile_picture']
                    msg="Password Changed Successfully"
                    return render (request,'login.html',{'msg':msg})
                else:
                    msg="Your New Password can't be from old password"
                    if is_buyer(user):
                        return render(request,'change-password.html',{'msg':msg})
                    else:
                        return render(request,'seller-change-password.html',{'msg':msg})
                   
            else:
                msg="Your New Password & Confirm New Password doesn't matched"
                if is_buyer(user):
                    return render(request,'change-password.html',{'msg':msg})
                else:
                    return render(request,'seller-change-password.html',{'msg':msg})
        else:
            msg="Your Old Password Doesn't Matched"
            if is_buyer(user):
                return render(request,'change-password.html',{'msg':msg})
            else:
                return render(request,'seller-change-password.html',{'msg':msg})

    else:
        if is_buyer(user):
             return render(request,'change-password.html')
        else:
            return render(request,'seller-change-password.html')

def forget_password(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            otp=random.randint(1000,9999)
            subject="OTP verification for Django Major Project"
            message="Your OTP for forgot password is "+str(otp)
            fr=settings.EMAIL_HOST_USER
            to=[user.email,]
            send_mail(subject,message,fr,to)
            request.session['otp']=otp
            request.session['email_to']=user.email
            return render (request,'otp-verify.html')
        
        except:
            msg="Your email is not Register with use. Please Try with Register Email ! "
            return render(request,'forget-password.html',{'msg':msg})
    
    else:
        return render(request,'forget-password.html')

def otp_verify(request):
    if request.method=="POST":
        otp1=int(request.session['otp'])
        otp2=int(request.POST['otp'])
        if otp1==otp2:
            del request.session['otp']
            return render(request,'new-password.html')
        else:
            msg='Invalid OTP. Please Try Again!'
            return render(request,'otp-verify.html',{'msg':msg})
    else:
        return render(request,'otp-verify.html')

def new_password(request):
    user=User.objects.get(email=request.session['email_to'])
    if request.POST['new_password']==request.POST['cnew_password']:
        if user.password!=request.POST['new_password']:
                    user.password=request.POST['new_password']
                    user.save()
                    msg="New Password updated successfully"
                    del request.session['email_to']
                    msg="Password Changed Successfully"
                    return render(request,'login.html',{'msg':msg})
        else:
            msg="New Password & Old Password Can't be same "
            return render(request,'new-password.html',{'msg':msg})
    else:
        msg="Your New Password & Confirm New Password doesn't matched"
        return render(request,'new-password.html',{'msg':msg})

def seller_add_product(request):
    seller,response=seller_required(request)
    if response:
        return response
    if request.method=="POST":
        Product.objects.create(
            seller=seller,
            product_category=request.POST['product_category'],
            product_name =request.POST['product_name'],
            product_price=request.POST['product_price'],
            product_decs=request.POST['product_decs'],
            product_image =request.FILES['product_image'],
        )
        msg="Product Added Successfully"
        return render(request,'seller-add-product.html',{'msg':msg})
    else:
        return render(request,'seller-add-product.html')

def seller_view_product(request):
    seller,response=seller_required(request)
    if response:
        return response
    products=Product.objects.filter(seller=seller)
    return render(request,'seller-view-product.html',{'products':products})

def seller_product_details(request,pk):
    seller,response=seller_required(request)
    if response:
        return response
    try:
        product=Product.objects.get(pk=pk,seller=seller)
    except Product.DoesNotExist:
        return redirect('seller-view-product')
    return render(request,'seller-product-details.html',{'product':product})

def seller_product_edit(request,pk):
    seller,response=seller_required(request)
    if response:
        return response
    try:
        product=Product.objects.get(pk=pk,seller=seller)
    except Product.DoesNotExist:
        return redirect('seller-view-product')
    if request.method=="POST":
        product.product_category=request.POST['product_category']
        product.product_name=request.POST['product_name']
        product.product_price=request.POST['product_price']
        product.product_decs=request.POST['product_decs']
        try:
            product.product_image=request.FILES['product_image']
        except:
            pass
        product.save()
        msg="Product Updated Successfully"
        return render(request,'seller-product-edit.html',{'product':product,'msg':msg})
    else:
        return render(request,'seller-product-edit.html',{'product':product})

def seller_product_delete(request,pk):
    seller,response=seller_required(request)
    if response:
        return response
    try:
        product=Product.objects.get(pk=pk,seller=seller)
    except Product.DoesNotExist:
        return redirect('seller-view-product')
    product.delete()
    return redirect('seller-view-product')

def product_details(request,pk):
    wishlist_flag=False
    cart_flag=False
    product=Product.objects.get(pk=pk) 
    user=User.objects.get(email=request.session['email'])
    try:
        Wishlist.objects.get(user=user,product=product)
        wishlist_flag=True
    except:
        pass
    try:
        Cart.objects.get(user=user,product=product,payment_status=False)
        cart_flag=True
    except:
        pass
    return render(request,'product-details.html',{'product':product,'wishlist_flag':wishlist_flag,'cart_flag': cart_flag})

def category(request,cat):
    products=Product()
    if cat=="all":
        products=Product.objects.all()
    else:
        products=Product.objects.filter(product_category=cat)
    return render(request,'shop.html',{'products':products})

def add_to_wishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Wishlist.objects.get_or_create(user=user,product=product)
    return redirect('wishlist')

def wishlist(request):
    user=User.objects.get(email=request.session['email'])
    wishlists=Wishlist.objects.filter(user=user)
    request.session['wishlist_count']=len(wishlists)
    return render(request,'wishlist.html',{'wishlist':wishlists})

def remove_from_wishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Wishlist.objects.filter(user=user,product=product).delete()
    return redirect('wishlist')

def add_to_cart(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Cart.objects.get_or_create(user=user,product=product,payment_status=False,defaults={
        'product_price':product.product_price,
        'product_qty':1,
        'total_price':product.product_price,
    })
    return redirect('cart')

def cart(request):
    net_price=0
    user=User.objects.get(email=request.session['email'])
    carts=Cart.objects.filter(user=user,payment_status=False)
    for i in carts:
        net_price=net_price+i.total_price
    request.session['cart_count']=len(carts)
    return render(request,'cart.html',{'carts':carts,'net_price':net_price})

def remove_from_cart(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    cart=Cart.objects.filter(user=user,product=product,payment_status=False)
    cart.delete()
    return redirect('cart')

def change_qty(request,pk):
    cart=Cart.objects.get(pk=pk)
    product_qty=int(request.POST['product_qty'])
    cart.product_qty=int(request.POST['product_qty'])
    cart.total_price=cart.product_price*product_qty
    cart.save()
    return redirect('cart')

#stripe

@csrf_exempt
def create_checkout_session(request):
	amount = int(json.load(request)['post_data'])
	final_amount=amount*100
	user=User.objects.get(email=request.session['email'])
	user_name=f"{user.fname} {user.lname}"
	user_address=f"{user.address}"
	user_mobile=f"{user.mobile}"
	session = stripe.checkout.Session.create(
		payment_method_types=['card'],
		line_items=[{
			'price_data': {
				'currency': 'inr',
				'unit_amount': final_amount,
				'product_data': {
					'name': 'Checkout Session Data',
					'description':f'''Customer:{user_name},\n\n
					Address:{user_address},\n
					Mobile:{user_mobile}''',
				},
			},
			'quantity': 1,
			}],
		mode='payment',
		success_url=YOUR_DOMAIN + '/success.html',
		cancel_url=YOUR_DOMAIN + '/cancel.html',
		customer_email=user.email,
		shipping_address_collection={
			'allowed_countries':['IN'],
		}
		)
	return JsonResponse({'id': session.id})

def success(request):
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment_status=False)
	for i in carts:
		i.payment_status=True
		i.save()
	carts=Cart.objects.filter(user=user,payment_status=False)
	request.session['cart_count']=len(carts)
	return render(request,'success.html')

def cancel(request):
	return render(request,'cancel.html')

def myorder(request):
    user=User.objects.get(email=request.session['email'])
    orders=Cart.objects.filter(user=user,payment_status=True)
    return render(request,'myorder.html',{'orders':orders})
