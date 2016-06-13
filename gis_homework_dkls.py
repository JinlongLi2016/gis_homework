def main():
	min_node = -2
	while S_set-Dealed_set:
		min_dist = 2000

		for node in (S_set - Dealed_set):
			# print node
			# time.sleep(1)
			new_dist = Dist[Dealed_list[-1]] + Cost[Dealed_list[-1]][node]
			if Dist[node]> new_dist:
				Dist[node] = new_dist
				Path[node] = Dealed_list[-1]

			if new_dist < min_dist:
				min_dist = new_dist
				min_node = node	
				# print 'minnode = ',min_node		
		if min_node == -2:
			print 'this step worng'
		else:
			Dealed_list.append(min_node)
			Dealed_set.add(min_node)
	# print Dealed_list
	# print Path
	# print Dist

def deal_node(index):
	if Cost[1][index] <500:
		return [1, index]
	else:
		return  deal_node(Path[index]) + [index]


if __name__ == '__main__':
	Cost1 = ([[1000,1000,1000,1000,1000,1000,1000],
		[1000, 0, 5, 1000, 8, 1000, 1000],
		[1000, 1000, 0, 12, 1000, 10, 1000],
		[1000, 1000, 1000, 0, 1000, 2, 13],     
		[1000, 1000, 14, 1000, 0, 21, 1000],
		[1000, 1000, 1000, 1000, 1000, 0, 9],
		[1000, 1000, 1000, 1000, 1000, 1000, 0]])
	Cost = [[1000,1000,1000,1000,1000,1000,1000],
		[1000, 0, 5, 1000, 8, 1000, 1000],
		[1000, 1000, 0, 12, 1000, 20, 1000],
		[1000, 1000, 1000, 0, 1000, 2, 13],     
		[1000, 1000, 14, 1000, 0, 21, 1000],
		[1000, 1000, 1000, 1000, 1000, 0, 9],
		[1000, 1000, 1000, 1000, 1000, 1000, 0]]
	Dealed_list = [1]
	Dealed_set = {1}
	S_set = {1,2,3,4,5,6}
	Dist = [1000, Cost[1][1], 5, 1000, 8, 1000, 1000]  # -1 represent +
	Path = [1, 1, 1, 1, 1, 1, 1]

	main()
	# newPath = Path[2:7]
	# newDist = Dist[2:7]
	# Dist_copy = copy.deepcopy(newDist)
	tpath = [0,0,0,0,0,0,0,0]
	for i in range(2,7):
		# index = Dist.index(Dist_copy[i])
		# index = Dist.index(newDist[i])
		tpath[i] = deal_node(i)
	for i in range(2, 7):
		print '1 => %d:  Min Distance = %d'%(i, Dist[i]),
		print '   Path:',tpath[i][0],
		for temp in range(1, len(tpath[i]) - 1):
			print '=>',tpath[i][temp],
		print '=>',tpath[i][len(tpath[i])-1]




	
