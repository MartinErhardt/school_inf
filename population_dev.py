#!/usr/bin/python
#    example implementation of the population problem
#    Copyright (C) 2014  martin.erhardt98@googlemail.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
import sys
population=[12300000,39100000,15500000,16300000]
population_change=(0.066,0.029,0.066)		# these are some constants
def calc_year():
	global population # I know, what I'm doing python
	helper	= round(population[1]*0.02) # some get born
	population[3]	= round(population[3]*0.972) # and the others die
	for i in reversed(range(0,len(population)-1,1)):	# ,someget older
		pop_change_abs		= round(population[i]*population_change[i]) # (in absolute numbers)
		population[i+1]	+= pop_change_abs
		population[i]	-= pop_change_abs
	population[0] += helper
def main(argv):
	print("year\t total\t\t young\t\t adult\t\t middle-aged\t old")
	print_pop(2005)
	try:
		for i in range(int(sys.argv[1])):
			calc_year()
			print_pop(i+2006)
	except (IndexError, ValueError) as e:
		print(e,'\n',"Please give an integral index as command line argument!")
def print_pop(i):
	print(i,'\t',sum(population),'\t',population[0],'\t',population[1],'\t',population[2],'\t',population[3])
if  __name__ =='__main__':main(sys.argv)
