### ex 1

# class A:
#     a=10
#     b=20

#     @classmethod
#     def disp(cls):
#         print(cls.a,cls.b)

# class B(A):
#     c=30
#     def __init__(self,m,n):
#         self.m=m
#         self.n=n

#     def display(self):
#         print(self.m,self.n)

# obj=B(500,600)
# obj.display()
# obj.disp()
# print(obj.a,obj.b)
# B.a



## ex 2

# class Bank:
#     bank_name="SBI"
#     bank_loc="Mysore"

#     def __init__(self,name,phno,adrs,bal):
#         self.name=name
#         self.phno=phno
#         self.adrs=adrs
#         self.bal=bal

#     @classmethod
#     def display(cls):
#         print(cls.bank_name,cls.bank_loc)

#     def disp(self):
#         print(self.name,self.phno,self.adrs,self.bal)

#     def change_address(self,new_adrs):
#         self.adrs=new_adrs
#         print(f"{self.name} your address has been updated successfully")


#     def change_phno(self,new_phno):
#         self.phno=new_phno
#         print(f"{self.name} your mobile number has been updated successfully")


# class Bank_update(Bank):
#     def __init__(self,name,phno,adrs,bal,email,pan,adhar):
#         self.name=name
#         self.phno=phno
#         self.adrs=adrs
#         self.bal=bal
#         self.email=email
#         self.pan=pan
#         self.adhar=adhar


#     def disp1(self):
#         print(self.name,self.phno,self.adrs,self.bal,self.email,self.pan,self.adhar)


# cst1=Bank_update("Deepak",8618164236,"peelamedu",90000,"deepakarjun678@gmail.com","HER4321S",243532456789456)
# cst2=Bank_update("Deepika",9619165337,"nava india",80000,"deepikpadukone678@gmail.com","RTYYT5462W",569056987566)

# cst1.disp1()
# cst1.disp()
# cst1.display()
# cst1.change_phno(676767673984)
# cst1.disp1()


## ex 3

class Bank:
    bank_name="SBI"
    bank_loc="Mysore"

    def __init__(self,name,phno,adrs,bal):
        self.name=name
        self.phno=phno
        self.adrs=adrs
        self.bal=bal

    @classmethod
    def display(cls):
        print(cls.bank_name,cls.bank_loc)

    def disp(self):
        print(self.name,self.phno,self.adrs,self.bal,end=' ')

    def change_address(self,new_adrs):
        self.adrs=new_adrs
        print(f"{self.name} your address has been updated successfully")


    def change_phno(self,new_phno):
        self.phno=new_phno
        print(f"{self.name} your mobile number has been updated successfully")


class Bank_update(Bank):
    def __init__(self,name,phno,adrs,bal,email,pan,adhar):
        super().__init__(name,phno,adrs,bal)
        self.email=email
        self.pan=pan
        self.adhar=adhar

    def disp1(self):
        super().disp()
        print(self.email,self.pan,self.adhar)


cst1=Bank_update("Deepak",8618164236,"peelamedu",90000,"deepakarjun678@gmail.com","HER4321S",243532456789456)
cst2=Bank_update("Deepika",9619165337,"nava india",80000,"deepikpadukone678@gmail.com","RTYYT5462W",569056987566)

cst1.disp()
cst1.disp1()