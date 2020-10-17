# payment_gateway_using_django
Here User Can Do online payment using paytm created with django

#Setup :
1) Create a folder and put all the files inside it.
2) Create a virtual environment - virtualenv env
3) Activate VirtualENV - ubuntu: source env/bin/activate
4) Run requirements.txt pip install r requirements.txt
5) Run the Application - python manage.py runserver
6) Migrate

#Notes on Testing Paytm:

(1) Add Your Paytm Merchant ID and Other Details in bottom of settings.py file

(2)  

Paytm Wallet 
  Mobile no : 7777777777 ( '7' 10 times) 
  Password: Paytm12345 OTP : 489871

Card 
  card no : any visa or master card 
  expiration month : any future date 
  cvv : 123 
  otp : 123123

( this is because here i am using paytm payment-gateway-api in test mode as i don't have paytm merchant account.so please use following info)
