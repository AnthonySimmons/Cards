#!/usr/bin/python

SuitStrings = ["Spades", "Hearts", "Jacks", "Diamonds"]

class Suit:
	Val = 0
	
	def __init__(self, val):
		self.Val = val
		
	def __str__(self):
		return SuitStrings[self.Val]		

