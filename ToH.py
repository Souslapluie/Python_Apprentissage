def towers_of_Hanoi (n, src, dest, tmp) :
	if n == 1 :
		return

	towers_of_Hanoi(n-1, src, tmp, dest)
	towers_of_Hanoi(n-1, tmp, dest, src)

from time import time

for n in range(1, 64) :
	start = time()
	towers_of_Hanoi(n, 'A', 'B', 'I')
	duration = time() - start
	print(n, "->", duration, "s")
