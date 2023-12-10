provider "google" {

  project = var.gcp-project-id
  credentials = file(var.gcp-svc-key)
  region = var.gcp-project-region
  zone = var.gcp-project-zone

}
