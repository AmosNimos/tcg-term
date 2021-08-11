

# Shuffle function
def shuffle(self, x, random=None):
	"""Shuffle list x in place, and return None.

	Optional argument random is a 0-argument function returning a
	random float in [0.0, 1.0); if it is the default None, the
	standard random.random will be used.

	"""

	if random is None:
	    randbelow = self._randbelow
	    for i in reversed(range(1, len(x))):
		# pick an element in x[:i+1] with which to exchange x[i]
		j = randbelow(i+1)
		x[i], x[j] = x[j], x[i]
	else:
	    _int = int
	    for i in reversed(range(1, len(x))):
		# pick an element in x[:i+1] with which to exchange x[i]
		j = _int(random() * (i+1))
		x[i], x[j] = x[j], x[i]
    
# Randint function    
def randint(self, a, b):
	"""Return random integer in range [a, b], including both end points.
	"""

	return self.randrange(a, b+1)

# Randrange function 
def randrange(self, start, stop=None, step=1, _int=int):
        """Choose a random item from range(start, stop[, step]).

        This fixes the problem with randint() which includes the
        endpoint; in Python this is usually not what you want.

        """

        # This code is a bit messy to make it fast for the
        # common case while still doing adequate error checking.
        istart = _int(start)
        if istart != start:
            raise ValueError("non-integer arg 1 for randrange()")
        if stop is None:
            if istart > 0:
                return self._randbelow(istart)
            raise ValueError("empty range for randrange()")

        # stop argument supplied.
        istop = _int(stop)
        if istop != stop:
            raise ValueError("non-integer stop for randrange()")
        width = istop - istart
        if step == 1 and width > 0:
            return istart + self._randbelow(width)
        if step == 1:
            raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))

        # Non-unit step argument supplied.
        istep = _int(step)
        if istep != step:
            raise ValueError("non-integer step for randrange()")
        if istep > 0:
            n = (width + istep - 1) // istep
        elif istep < 0:
            n = (width + istep + 1) // istep
        else:
            raise ValueError("zero step for randrange()")

        if n <= 0:
            raise ValueError("empty range for randrange()")

        return istart + istep*self._randbelow(n)
