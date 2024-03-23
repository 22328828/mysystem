import pandas as pd
'''Task 3: Data analysis using python (lists and data frames for managing books and members).
You are provided with insurance dataset on blackboard. Please logon on blackboard and download the
dataset. Write a python code to:
§ Read the dataset.
§ Inspects its column by displaying the first 10 records.
§ Display records for make and usage for sets_num that are more than 40.
§ Plot a basic graph showing effective_yr on y axes and carrying capacity on x-axes
Submission Guidelines
• Add xpiyose@gmail.com as a collaborator for your project.
• Push the final version of your code to the shared repository.'''

data = pd.read_csv("C:\Users\USER\Downloads\motor_insure.csv")
print(data.head(10))

#print(data[data['sets_num']> 40 ][['make','usage']])

import matplotlib.pyplot as pit 

pit.plot(data['EFFECTIVE_YEAR'],data['EFFECTIVE_YEAR'])
pit.ylabel('EFFECTIVE YEAR')
pit.xlabel('CARRYING CAPACITY')
pit.title('EFFECTIVE YEAR VS CARRYING CAPACITY')
pit.show()
