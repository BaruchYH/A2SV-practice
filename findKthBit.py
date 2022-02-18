def findKthBit(self, n: int, k: int) -> str:
		s = "0"
		while len(s) < k:
			s += "1"
			for i in range(len(s) - 2, -1, -1):
				if s[i] == "0":
					s += "1"
				else:
					s += "0"
		return s[k - 1]
