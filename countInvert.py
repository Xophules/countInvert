# Name: Xophules
# Date: 10/15/17
# Vers: 1.0
# Desc: A divide and conquer algorithm for counting inversions and sorting

from collections import deque


def mergeandcount(lft, rgt):
	"""
		Glue procedure to count inversions between lft and rgt.
		Input: two ordered sequences lft and rgt
		Output: tuple (number inversions, sorted combined sequence)
	"""

	if lft is None:
		return 0, rgt
	if rgt is None:
		return 0, lft
	l = []
	inv = 0
	lft = deque(lft)
	rgt = deque(rgt)

	while len(rgt) != 0 or len(lft) != 0:
		if len(lft) == 0:
			l.append(rgt.popleft())
			inv = inv + 1
			continue
		if len(rgt) == 0:
			l.append(lft.popleft())
			continue

		a = rgt.popleft()
		b = lft.popleft()

		if a < b:
			l.append(a)
			lft.appendleft(b)
		else:
			print b, "conflicts with", [a] + list(rgt)
			inv = inv + len(lft)
			l.append(b)
			rgt.appendleft(a)



	#print "Inv: ", inv, "l: ", l
	return inv, l






def sortandcount(seq):
	"""
		Divide-conquer-glue method for counting inversions.
		Function should invoke mergeandcount() to complete glue step.
		Input: ordered sequence seq
		Output: tuple (number inversions, sequence)
	"""
	if len(seq) == 1:
		return 0, seq

	div = len(seq)/2
	#print div
	ra, A = sortandcount(seq[div:])
	rb, B = sortandcount(seq[:div])
	rab, seqp = mergeandcount(A,B)
	return ra+rb+rab, seqp





if __name__ == "__main__":
	seq1 = [7, 10, 18, 3, 14, 17, 23, 2, 11, 16]
	seq2 = [2, 1, 3, 6, 7, 8, 5, 4, 9, 10]
	seq3 = [1, 3, 2, 6, 4, 5, 7, 10, 8, 9]
	songs1 = [(1, "Stevie Ray Vaughan: Couldn't Stand the Weather"),
			  (2, "Jimi Hendrix: Voodoo Chile"),
			  (3, "The Lumineers: Ho Hey"),
			  (4, "Adele: Chasing Pavements"),
			  (5, "Cake: I Will Survive"),
			  (6, "Aretha Franklin: I Will Survive"),
			  (7, "Beyonce: All the Single Ladies"),
			  (8, "Coldplay: Clocks"),
			  (9, "Nickelback: Gotta be Somebody"),
			  (10, "Garth Brooks: Friends in Low Places")]
	songs2 = [(3, "The Lumineers: Ho Hey"),
			  (4, "Adele: Chasing Pavements"),
			  (2, "Jimi Hendrix: Voodoo Chile"),
			  (1, "Stevie Ray Vaughan: Couldn't Stand the Weather"),
			  (8, "Coldplay: Clocks"),
			  (6, "Aretha Franklin: I Will Survive"),
			  (5, "Cake: I Will Survive"),
			  (7, "Beyonce: All the Single Ladies"),
			  (9, "Nickelback: Gotta be Somebody"),
			  (10, "Garth Brooks: Friends in Low Places")]
	songs3 = [(1, "Stevie Ray Vaughan: Couldn't Stand the Weather"),
			  (2, "Jimi Hendrix: Voodoo Chile"),
			  (3, "The Lumineers: Ho Hey"),
			  (4, "Adele: Chasing Pavements"),
			  (6, "Aretha Franklin: I Will Survive"),
			  (5, "Cake: I Will Survive"),
			  (7, "Beyonce: All the Single Ladies"),
			  (8, "Coldplay: Clocks"),
			  (10, "Garth Brooks: Friends in Low Places"),
			  (9, "Nickelback: Gotta be Somebody")]
	print seq1
	print "# Inversions: %i\n" % sortandcount(seq1)[0]
	print seq2
	print "# Inversions: %i\n" % sortandcount(seq2)[0]
	print seq3
	print "# Inversions: %i\n" % sortandcount(seq3)[0]
	print songs1
	print "# Inversions: %i\n" % sortandcount(songs1)[0]
	print songs2
	print "# Inversions: %i\n" % sortandcount(songs2)[0]
	print songs3
	print "# Inversions: %i\n" % sortandcount(songs3)[0]
