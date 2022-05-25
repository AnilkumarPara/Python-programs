class Bank:
    def __init__(self,customer_name,cus_acc_no):
        #self.cus_name=customer_name
        
        self.customer_name=customer_name
        print(f"{self} cus_name address=",id(self.customer_name))
        self.cus_account_no=cus_acc_no
        print(f"{self} cus_account_no address=",id(self.cus_account_no))
    
    def display_customer_details(self):
        #self.customer_name='Dravid'
        print("customer name=",Bank.customer_name)
        print("customer account number=",self.cus_account_no)


cus1=Bank('Sachin',100)
cus2=Bank('Jayalalitha',200)
print("--------Customer 1 details-----------")
cus1.display_customer_details()
print("--------Customer 2 details-----------")
cus2.display_customer_details()
Bank.display_customer_details(cus1)
#print(Bank.customer_name)
