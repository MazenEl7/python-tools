import socket
#nameEnter = input("Enter the url without www. and .com of the website to get the ip: ")
#ip = socket.gethostbyname(f"www.{nameEnter}.com")

#print(f"the ip of website is: {ip}")
#__________________________________________#
#servName = input("Enter the name of the service you want her port: ")
#portName = socket.getservbyname(servName)
#
#print(f"The port of the service {servName} is: {portName}")
#__________________________________________#
servPortName = int(input("Enter the name of the port you want her service: "))
servPort = socket.getservbyport(servPortName)
print(f"The service of the port {servPortName} is: {servPort}")
#__________________________________________#
