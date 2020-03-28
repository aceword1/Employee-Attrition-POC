#!/usr/bin/env python
# coding: utf-8
#----------------------------------------------------------------------------------
#Company X has an issue with employee attrition. 
#The Company needs a lasting analytical solution to diagnose the causes and predict the future effects.
#----------------------------------------------------------------------------------
# In[ ]:


#import the necessary modules
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import statistics


# In[ ]:


#read the csv file
existing_employee = pd.read_csv("/content/existing_employee.csv")
employee_who_left= pd.read_csv("/content/employee_who_left (2).csv")


# In[7]:


#test the data - existing employees
existing_employee.head()


# In[8]:


#test the data - employees who left
employee_who_left.head()


# ***********************************************DATA ANALYSIS*******************************************************************

# In[ ]:


#data analysis


# ************************************SALARY COUNT FOR EXISTING AND EXITED EMPLOYEES********************************************

# In[9]:


#employees who left
employee_who_left.salary.value_counts()


# In[10]:


#existing employees
existing_employee.salary.value_counts()


# In[ ]:





# ******WORK ACCIDENT COUNT FOR BOTH EMPLOYEES WHO LEFT AND EXISTING*********
# 

# In[11]:


employee_who_left['Work_accident'] = employee_who_left.Work_accident.replace(to_replace =1, value ="Yes") 
employee_who_left['Work_accident'] = employee_who_left.Work_accident.replace(to_replace =0, value ="No")
employee_who_left.Work_accident.value_counts()


# In[12]:


existing_employee['Working_accident'] = existing_employee.Work_accident.replace(to_replace =1, value = 'Yes')
existing_employee['Working_accident'] = existing_employee.Work_accident.replace(to_replace =0, value = 'No')
existing_employee.Work_accident.value_counts() 


# *********PROMOTION COUNT FOR THE LAST 5YEARS FOR BOTH EMPLOYEES WHO LEFT AND EXISTING*********

# In[13]:


employee_who_left['promotion_last_5years'] = employee_who_left.promotion_last_5years.replace(to_replace =1, 
                 value ="Yes") 
employee_who_left['promotion_last_5years'] = employee_who_left.promotion_last_5years.replace(to_replace =0, 
                 value ="No")
employee_who_left.promotion_last_5years.value_counts()


# In[14]:


existing_employee['promotion_last_5years'] = existing_employee.promotion_last_5years.replace(to_replace =1,
                                  value = 'Yes')
existing_employee['promotion_last_5years'] = existing_employee.promotion_last_5years.replace(to_replace =0,
                                   value = 'No')
existing_employee.promotion_last_5years.value_counts()


# 
# ******CROSS ANALYSIS FOR BOTH EMPLOYEES WHO LEFT AND EXISTING EMPLOYEES*******

# **SALARY PLOT**

# In[15]:


plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
sns.countplot(employee_who_left['salary'])
plt.title('Distribution of salaries of Employees who left the company')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.tight_layout()


# In[16]:


plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
sns.countplot(existing_employee['salary'])
plt.title('Distribution of salaries of Existing Employees in the company')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.tight_layout()


# In[ ]:





# **DEPARTMENT BAR PLOT**

# In[17]:


plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
sns.countplot(employee_who_left['dept'])
plt.title('Departments of Employees who left the Company')
plt.tight_layout()


# In[ ]:





# In[18]:


plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
sns.countplot(existing_employee['dept'])
plt.title('Departments of Existing Employee ')
plt.tight_layout()


# In[ ]:





# **SATISFACTION LEVEL**

# In[47]:


plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
sns.boxplot(x='dept', y='satisfaction_level', data=employee_who_left)
plt.ylim([0,1])
plt.title('Distribution of satisfaction level of Employees that left by Department')
plt.xlabel('Department')
plt.ylabel('Satisfaction Level')
plt.tight_layout()


# In[ ]:





# In[48]:


plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
sns.boxplot(x='dept', y='satisfaction_level', data=existing_employee)
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.1))
plt.title('Distribution of satisfaction level of Existing Employees by Department')
plt.xlabel('Department')
plt.ylabel('Satisfaction Level')
plt.tight_layout()


# From the box plot of both Existing employees and employees who left the company, the following insights have been discovered 
# 
# 1.   The mean satisfaction level of employees who left the company ranges bewteen 40-50% 
# 2.   The mean satisfaction level of existing employees in  the company ranges between 60-70%
# 
# Performing further analysis on the satisfaction level of both employees who left and existing employees in the company for better insight 
# 

# In[ ]:





# In[21]:


plt.figure(figsize=(14,7))
sns.set(style='darkgrid')
sns.barplot(x='dept', y='satisfaction_level', hue='salary', data = employee_who_left)
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.05))
plt.title('Satisfaction level by Dept based on the Salary of Employees who left')
plt.tight_layout()
plt.legend(loc=2)


# In[22]:


