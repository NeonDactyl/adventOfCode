WIDTH = 25
HEIGHT = 6
AREA = WIDTH * HEIGHT

with open("8.in") as file:
	pixels = file.read().strip()
layers = []
final_image = [' '] * AREA
for i in range(0, int(len(pixels) / AREA)):
	current_layer = pixels[i * AREA:i * AREA + AREA]
	layers.append(current_layer)

for idx, pix in enumerate(final_image):
	for layer in layers[::-1]:
		if layer[idx] == '2':
			continue
		elif layer[idx] == '0':
			final_image[idx] = '.'
		elif layer[idx] == '1':
			final_image[idx] = '#'
		else:
			print("Serious error occured in the input. What. The. Fuck.")

for idx in range(len(final_image)):
	if idx % WIDTH == 0:
		print()
	print(final_image[idx], end='')
print()
