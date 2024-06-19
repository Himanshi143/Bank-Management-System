#Bank Management System
import os
class Account:
  def __init__(self):
    self.acc=[]
  def addide(self,accno,name,types,deposit):
    self.acc.append({"Account Number":accno,"Name":name,"Type":types,"Deposit":deposit})
  def deps(self,ac,dep):
    for i in range(len(self.acc)):
      if(self.acc[i]["Account Number"]==ac):
        self.acc[i]["Deposit"]+=dep
        r=str(ac)+".txt"
        f=open(r,"a")
        f.write("\n Deposited amount: "+str(dep))
        f.write("\n Total amount: "+str(self.acc[i]["Deposit"]))
        f.close()
      else:
        continue
  def wits(self,ac,dep):
    for i in range(len(self.acc)):
      if(self.acc[i]["Account Number"]==ac):
        if(self.acc[i]["Deposit"]>dep):
          self.acc[i]["Deposit"]-=dep
          r=str(ac)+".txt"
          f=open(r,"a")
          f.write("\n Withdrawal amount: "+str(dep))
          f.write("\n Total amount: "+str(self.acc[i]["Deposit"]))
          f.close()
        else:
          print("Enter amount less than deposited amount")
      else:
        continue
  def bala(self,ac):
    for i in range(len(self.acc)):
      if(self.acc[i]["Account Number"]==ac):
        print("Balance left: ",self.acc[i]["Deposit"])
      else:
        continue
  def accholder(self):
      for i in range(len(self.acc)):
       print(str(self.acc[i]["Account Number"])+"        "+self.acc[i]["Name"]+"        "+self.acc[i]["Type"])
  def cls(self,ac):
    for i in range(len(self.acc)):
      if(self.acc[i]["Account Number"]==ac):
        r=str(ac)+".txt"
        os.remove(r)
        self.acc.pop(i)
      else:
        continue
  def dele(self):
    for i in range(len(self.acc)):
      b=self.acc[i]["Account Number"]
      r=str(b)+".txt"
      os.remove(r)


def main():
  obj=Account()
  while True:
    print("1. Create new account and Enter details")
    print("2. Deposit already created account: ")
    print("3. Withdrawal already created account: ")
    print("4. Balance Enquiry")
    print("5. Account holder list")
    print("6. Close account")
    print("7. To exit")
    ch=int(input("Enter choice: "))
    if(ch==1):
      a=int(input("Enter account Number atleast of length 3: "))
      n=input("Enter name as per in Aadhar Card: ")
      t=input("Enter type of the account either *C* for current and *S* for saving: ").upper()
      d=float(input("Deposit ammount [Saving>=1000 and Current>=1500]: "))
      if(len(str(a))>=3 and t=="C" and d>=1500):
        obj.addide(a,n,t,d)
        z=str(a)+".txt"
        f=open(z,"a")
        q="   Account Number: "+str(a)+"     Name: "+str(n)+"     Type: "+str(t)+"    Deposit: "+str(d)
        f.write(q)
        f.close()
      elif(len(str(a))>=3 and t=="S" and d>=1000):
        obj.addide(a,n,t,d)
        z=str(a)+".txt"
        f=open(z,"a")
        q="   Account Number: "+str(a)+"     Name: "+str(n)+"     Type: "+str(t)+"    Deposit: "+str(d)
        f.write(q)
        f.close()
      else:
        print("Enter correct details")
    elif(ch==2):
      ac=int(input("Enter account number in which it is to be deposited: "))
      dep=float(input("Enter amount to be deposited: "))
      obj.deps(ac,dep)
    elif(ch==3):
      ac=int(input("Enter account number in which it is to be withdraw: "))
      dep=float(input("Enter amount which u want to widraw : "))
      obj.wits(ac,dep)
    elif(ch==4):
      ac=int(input("Enter account number to get balance left: "))
      obj.bala(ac)
    elif(ch==5):
      print("HOLDERS LIST:")
      obj.accholder()
    elif(ch==6):
      ac=int(input("Enter account number of the account to be closed: "))
      obj.cls(ac)
      print("Account Closed")
    elif(ch==7):
      obj.dele()
      break
    else:
      print("Choose Correct operation")
if __name__=="__main__":
  main()