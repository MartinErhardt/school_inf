#!/usr/bin/python
#    example implementation of the mouse problem
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
def main():
	young, adult, old, steps=0,0,0,0
	print("Enter number of young mice: ")
	young=get_in()
	print("Enter number of adult mice: ")
	adult=get_in()
	print("Enter number of old mice: ")
	old=get_in()
	print("Enter steps: ")
	steps=get_in()
	mouse.add_mice(young,0)
	mouse.add_mice(adult,1)
	mouse.add_mice(old,2)
	print("young\t adult\t old\t total")
	mouse.get_mice_older_n(steps)
def get_in():
	ret=0
	try:
		ret=int(input())
	except ValueError:
		print("no valid input, please enter an integer")
		sys.exit(1)
	return ret
class mouse(object):
	mice=[[],[],[]]
	eldered_mice=[[],[],[]]
	def get_older(self,n):
		if self.status==2 or n >= round(len(mouse.mice[self.status])/((self.status+1)*2)):
			return
		eldered_mouse=mouse.new_mouse(self.status+1)
		mouse.eldered_mice[self.status+1].append(eldered_mouse)
	def reproduce_n(self,n):
		for i in range(n):
			new_mouse=young_mouse()
			mouse.mice[0].append(new_mouse)
	@staticmethod
	def add_mice(n, state):
		for i in range(n):
			mouse.mice[state].append(mouse.new_mouse(state))
	@staticmethod
	def new_mouse(state):
		if not state:
			return young_mouse()
		elif state==1:
			return adult_mouse()
		elif state==2:
			return old_mouse()
	@staticmethod
	def get_mice_older():
		for cur_mouse_list in mouse.mice:
			for cur_mouse in cur_mouse_list:
				cur_mouse.reproduce()
		mouse.count_mice()
		for cur_mouse_list in mouse.mice:
			for i, cur_mouse in enumerate(cur_mouse_list):
				cur_mouse.get_older(i)
		mouse.mice=mouse.eldered_mice[:]
		mouse.eldered_mice=[[],[],[]]
	@staticmethod
	def get_mice_older_n(gens):
		for i in range(gens):
			mouse.get_mice_older()
	@staticmethod
	def count_mice():
		print(len(mouse.mice[0]),'\t', len(mouse.mice[1]), '\t', len(mouse.mice[2]),'\t', len(mouse.mice[0])+len(mouse.mice[1])+len(mouse.mice[2]))
class young_mouse(mouse):
	def __init__(self):
		self.status=0
	def reproduce(self):
		pass
class adult_mouse(mouse):
	def __init__(self):
		self.status=1
	def reproduce(self):
		self.reproduce_n(4)
class old_mouse(mouse):
	def __init__(self):
		self.status=2
	def reproduce(self):
		self.reproduce_n(2)
main()
