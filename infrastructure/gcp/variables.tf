variable "gke_username" {
  default     = "Cleyber"
  description = "gke username"
}

variable "gke_password" {
  default     = "y%X$Ipjg!b7Z" # usar o site https://www.lastpass.com/pt/features/password-generator
  description = "gke password"
}

variable "gke_num_nodes" {
  default     = 2
  description = "number of gke nodes"
}

variable "project_id" {
  default     = "edc-desafio-igti"
  description = "project id"
}

variable "region" {
  default     =  "us-east1"
  description = "region"
}

variable "member"{
    default     = "cleyber.cabral@gmail.com" 
    description = "IAM member"
}

variable "name" {
  default     = "desafio-igti"
  description = "The name of the bucket."
  type        = string
}

variable "location" {
  description = "The location of the bucket."
  default     = "us-east1-b"
  type        = string
}