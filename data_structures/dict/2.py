"""
Write a program to concatenate the following dictionaries 
to create a new one.  

Sample Dictionary : 
dic1={1:10, 2:20}  dic2={3:30, 4:40}  dic3={5:50,6:60} 

Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
"""
dic1={1:10, 2:20}  
dic2={3:30, 4:40}  
dic3={5:50,6:60} 
dic4= dict()

mode = int(input("Enter mode (1/2/3): "))

if mode == 1:
    dic4.update(dic1) ; dic4.update(dic2) ; dic4.update(dic3)
    print("Using update keyword")

if mode == 2:
    dic4 = {**dic1, **dic2, **dic3}
    print("Using unpack operation: {**dic1, **dic2}")

if mode == 3:
    dic4 = dic1 | dic2 | dic3
    print("Merge: dic1 | dic2")
    
print(dic4)
