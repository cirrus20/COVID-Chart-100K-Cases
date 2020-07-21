import matplotlib.pyplot as plt

#sets
States = ['AZ','CA','FL','GA','IL','MA','NJ','NY','NC','PA','TX']
Cases = [145320,400195,360386,132788,164224,113789,178937,412034,101286,106498,345672]

#actions
plt.title ('COVID Victims Graph')

plt.xlabel('State')
plt.ylabel('Cases')
plt.bar(States,Cases,color='green')

plt.show()