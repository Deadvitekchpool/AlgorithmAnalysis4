from matplotlib import pyplot

input_data = []

s = input()
with open(s) as f:
	for line in f:
		comps = line.split(',')
		x = comps[1]
		y = comps[2]
		input_data.append((x, y))

print(input_data)