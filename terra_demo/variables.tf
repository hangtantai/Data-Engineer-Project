variable "project" {
  description = "Project"
  default     = "numeric-vehicle-424304-u7"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "credentials" {
  description = "Credentials"
  default     = "C:/Users/Hang Tan Tai/Documents/week_1/terra_demo/keys/my_creds.json"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My Bigquery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "numeric-vehicle-424304-u7-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}