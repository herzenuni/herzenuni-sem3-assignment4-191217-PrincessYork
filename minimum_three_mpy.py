def minimum_three_mpy(*args):
	if len(args) < 3:
		print("minimum_three_mpy : 3 arguments minimum")
		return None

	try:
		mpy = args[0] * args[1] * args[2]
		counter = 0
		for i in range(len(args)):
			for j in range(i + 1, len(args)):
				for k in range(j + 1, len(args)):
					counter += 1
					new_mpy = args[i] * args[j] * args[k]
					print("[", counter, "] args : ", args[i], " ", args[j], " ", args[k], "new_mpy : ", new_mpy)
					if new_mpy < mpy:
						mpy = new_mpy
						print("[", counter, "] update mpy : ", mpy)
		return mpy
	except TypeError as ex:
		print(ex)
		return None

if __name__ == "__main__":
	print("minimum mpy of 1,2,3,4,5,6 : ", minimum_three_mpy(1,2,3,4,5,6))