import pandas as pd
import statistics

df = pd.read_csv("data.csv")
data = df["Weight(Pounds)"].tolist()

mean=statistics.mean(data)
deviation=statistics.stdev(data)

print(mean)
print(deviation)

range1_start,range1_end=mean-1*deviation,mean+1*deviation
range2_start,range2_end=mean-2*deviation,mean+2*deviation
range3_start,range3_end=mean-3*deviation,mean+3*deviation

range1_array = [i for i in data if i > range1_start and i < range1_end]  
range2_array = [i for i in data if i > range2_start and i < range2_end]  
range3_array = [i for i in data if i > range3_start and i < range3_end] 

length=len(data)
length1=len(range1_array)
length2=len(range2_array)
length3=len(range3_array)

percentage_range1=length1*100/length
percentage_range2=length2*100/length
percentage_range3=length3*100/length

print(percentage_range1)
print(percentage_range2)
print(percentage_range3)