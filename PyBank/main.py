
# coding: utf-8

# In[1]:


import csv


# In[2]:


bank_data='budget_data.csv'


# In[3]:


print("Financial Analysis")
print("----------------------------")

month=[]
money=[]
change=[]
with open(bank_data) as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        month.append(row[0])
        money.append(row[1])


# In[4]:


print(f'Total Months: {len(month)-1}')


# In[5]:


money.remove("Profit/Losses")
money = list(map(int, money))


# In[6]:


sum=0
for i in range(len(money)):
    sum=sum+money[i]
    ave_change=(money[-1]-money[0])/(len(money)-1)
    
    if i >=1:
        changes=money[i]-money[i-1]
        change.append(changes)
        max_change=max(change)
        max_date=month[change.index(max(change))+2]
        min_change=min(change)
        min_date=month[change.index(min(change))+2]
print(f"Total: ${sum}") 
print(f"Average Change: ${ave_change:.2f}") 
print(f"Greatest Increase in Profits: {max_date} (${max_change})")
print(f"Greatest Decrease in Profits: {min_date} (${min_change})")


# In[7]:


txtpath='output.txt'
txtfile=open(txtpath, "w")


# In[8]:


txtfile.write("Financial Analysis\n")
txtfile.write("----------------------------\n")
txtfile.write(f'Total Months: {len(month)-1}'+"\n")
txtfile.write(f"Total: ${sum}"+"\n") 
txtfile.write(f"Average Change: ${ave_change:.2f}"+"\n") 
txtfile.write(f"Greatest Increase in Profits: {max_date} (${max_change})"+"\n")
txtfile.write(f"Greatest Decrease in Profits: {min_date} (${min_change})"+"\n")
txtfile.close()

