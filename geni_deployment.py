import mycontext
import geni.rspec.pg as PG
import geni.aggregate.instageni as IG
import geni.rspec.egext as EGX
import geni.rspec.igext as IGX
import geni.util

def software(i):
    dic = {}
    dic['pegasus'] = "http://###/downloads/install-pegasus.tar.gz"
    dic['apache'] = "http://###/downloads/install-apache.tar.gz"
    dic['mysql'] = "http://###/downloads/install-mysql.tar.gz"
    if i in dic:
        return dic[i]


def cluster (N_NODES, AM, SLICE_NAME, NODE_NAME, XML_NAME, SOFTWARE, PUBLIC_IP):
  	rspec = PG.Request()
  	IFACE = "if%d"
  	INSTALL  = "install-%s"
	  for i in range (0, N_NODES):
		    if i == 0:
			      vm = IGX.XenVM("master")
			      vm.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU14-64-STD"
			      rspec.addResource(vm)
			      vm.routable_control_ip = PUBLIC_IP
            if N_NODES > 1:
                vm_iface = vm.addInterface(IFACE % i)
                link = PG.LAN("lan0")
                link.addInterface(vm_iface)
	    	else:
			      vm = IGX.XenVM(NODE_NAME % (i-1))
            vm.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU14-64-STD"
            rspec.addResource(vm)
            vm_iface = vm.addInterface(IFACE % i)
            link.addInterface(vm_iface)

        for i in SOFTWARE:   #  /bin/bash
          vm.addService(PG.Install(url=software(i), path="/tmp"))
          vm.addService(PG.Execute(shell="/bin/bash", command = "sudo sh /tmp/%s"%INSTALL%i+".sh"))
       
	  if N_NODES > 1:
		    rspec.addResource(link)
	

	  #Deploy resources at GENI
    manifest = AM.createsliver(context, SLICE_NAME, rspec)
    geni.util.printlogininfo(manifest = manifest)

	  #Create manifest in XML file
	  rspec.writeXML(XML_NAME)

def deletesliver(AM, SLICE_NAME):
	  AM.deletesliver(context, SLICE_NAME)

if __name__ == '__main__':

    context = mycontext.buildContext()

    N_NODES = 2
    AM = IG.Chicago
    SLICE_NAME = "slice-test"
    NODE_NAME = "node%d" 
    XML_NAME = "manifest_test.xml"
    SOFTWARE = ['apache','mysql']
    PUBLIC_IP = False

    cluster(N_NODES, AM, SLICE_NAME, NODE_NAME, XML_NAME, SOFTWARE, PUBLIC_IP)

    #delete sliver
    #deletesliver(AM, SLICE_NAME)
