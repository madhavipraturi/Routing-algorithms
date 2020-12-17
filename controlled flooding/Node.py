import socket
import time

port_numbers={"10.10.10.10":31523,"10.10.10.20":32676,"10.10.10.30":33819,
	"10.10.10.40":34217,"10.10.10.50":35192,"10.10.10.60":36785,"10.10.10.70":37413}

IP_by_port={31523:"10.10.10.10",32676:"10.10.10.20",33819:"10.10.10.30",
	34217:"10.10.10.40",35192:"10.10.10.50",36785:"10.10.10.60",37413:"10.10.10.70"}



class Node:

	def __init__(self,name,IP):
		self.name=name
		self.IP=IP
		self.last_received_number={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0}
		self.address=("127.0.0.1",port_numbers.get(self.IP))
		self.mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.mysocket.bind(self.address)
		self.node_neighbor=[self.name];

	def __del__(self):
		self.mysocket.close()

	def send(self, des_node_info,packet):
		#print des_node_info.split()
		#print des_node_info.split()[0]
		receiver_address=('127.0.0.1',port_numbers.get(des_node_info.split()[0]))
		self.mysocket.sendto(packet,receiver_address)
		#print packet," destination ",des_node_info, " at:", time.time()
		time.sleep( 0.2 )


	def flood(self, packet):
		for each in self.node_neighbor:
			if len(each) > 5:
				self.send(each,packet)

	def receive(packet):
		#need to determine drop or forward
		if drop_packet(packet):
			#drop
			file = open("log.txt","a")
			file.write("\n")
			pass
		else:
			#forward
			for each in self.node_neighbor:
				if each.name is packet.source_name:
					#don't send back to the sender
					pass
				else:
					send(each,packet)






		