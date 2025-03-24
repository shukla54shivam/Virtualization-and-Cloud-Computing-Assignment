import time
import psutil
from google.cloud import compute_v1

# Set up GCP Compute client
project = "vc-assignment-3"
zone = "us-central1-a"
instance_name = "auto-scale-instance"

def create_instance():
    instance_client = compute_v1.InstancesClient()
    instance = compute_v1.Instance(
        name=instance_name,
        machine_type=f"zones/{zone}/machineTypes/e2-micro",
        disks=[compute_v1.AttachedDisk(
            auto_delete=True,
            boot=True,
            initialize_params=compute_v1.AttachedDiskInitializeParams(
                source_image="projects/debian-cloud/global/images/debian-11"
            )
        )],
        network_interfaces=[compute_v1.NetworkInterface(
            name="global/networks/default"
        )]
    )
    operation = instance_client.insert(project=project, zone=zone, instance_resource=instance)
    print("Scaling to GCP... Instance creation in progress.")

while True:
    cpu_usage = psutil.cpu_percent(interval=5)
    print(f"CPU Usage: {cpu_usage}%")

    if cpu_usage > 75:
        print("High CPU detected! Scaling to GCP...")
        create_instance()
        break

    time.sleep(5)
