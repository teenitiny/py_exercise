"""
File: arrayset.py
Author: Ken Lambert
"""

from arraybag import ArrayBag
from abstractset import AbstractSet

class ArraySet(ArrayBag, AbstractSet):
	"""An array-based implementation of a set."""

	def __init__(self, sourceCollection=None):
		ArrayBag.__init__(self, sourceCollection)

	def add(self, item):
		"""Adds item to the set if it is not in the set."""
		if not item in self:
			ArrayBag.add(self, item)