plt.figure(figsize=(14,7))
sns.set(style='darkgrid')
sns.barplot(x='dept',y='satisfaction_level',hue='salary',data= existing_employee)
plt.title('Satisfaction level by dept based on the Salary of Existing Employee')
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.05))
plt.tight_layout()
plt.legend(loc=2)


# In[23]:


plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
plt.hist(employee_who_left['satisfaction_level'])
plt.title('Distribution of satisfaction_level of Employees who left')
plt.xlabel('satisfaction_level')
plt.ylabel('Frequency')
plt.tight_layout()


# In[ ]:


employee_who_left['satisfaction_level2'] = pd.cut(employee_who_left['satisfaction_level'], 
       3, labels=["small", "medium", "high"])


# In[25]:


employee_who_left.satisfaction_level2.value_counts()


# In[26]:


plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
plt.hist(employee_who_left['satisfaction_level2'])
plt.title('Distribution Range of satisfaction_level of Employees who left')
plt.xlabel('satisfaction_level')
plt.ylabel('Frequency')
plt.tight_layout()


# In[27]:


plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
plt.hist(existing_employee['satisfaction_level'])
plt.title('Distribution of satisfaction_level of Existing Employees')
plt.xlabel('satisfaction_level')
plt.ylabel('Frequency')
plt.tight_layout()


# In[ ]:


existing_employee['satisfaction_level2'] = pd.cut(existing_employee['satisfaction_level'], 
       3, labels=["small", "medium", "high"])


# In[29]:


existing_employee.satisfaction_level2.value_counts()


# In[30]:


plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
plt.hist(existing_employee['satisfaction_level2'])
plt.title('Distribution Range of satisfaction_level of Existing Employees')
plt.xlabel('satisfaction_level')
plt.ylabel('Frequency')
plt.tight_layout()


# From the satisfaction level chart plots of employees who left the company, it is observed that the satisfaction level is below average, therefore it is vital to show the percentage of employees who left that are in this category 

# DETERMINING THE PERCENTAGE OF EMPLOYEES WHO LEFT THE COMPANY HAD A SATISFACTION LEVEL BELOW AVERAGE OF 45

# In[31]:


(len(existing_employee[existing_employee['satisfaction_level']<0.45])/len(existing_employee)) * 100


# From the output generated it can be observed that an estimate of 65% of employees who left had a satisfaction level below average of 45%.
# This needs to be looked into as it's a determining factor as to why employees left the company.
# Futher insights needs to be carried out as to why the satisfaction level is low.
# Promotion status, salary where two factors that was considered by intuition which prompted further analysis to determine the percenatge of employees who left having a satisfaction level of 45%, their promotion status and salary range

# In[33]:


(existing_employee[existing_employee['satisfaction_level']<0.45] ['salary'].value_counts(normalize=True))*100


# From the output displayed, it can be seen that an estimate of 61% of employees who left where low income earners, 37% where medium income earners and 2% where high income earners.

# In[34]:


(existing_employee[existing_employee['satisfaction_level']<0.45] ['promotion_last_5years'].value_counts(normalize=True))*100


# From the output displayed, it can be seen that 99.6% of employees who left had a satisfaction level less than 45% and where not promoted in the last five years

# Through the insights gained from the employees who left, it is vital to validate the position of the existing employees in the company.

# DETERMINING THE MEAN SATISFACTION LEVEL OF EXISTING EMPLOYEES

# In[35]:


statistics.mean(existing_employee['satisfaction_level'])*100


# From the output it is seen that the average satisfaction level of existing employees is estimated around 67%. Hence using the metrics/determing factor of employees who left as an insight to crosscheck existing employees who are prone to leave the company considering their promotion status

# In[36]:


(len(existing_employee[existing_employee['satisfaction_level']<0.45])/len(EL)) * 100


# In[37]:


(existing_employee[existing_employee['satisfaction_level']<0.45] ['promotion_last_5years'].value_counts(normalize=True))*100


# From the result displayed it shows 44% of existing employees have a satisfaction level below 45% and from this it is seen that an estimate of 98% have not been promoted in the last 5 years

# 

# BI/MULTIVARIATE ANALYSIS

# In[ ]:


plt.figure(figsize=(14,7))
sns.set(style='darkgrid')
sns.barplot(x='dept', y='satisfaction_level', hue='salary', data = employee_who_left)
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.05))
plt.title('Satisfaction level by Dept based on the Salary of Employees who left')
plt.tight_layout()
plt.legend(loc=2)


# In[46]:


plt.figure(figsize=(14,7))
sns.set(style='darkgrid')
sns.barplot(x='dept', y='satisfaction_level', hue='salary', data = existing_employee)
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.05))
plt.title('Satisfaction level by Dept based on the Salary of  Existing Employees')
plt.tight_layout()
plt.legend(loc=2)


# In[38]:


