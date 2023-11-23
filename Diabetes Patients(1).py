#!/usr/bin/env python
# coding: utf-8

# # To Visualize Diabetes Patients 

# ### Import The Libraries 

# In[1]:


import pandas as pd  # data preprocessing
import seaborn as sns  # visualization
import matplotlib.pyplot as plt  # visualization
from sklearn import datasets  #implement machine learning models and statistical modelling


# ### Feature Description

# In[2]:


#INSIGHTS

#Out of a total of 2.954 pregnancies 449% 1,304) were diagnosed is diabetic, while the remaining 56% (1.650) were categorized as non-diabetic


#Among the 768 individual's surveyed was found that 268 of them were suffering from diabetes Additionaly, within this group, 219 patients were classified as obese, with a BMI exceeding 30, while 34 patients were identified as overweight with a BMI ranging from 25 to 30.


#In the survey of 768 individuals, 268 of whom were diabetic patients, it was observed that 167 had a diastolic blood pressure reading within the healthy range of 50-80 mm Hg, while 77 fell within the range of 80-120 mm Hg and 24 exhibited a diastolic blood pressure below the recommended healthy threshold of 50 mm Hg.


#A notable observation in the study is that the majority of diabetic women are within the age range of 20-60. Among this group, 90 women fall within the 20-30 age bracket, 76 are in the 30-40 age range, 64 belong to the 40-50 age category, and 31 are situated in the 50-60 age group.


#In the diabetic patient group, 146 individuals showed an insulin reading of mu U/ml, etten linker to type 1 diabetes, where the immuna systemdamages insulin-producing cells. Also, 111 diabetic patients had high insulin levels 105 mu U/ml) while 17 had moderate levels (<100 mu U/ml). These varied insulin profiles provide sights into diabetes management.


#The majority of diabetic patients exhibit plasma glucose concentrations between 126 and 200 mg/l during a 2-hour oral glucose tolerance test


#The majority of diabetic patients typically exhibit an average skin thickness ranging from 1671 mm to 25.22 mm


#A majority of patients, specifically 65% fall within the low risk category based on the Pedigree Function group, faling between values greater than 01 and less than 0.5. Additionally, 29% of patients are classified as being at moderate risk with values ranging from greater than 0.5 to less than 1. Only a smaller subset, comprising 5% of patients, are positioned in the high-risk category, characterized by Pedigree Function values exceeding 1


# ### Load Data Set 

# In[3]:


#Import Data
df = pd.read_csv('diabetes.csv')


# In[4]:


#Top 5 Rows Diabetes Table
df.head()


# In[5]:


df.dropna()


# ### Number Of Rows And Columns 

# In[6]:


#Rows & Column
df.shape


# In[7]:


#Columns Of Diabetes Table
df.columns


# In[8]:


#Average Of Patient Age
Average_age = df["Age"].mean()
Average_age = int(Average_age)
Average_age


# In[9]:


#Average Of BMI
Average_BMI = df["BMI"].mean()
round(Average_BMI,2)


# In[10]:


#Average Of BloodPressure
Average_BP = df["BloodPressure"].mean()
round(Average_BP,2)


# In[11]:


#Total Pregnancies
Total_Preg = df["Pregnancies"].sum()
Total_Preg


# In[12]:


plt.figure(figsize = (8,6))
sns.boxplot(x = 'Pregnancies',y = 'BloodPressure',data = df)

plt.xlabel("Pregnancies")
plt.ylabel("Count of BloodPressure")
plt.title("Pregnancies Vs BloodPressure")
plt.show()


# In[13]:


sns.scatterplot(x = 'Age',y = 'Insulin',data = df)
plt.xlabel("Age")
plt.ylabel("Insulin")
plt.title("Age Vs Insulin")
plt.show()


# In[14]:


plt.figure(figsize = (8,6))
sns.lineplot(x = "Pregnancies",y = "Outcome",data = df)
plt.title("Pregnancies Vs DiabetesRate")
plt.ylabel("DiabetesRate")
plt.show()


# In[15]:


plt.figure(figsize = (8,4))
sns.histplot(data = df,x = "Age",bins = 20,kde = True)
plt.show()


# In[16]:


correlation_matrix = df.corr()

plt.figure(figsize=(10, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()


# ## SUGGESIONS

# In[17]:


#SUGGESIONS


#Prevalence of Diabetes: Out of 2,954 pregnancies, 44% were diagnosed as diabetic. This incicates a reatively high prevalence of diabetes in this population


#Age and Diabetes: The majority of diabetic women fall within the age range of 20-60. This suggests that diabetes is prevalent across different age groups, with a higher concentration in middle-aged individuals it's important to target diabetes prevention and management efforts across all age groups, with a focus on those in their 30s and 40s


#Insulin Levels: Insuan readings provide insights into the type and severity of diabetes: The presence of individuals with very low insulin levels (mu U/ml) suggests the poss baty of type 1 diabetes, which is an autoimmune condition. High insulin levels (> 105 mu /m may indicate insulin resistance, a common feature in type 2 diabetes. Moderate insulin levels [100 mu U/ml) may also be seen in type 2 diabetes. Effective diabetes management should be tailored to the specific type and insulin levels of patients. 
                                                                          

#Blood Glucose Levels: Most diabetic patients exhibit plasma glucose concentrations between 126 and 200 mg/dL during 2-hour cral glucose tolerance test. This range indicates Impaired glucose tolerance and is characteristic of diabetes Glycemic contro is essential for diabetes management and patients falling within this range should receive education and support on blood sugar management through diet, exercice and medication as needed


#BMI and Weight: Some diabetic patients are classified as obese or overweight. Weight management is crucial for diabetes control, and individuals with high BMI should be encouraged to adopt a healthier lifestyle, including e balanced diet and regular physical activity. 

#Blood Pressure: Blood pressure levels can impact diabetes management Monitoring and maintaining healthy blood pressure (between 50-80 m Hy is essential for diabetic patients to reduce the risk of complications. Those with elevated blood pressure should receive appropriate treatment and lifestyle advice.


#Skin Thickness: White skin thickness may not directly correlate with diabetes, it could be indicative of other health issues. Further investigation may be needed to understand any potential associations


#Pedigree Function: The Pedigree Function values indicate the genetic risk of diabetes: Patients in the high-risk category may benefit from more intensive monitoring and ifestyle interventions to reduce their risk.


# In[ ]:





# In[ ]:




