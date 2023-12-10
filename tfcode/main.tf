
resource "google_compute_instance" "my_test_vm" {
  
  name = var.instancename
  machine_type = "f1-micro"
  zone = var.gcp-project-zone

  boot_disk {
    initialize_params {
      image = "centos-7-v20210420"
    }
  }

  network_interface {
    network = "default"
    access_config{
        //
    }
  }
}