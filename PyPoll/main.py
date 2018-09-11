
# coding: utf-8

# In[1]:


import csv


# In[2]:


poll_data='election_data.csv'


# In[3]:


textpath='output.txt'
textfile=open(textpath,'w')


# In[4]:


print("Election Results")
print("----------------------------")


# In[5]:


textfile.write("Election Results\n")
textfile.write("----------------------------\n")


# In[6]:


voter=[]
county=[]
votelist=[]

with open(poll_data) as csvfile:
    csvreader = csv.reader(csvfile)
    #skip the header
    header=next(csvreader)
    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        votelist.append(row[2])
print(f'Total Votes: {len(voter)}')
print("----------------------------")


# In[7]:


textfile.write(f'Total Votes: {len(voter)}'+'\n')
textfile.write("----------------------------\n")


# In[8]:


candidates=[]
candidates=list(set(votelist))


# In[9]:


vote_num=[]

for c in candidates:
    count=0
    for v in votelist:
        if c==v:
            count=count+1
    vote_num.append(count)
    
    print(f"{c}: {votelist.count(c)/len(voter):.3%} ({votelist.count(c)})")


# In[10]:


textfile.write(f"{c}: {votelist.count(c)/len(voter):.3%} ({votelist.count(c)})"+'\n')


# In[11]:


winner=candidates[vote_num.index(max(vote_num))]
print("----------------------------")
print(f'Winner: {winner}')
print("----------------------------")


# In[12]:


textfile.write("----------------------------\n")
textfile.write(f'Winner: {winner}'+"\n")
textfile.write("----------------------------\n")
textfile.close()