employee_who_left_PRO =employee_who_left.pivot_table(index='salary',columns='promotion_last_5years',values='satisfaction_level')
employee_who_left_PRO.plot.bar()
plt.title("Satisfaction Level of Employees who left based on Salary and Promotion Status")
plt.xlabel("Salary Range")
plt.ylabel("Satisfaction Level")


# Insight: Most employees who left with a high salary range weren't promoted,regardless of other employee who were promoted that had their salary range from low to medium, it futher can be seen that the satisfaction level was below average of 45% and the employees who left where not promoted irrespective of their salary income. 
# Hence Satisfaction level and promotion status are determining factors as to why employees are leaving the company.

# In[39]:


Existing_Employee_PRO =existing_employee.pivot_table(index='salary',columns='promotion_last_5years',values='satisfaction_level')
Existing_Employee_PRO.plot.bar()
plt.title(" Satisfaction Level of Existing Employee based on Salary and Promotion Status")
plt.xlabel("Salary Range")
plt.ylabel("Satisfaction Level")
plt.legend(loc=2)


# The insight obtained from this ouput for employees still existing in the company is such that salary is not a determining  factor as to why the existing employees should leave the company due to the fact that the employees satisfaction level is above an average of 50% irrespective of their promotion status.

# In[40]:


EL_PRO =employee_who_left.pivot_table(index='time_spend_company',columns='promotion_last_5years',values='satisfaction_level')
EL_PRO.plot.bar()
plt.title("Satisfaction Level of Employee who left based on Time Spent in the company and promotion Status")
plt.xlabel("Time Spent")
plt.ylabel("Satisfaction Level")


# From output above the insight: Time Spent and promotion status are great factors that determine if an employee should leave or not, some employee who left that spent 6 years in the company weren't promoted, even though their satisfaction level was quite moderate.
# It can also be seen that An avaerge employee who left spent about 4 years with 0.45 satisfaction level and wasn't promoted. 
# 
# Recommedation: 

# In[41]:


Existing_Employee_PRO =existing_employee.pivot_table(index='time_spend_company',columns='promotion_last_5years',values='satisfaction_level')
Existing_Employee_PRO.plot.bar()
plt.title("Satisfaction Level of Existing Employee based on Time Spent in the company and promotion Status")
plt.xlabel("Time Spent")
plt.ylabel("Satisfaction Level")
plt.legend(loc=2)


# From the output the insight obtained is such that the existing employees in company irrespective of the time spent have a moderate satisfaction level and positive promotion  status above 0.5 exculding employeees that spent between 5 years in the company.
# Hence satisfaction level of employees that spent 5 years should is considered as a determining factor and why such employees are prone to leave.

# In[42]:


EL_PRO =employee_who_left.pivot_table(index='salary',columns='Work_accident',values='satisfaction_level')
EL_PRO.plot.bar()
plt.title("Satisfaction Level of Employees who left based on Salary and work accident")
plt.xlabel("Salary")
plt.ylabel("Satisfaction Level")


# From the output the insight obtained is such that employees who left that earn between low and medium salaries where affected by work accidents and their satisfaction level was below avaerage of 0.45 as compared to those with a high salary.
# Hence work accident and satisfaction level are reasons as to why employees are leaving the company.

# In[43]:


Existing_Employee_PRO =existing_employee.pivot_table(index='salary',columns='Work_accident',values='satisfaction_level')
Existing_Employee_PRO.plot.bar()
plt.title("Satisfaction Level of Existing Employee based on Salary in the company and work accident")
plt.xlabel("salary")
plt.ylabel("Satisfaction Level")


# In[44]:


EL_PRO =EL.pivot_table(index='number_project',columns='promotion_last_5years',values='satisfaction_level')
EL_PRO.plot.bar()
plt.title("Satisfaction Level of Employees who left based on Number of Projects and Promotion Status")
plt.xlabel("Number Project")
plt.ylabel("Satisfaction Level")


# From the output displayed, the insight gotten it can be seen that as the number of projects embarked on by employees who left exceeded 4, the satisfaction level began to decline and they where not promoted in the last five years.
# Hence an increase in the number of projects resulting in a decline in satisfaction level and employee promotion status can be seen as reasons as to why employees are leaving the company.

# In[45]:


Existing_Employee_PRO =existing_employee.pivot_table(index='number_project',columns='promotion_last_5years',values='satisfaction_level')
Existing_Employee_PRO.plot.bar()
plt.title("Satisfaction Level of Existing Employee based on Number of Projects and Promotion Status")
plt.xlabel("Number Project")
plt.ylabel("Satisfaction Level")


# From the output displayed, the insight gotten it can be seen that as the number of projects embarked on by employees still in the company exceeded 4, the satisfaction level began to decline and they where not promoted in the last five years, this can also be seen as a trend for employees who left.
# Hence an increase in the number of projects resulting in a decline in satisfaction level and employee promotion status can be seen as reasons as to which exsiting employees are prone to leave the company.
