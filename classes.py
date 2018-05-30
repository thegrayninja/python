class IPAddress:
    IPAddy = ""
    NetMask = ""
    Gateway = ""
    def description(self):
        desc_str = "IP: {}\nMask: {}\nGateway {}".format(self.IPAddy, self.NetMask, self.Gateway)
        return desc_str


Apple = IPAddress()
Apple.IPAddy = "10.10.0.1"
Apple.NetMask = "255.255.255.0"
Apple.Gateway = "10.10.0.254"


Banana = IPAddress()

Banana.IPAddy = "192.168.0.24"
Banana.NetMask = "255.255.0.0"
Banana.Gateway = "192.168.255.254"

print(Apple.description())
print(Banana.description())
