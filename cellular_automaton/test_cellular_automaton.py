#!/usr/bin/zsh	

from cellular_automaton import *
from nose.tools import *

def test_rule():
	assert_equal(rule(0), "00000000")
	assert_equal(rule(1), "10000000")
	assert_equal(rule(2), "01000000")
	assert_equal(rule(3), "11000000")
	assert_equal(rule(15), "11110000")
	assert_equal(rule(255), "11111111")

def test_evolve_one_generation():
	assert_equal(evolve("1", "01111000"), "111")
	assert_equal(evolve("010", "01111000"), "01110") # -> rule[000b = 0d] rule[001b = 1d] rule[010b = 2d] ...
	assert_equal(evolve("111", "10101010"), "00011") # -> rule[001] rule[011] rule[111] rule[110] rule[100]

def test_evolve_multiple_generations():
	rule = "10101010"
	generation_zero = "010"
	generation_one = evolve(generation_zero, rule)
	generation_two = evolve(generation_one, rule)
	generation_three = evolve(generation_two, rule)

	assert_equal(evolve_all(generation_zero, rule, 3), [generation_zero, generation_one, generation_two, generation_three])