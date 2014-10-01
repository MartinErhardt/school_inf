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
	young=get_in("Enter number of young mice: ")
	adult=get_in("Enter number of adult mice: ")
	old=get_in("Enter number of old mice: ")
	steps=get_in("Enter steps: ")
	Mouse.add_mice(young,0)
	Mouse.add_mice(adult,1)
	Mouse.add_mice(old,2)
	print("young\t adult\t old\t total")
	Mouse.get_mice_older_n(steps)
def get_in(msg):
	ret=0
	try:
		ret=int(input(msg))
	except ValueError:
		print("no valid input, please enter an integer")
		sys.exit(1)
	return ret
class Mouse:
	mice=[[],[],[]]
	eldered_mice=[[],[],[]]
	def get_older(self,n):
		if self.state==2 or n >= round(len(Mouse.mice[self.state])/((self.state+1)*2)):
			return
		eldered_mouse=Mouse.new_mouse(self.state+1)
		Mouse.eldered_mice[self.state+1].append(eldered_mouse)
	def reproduce_n(self,n):
		for i in range(n):
			new_mouse=YoungMouse()
			Mouse.mice[0].append(new_mouse)
	@staticmethod
	def add_mice(n, state):
		for i in range(n):
			Mouse.mice[state].append(Mouse.new_mouse(state))
	@staticmethod
	def new_mouse(state):
		if not state:
			return YoungMouse()
		elif state==1:
			return AdultMouse()
		elif state==2:
			return OldMouse()
	@staticmethod
	def get_mice_older():
		for cur_mouse_list in Mouse.mice:
			for cur_mouse in cur_mouse_list:
				cur_mouse.reproduce()
		Mouse.count_mice()
		for cur_mouse_list in Mouse.mice:
			for i, cur_mouse in enumerate(cur_mouse_list):
				cur_mouse.get_older(i)
		Mouse.mice=Mouse.eldered_mice[:]
		Mouse.eldered_mice=[[],[],[]]
	@staticmethod
	def get_mice_older_n(gens):
		for i in range(gens):
			Mouse.get_mice_older()
	@staticmethod
	def count_mice():
		print(len(Mouse.mice[0]),'\t', len(Mouse.mice[1]), '\t', len(Mouse.mice[2]),'\t', len(Mouse.mice[0])+len(Mouse.mice[1])+len(Mouse.mice[2]))
class YoungMouse(Mouse):
	def __init__(self):
		self.state=0
	def reproduce(self):
		pass
class AdultMouse(Mouse):
	def __init__(self):
		self.state=1
	def reproduce(self):
		self.reproduce_n(4)
class OldMouse(Mouse):
	def __init__(self):
		self.state=2
	def reproduce(self):
		self.reproduce_n(2)
if  __name__ =='__main__':main()
