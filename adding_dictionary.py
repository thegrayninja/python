def addition(nums, target):
	result_dict = {}
	for i in range(len(nums)):
		if nums[i] not in result_dict:
			result_dict[target - nums[i]] = i
		else:
			print (result_dict[nums[i]], i)

addition([7,10,13,55,68,8,3,2,4],17)
