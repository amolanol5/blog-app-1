provider "aws" {

}



terraform {

  cloud {
    organization = "development-andres"

    workspaces {
      name = "Workspace-DNS-prod"
    }
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.11.0"
    }
  }
}