package org.cloudbus.cloudsim.examples;

import org.cloudbus.cloudsim.*;
import org.cloudbus.cloudsim.core.CloudSim;
import org.cloudbus.cloudsim.provisioners.*;

import java.util.*;

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

            // ================= VM LIST =================
            List<Vm> vmlist = new ArrayList<>();

            Vm vm = new Vm(
                    0, brokerId, 1000, 1,
                    512, 1000, 10000,
                    "Xen",
                    new CloudletSchedulerTimeShared()
            );

            vmlist.add(vm);
            broker.submitGuestList(vmlist);

            // ================= CLOUDLET LIST =================
            List<Cloudlet> cloudletList = new ArrayList<>();

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

            // ================= SJF SCHEDULING =================
            Collections.sort(cloudletList, new Comparator<Cloudlet>() {
                @Override
                public int compare(Cloudlet c1, Cloudlet c2) {
                    return Long.compare(c1.getCloudletLength(), c2.getCloudletLength());
                }
            });

            broker.submitCloudletList(cloudletList);

            // ================= SIMULATION =================
            CloudSim.startSimulation();

            List<Cloudlet> resultList = broker.getCloudletReceivedList();

            CloudSim.stopSimulation();

            printCloudletList(resultList);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // ================= DATACENTER =================
    private static Datacenter createDatacenter(String name) {

        List<Host> hostList = new ArrayList<>();

        List<Pe> peList = new ArrayList<>();
        peList.add(new Pe(0, new PeProvisionerSimple(1000)));

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
                        "x86", "Linux", "Xen",
                        hostList,
                        10.0, 3.0, 0.05, 0.001, 0.0
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

    // ================= OUTPUT =================
    private static void printCloudletList(List<Cloudlet> list) {

        System.out.println("\nCloudlet ID\tSTATUS\tVM ID\tTime");

        for (Cloudlet cloudlet : list) {

            System.out.println(
                    cloudlet.getCloudletId() + "\tSUCCESS\t" +
                    cloudlet.getVmId() + "\t" +
                    cloudlet.getActualCPUTime()
            );
        }
    }
}

//javaproject:CloudSimProject
//package:org.cloudbus.cloudsim.examples
//paste org to src
//cllassname:SJF_Scheduling
//runas:java application