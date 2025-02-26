## unordered
## key value paire 

# You can define dictionory in two way 
my_dist = {"name":"sandesh", "age": 26, "bmi": 19.5, "code": "python"}

print(my_dist["age"]) ## You can call a key it will give the value of key like age is key and 26 is value.
print(my_dist)
my_dist = {
            "name":"sandesh",
           "age": 26,
            "bmi": 19.5,
            "code": "python"
         }
print(my_dist["age"]) ## pass the key name here 
print(my_dist)

##Upldate the vule of key

my_dist["age"]=30
print(my_dist)

del my_dist["bmi"]  ## pass the key name here  delte the va;ue
print(my_dist)

# my_dist.update("bmi", 20)
# print(my_dist)


for i in my_dist: ## Get only Key
   print(i)

for i in my_dist.values():  ## Get only value
   print(i)

for i,j in my_dist.items():  ## Both only value
   print(i,j)

for i in my_dist:  ## Both only value
   print(i, my_dist[i])