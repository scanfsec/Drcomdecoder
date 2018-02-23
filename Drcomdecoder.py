#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- by:scanf -*-

class Drcomcode(object):
	def __init__(self):
		self.key = self.numericpassword("TblRefreshCurMonthServiceUse")
		self.to_text =[]

	def myindex(self,shadow):
		j = 1
		i = 1
		while True:
			j *= 2
			i = i+1
			if shadow<i:
				break
		return j

	def numericpassword(self,word):
		shift1 = 0
		shift2 = 0
		value = 0
		str_len = len(word)
		i = 0
		while True:
			ch = ord(word[i])
			value ^=ch*self.myindex(shift1)
			value ^=ch*self.myindex(shift2)
			shift1 = (shift1+7)%19
			shift2 = (shift2+13)%23
			i = i+1
			if i >= str_len:
				break
		value = (value^0x18901)%100537
		return value

	def decode(self,text):
		str_len = len(text)-1
		i = 0
		while True:
			if i>=str_len:
				break
			ch = ord(text[i])
			if (ch>=32) and (ch<=126):
				i += 1
				ch -= 32
				offset =96.0*(self.key*i%100537/100537.0)
				ch = (ch-int(offset))%95
				if ch<0:
					ch = ch+95
				ch = ch+32
				i = i-1
				self.to_text.append(chr(ch))
			i = i+1
		return self.to_text

	def encode(self,text):

		str_len = len(text)-1
		i =0
		while True:
			if i>str_len:
				break
			ch = ord(text[i])
			if (ch>=32) and (ch<=126):
				i += 1
				ch -= 32
				offset = 96.0*(self.key*i%100537/100537.0)
				ch = (ch+int(offset))%95
				ch +=32
				i -= 1
				self.to_text.append(chr(ch))
			i += 1
		self.to_text.append('a')
		return self.to_text

print ''.join(Drcomdecoder().decode("Ma"))
print ''.join(Drcomdecoder().encode('1'))


