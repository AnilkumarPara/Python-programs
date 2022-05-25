class Bank:
    bank_name='Andhra Bank'
    def __init__(self,customer_name,cus_acc_no):
        self.customer_name=customer_name
        self.cus_acc_no=cus_acc_no
    
    @classmethod
    def bank_name_change(cls,bank_name):
        #print(cls.customer_name)
        cls.bank_name=bank_name

cus1=Bank('Anil',100)
cus2=Bank('Sachin',200)
print("Bank name before changing=", cus1.bank_name)
print("Bank name before changing=", cus2.bank_name)
print("Bank name before changing=", Bank.bank_name)
Bank.bank_name_change('Union Bank')
print("Bank name after changing=", cus1.bank_name)
print("Bank name after changing=", cus2.bank_name)
print("Bank name after changing=", Bank.bank_name)
