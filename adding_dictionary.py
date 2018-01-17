#not mine..friend showed me this
def addition(nums, target):
	result_dict = {}
	for i in range(len(nums)):
		if nums[i] not in result_dict:
			result_dict[target - nums[i]] = i
		else:
			print (result_dict[nums[i]], i)

addition([7,10,13,55,68,8,3,2,4],17)



##wrote this up for a future project
Platforms = {}

SampleData = ["People","Dogs","People","Cats","Car","Cats",""]
SampleData2 = ["Psycho","Addict","Insane","Cats","Car","Cats",""]


for i in SampleData:
    i = i.strip()
    if i not in Platforms:
        Platforms[i] = {"assets":[i]}
    else:
        Platforms[i]["assets"].append(i)

print(Platforms)
