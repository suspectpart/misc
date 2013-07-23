#!/usr/bin/python

import sys

def rule(i):
	return "".join(reversed(list("{0:08b}".format(i)))) # 00111001 becomes [1,0,0,1,1,1,0,0], so that rule[1], rule[2].. work 
	
def cellular_automaton(generation_zero, rule, max_generations):
	generations = evolve_all(generation_zero, rule, max_generations)
	width = len(generations[-1])

	for i, generation in enumerate(generations):
		padded_zeros = (width - len(generation)) / 2
		padded_generation = "0" * padded_zeros + generation + "0" * padded_zeros
		print "".join(map(str, padded_generation)).replace("0", " ").replace("1", "X")

def evolve_all(generation_zero, rule, max_generation):
	generations = [generation_zero]
	for i in range(max_generation):
		generations.append(evolve(generations[i], rule))
	return generations

def evolve(generation, rule):
	next_generation = ""
	generation = "00" + generation + "00"
	for i, cell in enumerate(generation[1:-1]):
		left_neighbour, right_neighbour = str(generation[i]), str(generation[i+2])
		binary_value_of_cell = int(left_neighbour + cell + right_neighbour, 2) 
		next_generation += rule[binary_value_of_cell]	
	return next_generation

if __name__ == "__main__":
	generation_zero = str(sys.argv[1])
	r = rule(int(sys.argv[2]))
	max_generation = int(sys.argv[3])
	cellular_automaton(generation_zero, r, max_generation)