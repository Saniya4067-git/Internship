package org.cloudbus.cloudsim.examples;

import java.util.*;

import org.cloudbus.cloudsim.*;
import org.cloudbus.cloudsim.core.CloudSim;
import org.cloudbus.cloudsim.provisioners.*;

public class SJF_Scheduling {

    public static void main(String[] args) {

        try {

            int num_user = 1;
            Calendar calendar = Calendar.getInstance();
            boolean trace_flag = false;

            CloudSim.init(num_user, calendar, trace_flag);

            Datacenter datacenter0 = createDatacenter("Datacenter_0");

            DatacenterBroker broker = new DatacenterBroker("Broker");

            int brokerId = broker.getId();

            List<Vm> vmlist = new ArrayList<Vm>();

            Vm vm = new Vm(
                    0,
                    brokerId,
                    1000,
                    1,
                    512,
                    1000,
                    10000,
                    "Xen",
                    new CloudletSchedulerTimeShared()
            );

            vmlist.add(vm);

            broker.submitVmList(vmlist);

            List<Cloudlet> cloudletList = new ArrayList<Cloudlet>();

            long[] lengths = {4000, 2000, 3000, 1000};

            for (int i = 0; i < lengths.length; i++) {

                Cloudlet cloudlet = new Cloudlet(
                        i,
                        lengths[i],
                        1,
                        300,
                        300,
                        new UtilizationModelFull(),
                        new UtilizationModelFull(),
                        new UtilizationModelFull()
                );

                cloudlet.setUserId(brokerId);

                cloudletList.add(cloudlet);
            }

            Collections.sort(cloudletList, new Comparator<Cloudlet>() {

                public int compare(Cloudlet c1, Cloudlet c2) {

                    if (c1.getCloudletLength() < c2.getCloudletLength())
                        return -1;
                    else if (c1.getCloudletLength() > c2.getCloudletLength())
                        return 1;
                    else
                        return 0;
                }
            });

            broker.submitCloudletList(cloudletList);

            CloudSim.startSimulation();

            List<Cloudlet> resultList =
                    broker.getCloudletReceivedList();

            CloudSim.stopSimulation();

            printCloudletList(resultList);

        } catch (Exception e) {

            e.printStackTrace();
        }
    }

    private static Datacenter createDatacenter(String name) {

        List<Host> hostList = new ArrayList<Host>();

        List<Pe> peList = new ArrayList<Pe>();

        peList.add(new Pe(
                0,
                new PeProvisionerSimple(1000)
        ));

        Host host = new Host(
                0,
                new RamProvisionerSimple(2048),
                new BwProvisionerSimple(10000),
                1000000,
                peList,
                new VmSchedulerTimeShared(peList)
        );

        hostList.add(host);

        DatacenterCharacteristics characteristics =
                new DatacenterCharacteristics(
                        "x86",
                        "Linux",
                        "Xen",
                        hostList,
                        10.0,
                        3.0,
                        0.05,
                        0.001,
                        0.0
                );

        Datacenter datacenter = null;

        try {

            datacenter = new Datacenter(
                    name,
                    characteristics,
                    new VmAllocationPolicySimple(hostList),
                    new LinkedList<Storage>(),
                    0
            );

        } catch (Exception e) {

            e.printStackTrace();
        }

        return datacenter;
    }

    private static void printCloudletList(List<Cloudlet> list) {

        System.out.println("\nCloudlet ID\tSTATUS\tVM ID\tTime");

        for (Cloudlet cloudlet : list) {

            System.out.println(
                    cloudlet.getCloudletId()
                    + "\tSUCCESS\t"
                    + cloudlet.getVmId()
                    + "\t"
                    + cloudlet.getActualCPUTime()
            );
        }
    }
}