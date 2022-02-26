class Solution_lexicalOrder:

	def dfs(self,i,n,re):
		if i> n:
		return
		re.append(i)
		for this in range(i*10,(i+1)*10):
			self.dfs(this,n,re)

	def lexicalOrder(self, n: int) -> list:
		re = list()
		for i in range(1,10):
			self.dfs(i,n,re)
		return re
		
	def t(self):
		print(self.lexicalOrder(15))
