class Bank:
    bank_name='Andhra Bank'
    def __init__(self,customer_name,cus_acc_no):
        self.customer_name=customer_name
        self.cus_acc_no=cus_acc_no
        
    def display_customer_details(self):
        #self.customer_name='Dravid'
        print("customer name=",self.customer_name)
        print("customer account number=",self.cus_acc_no)


    @classmethod
    def bank_name_change(cls,bank_name):
        #print(cls.customer_name)
        cls.bank_name=bank_name
        
    @staticmethod
    def interest_calculation(principal_amount,interest_rate,no_of_months):
        #print(bank_name)
        #print(Bank.customer_name)
        print("Intereset=",(principal_amount/100)*(interest_rate*no_of_months))

cus1=Bank('Anil',100)
cus2=Bank('Sachin',200)
cus1.display_customer_details()
Bank.bank_name_change('Union Bank')
cus2.interest_calculation(100,2,11)
