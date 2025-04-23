import matplotlib.pyplot as pit
import numpy as np

# placements = [500,300,200,100,50]
# branch = ['cse','csm','csc','csd','cso']


#bar chart
# pit.title("Placement Comparison")
# pit.xlabel("Branch")
# pit.ylabel("Placements")
# mycolors = ["red","yellow","blue","pink","orange"]
# pit.legend(title="mycolors")

# pit.bar(branch,placements,color=mycolors)
# for i, value in enumerate(placements)
# pit.show()


#pie chart
# placements = np.array([500,300,240,290,80])
# my_labels = ["cse","csm","csc","csd","cso"]
# my_explode = [0.2,0,0,0,0]
# mycolors = ["red","yellow","blue","pink","orange"]
# pit.pie(placements,labels=my_labels,colors=mycolors,explode=my_explode,shadow=True,autopct='%2.1f%%')
# pit.show()


#histo graph
# num = np.random.randint(100,200,100)

# pit.hist(num,bins=10,edgecolor="black",color="yellow")
# pit.title("Histogram")
# pit.xlabel("X-axis")
# pit.ylabel("Y-axis")
# pit.show()

# pillow

# np.random.seed(42)
# data = np.random.normal(0,1,100)
# print(data)

# pit.boxplot(data)
# pit.show()

placements = [400,300,200,100,50]
branch = ['cse','csm','csc','csd','cso']

pit.scatter(placements,branch)
placements1 = [350,250,150,100,90]
branch1 = ['cse','csm','csc','csd','cso']
pit.scatter(placements1,branch1,marker='+',alpha=0.7,s=1000)
pit.show()



