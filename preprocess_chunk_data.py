import random

def chunk_data(input_file, output_file):
	with open(input_file, "r") as f:
		lines = f.readlines()
	char_lines = []
	for line in lines:
		line = line.strip()
		characters = list(line)
		for char in characters:
			random_number = random.random()
			if random_number > 0.8:
				char_lines.append("#" + " " + "#" + " " + "B-" + char + "\n")
			else:
				char_lines.append(char + " " + char + " " + "O-" + char + "\n")
		char_lines.append("\n")
	with open(output_file, "w") as f:
		f.writelines(char_lines)

	return


def main():
	chunk_data("train_snippet.txt", "train.txt")
	return

if __name__ == "__main__":
	main()