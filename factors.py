#!/usr/bin/python3
import sys

def factorize(number):
	for i in range(2, number):
		if number % i == 0:
			return (number // i, i)
	return None
def main():
	if len(sys.argv) != 2:
		print("Usage: factors <file>")
		sys.exit(1)

	input_file = sys.argv[1]
	try:
		with open(input_file, 'r') as file:
			for line in file:
				num = int(line.strip())
				factors = factorize(num)

				if factors:
					print(f"{num}={factors[0]}*{factors[1]}")
	except (FileNotFoundError, ValueError):
		print(f"Error: File '{input_file}' not found.\n OR
			Use natural numbers")
		sys.exit(1)

if __name__ == "__main__":
	main()
