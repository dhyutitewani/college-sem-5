#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"
#include "ns3/netanim-module.h"

using namespace ns3;
NS_LOG_COMPONENT_DEFINE("FirstScriptExample");

int main(int argc, char *argv[]) {
  Time::SetResolution(Time::NS);

  NodeContainer nodes; 
  nodes.Create(2);

  PointToPointHelper p2p; 
  p2p.SetDeviceAttribute("DataRate", StringValue("10Mbps")); 
  p2p.SetChannelAttribute("Delay", StringValue("2ms"));

  InternetStackHelper stack; 
  stack.Install(nodes);
  NetDeviceContainer devices = p2p.Install(nodes);

  Ipv4AddressHelper address; 
  address.SetBase("10.1.1.0", "255.255.255.0"); 
  Ipv4InterfaceContainer interfaces = address.Assign(devices);

  UdpEchoServerHelper echoServer(9); 
  ApplicationContainer serverApps = echoServer.Install(nodes.Get(1)); 
  serverApps.Start(Seconds(1.0)); 
  serverApps.Stop(Seconds(10.0));

  UdpEchoClientHelper echoClient(interfaces.GetAddress(1), 9); 
  echoClient.SetAttribute("MaxPackets", UintegerValue(4)); 
  echoClient.SetAttribute("Interval", TimeValue(Seconds(1.0))); 
  echoClient.SetAttribute("PacketSize", UintegerValue(1024));

  ApplicationContainer clientApps = echoClient.Install(nodes.Get(0)); 
  clientApps.Start(Seconds(2.0)); 
  clientApps.Stop(Seconds(10.0));

  AnimationInterface anim("1.xml"); 
  anim.SetConstantPosition(nodes.Get(0), 10.0, 10.0); 
  anim.SetConstantPosition(nodes.Get(1), 20.0, 30.0);

  if (true) PointToPointHelper().EnablePcapAll("p2p");

  Simulator::Run(); Simulator::Destroy();

  return 0;
}
