#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"
#include "ns3/netanim-module.h"

using namespace ns3;

NS_LOG_COMPONENT_DEFINE("FSE");

int main(int argc, char *argv[]) {
    Time::SetResolution(Time::NS);
    LogComponentEnable("UdpEchoClientApplication", LOG_LEVEL_INFO);
    LogComponentEnable("UdpEchoServerApplication", LOG_LEVEL_INFO);

    NodeContainer n;
    n.Create(2);

    PointToPointHelper p2p;
    p2p.SetDeviceAttribute("DataRate", StringValue("10Mbps"));
    p2p.SetChannelAttribute("Delay", StringValue("2ms"));

    NetDeviceContainer d = p2p.Install(n);
    InternetStackHelper().Install(n);

    Ipv4InterfaceContainer i = Ipv4AddressHelper("10.1.1.0", "255.255.255.0").Assign(d);

    UdpEchoServerHelper(9).Install(n.Get(1)).Start(Seconds(1.0)).Stop(Seconds(10.0));

    UdpEchoClientHelper(i.GetAddress(1), 9).SetAttribute("MaxPackets", UintegerValue(4))
        .SetAttribute("Interval", TimeValue(Seconds(1.0))).SetAttribute("PacketSize", UintegerValue(1024))
        .Install(n.Get(0)).Start(Seconds(2.0)).Stop(Seconds(10.0));

    AnimationInterface("1.xml").SetConstantPosition(n.Get(0), 10.0, 10.0).SetConstantPosition(n.Get(1), 20.0, 30.0);

    if (true) PointToPointHelper().EnablePcapAll("p2p");

    Simulator::Run();
    Simulator::Destroy();

    return 0;
}

