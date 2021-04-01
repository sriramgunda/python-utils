from collections import Counter
  
# Create a list
names = ['sriram', 'harish', 'ravi', 'nava', 'harish', 'sriram', 'sriram']
count_names = Counter(names)
print(count_names)
print(count_names.most_common()[0])
  
namelist = ['sriram','harish','ravi','nava', 'mouni']
  
# Here mouni is not in names 
# so count of mouni will be zero
for name in namelist:
    print (name, count_names[name])
