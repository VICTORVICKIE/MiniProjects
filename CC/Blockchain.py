from hashlib import sha256



def update_hash(*args):      #hashes the data
	hashing_text = ''
	h = sha256()
	for arg in args:
		hashing_text += str(arg)
		
	h.update(hashing_text.encode('utf-8'))
	return h.hexdigest()


class Block():
	data  = None
	has   = None 
	nonce = 0
	previous_hash = "0" * 64

	def __init__(self,data,number=0):
		self.data = data
		self.number = number

	def hash(self):        # calls hash_func 
		return	update_hash(self.previous_hash, self.number, self.data, self.nonce)
	
	def __str__(self):		#magical str method
		return str(f"Block# : {self.number} \nhash : {self.hash()} \nprevious_hash : {self.previous_hash} \nData : {self.data} \nNonce : {self.nonce} \n")



class Blockchain():
	difficulty = 4     #Difficulty level higher the difficulty higher the time takes to mine

	def __init__(self,chain=[]):
		self.chain = chain

	def add_block(self, block):
		self.chain.append(block)

	def remove_block(self, block):
		self.chain.remove(block)

	def mine(self, block):
		try:
			block.previous_hash = self.chain[-1].hash()
		except IndexError:
			pass


		while True:
			if block.hash()[:self.difficulty] == "0" * self.difficulty:
				self.add_block(block)
				break

			else:
				block.nonce += 1
	
	def isValid(self):
		for i in range(1,len(self.chain)):
			_previous = self.chain[i].previous_hash
			_current = self.chain[i-1].hash()

			if _previous != _current or _current[:self.difficulty] != "0" * self.difficulty:
				return False
		return True	




def main():
	blockchain = Blockchain()
	database = ["VICTOR","Y","rs.x","6pm"]

	n = 0
	for data in database:
		n += 1
		blockchain.mine(Block(data,n))
	for block in blockchain.chain:
		print(block)
		
	#blockchain.chain[2].data = "NeW DaTa" 	#try tampering data
	#blockchain.mine(blockchain.chain[2])	#    ""

	print(blockchain.isValid())


if __name__ == '__main__':
	main()
	