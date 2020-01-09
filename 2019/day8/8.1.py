width = 25
height = 6
area = width * height

with open("8.in") as file:
	pixels = file.read().strip()
min_zeroes = area
result = 0
print(len(pixels) / area)
for i in range(0, int(len(pixels) / area)):
	current_layer = pixels[i * area:i * area + area]
	zeroes = current_layer.count('0')
	if zeroes < min_zeroes:
		min_zeroes = zeroes
		result = current_layer.count('1') * current_layer.count('2')
print(result)
