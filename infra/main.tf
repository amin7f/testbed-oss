terraform {
  required_version = ">= 1.6.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "= 4.81.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = "rg-security-testbed"
  location = "westeurope"
}

# ID: I-03
resource "azurerm_storage_account" "assets" {
  name                              = "sttestbedassets"
  resource_group_name               = azurerm_resource_group.main.name
  location                          = azurerm_resource_group.main.location
  account_tier                      = "Standard"
  account_replication_type          = "LRS"
  https_traffic_only_enabled        = true
  min_tls_version                   = "TLS1_2"
  infrastructure_encryption_enabled = true
  public_network_access_enabled     = true
  allow_nested_items_to_be_public   = true
}

resource "azurerm_storage_container" "media" {
  name                  = "media"
  storage_account_id    = azurerm_storage_account.assets.id
  container_access_type = "blob"
}

# ID: I-04
resource "azurerm_network_security_group" "app" {
  name                = "nsg-testbed-app"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name

  security_rule {
    name                       = "ssh"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

# ID: I-05
resource "azurerm_storage_account" "exports" {
  name                              = "sttestbedexports"
  resource_group_name               = azurerm_resource_group.main.name
  location                          = azurerm_resource_group.main.location
  account_tier                      = "Standard"
  account_replication_type          = "LRS"
  https_traffic_only_enabled        = false
  min_tls_version                   = "TLS1_2"
  infrastructure_encryption_enabled = true
  public_network_access_enabled     = false
  allow_nested_items_to_be_public   = false
}

# ID: I-07
resource "azurerm_storage_account" "archive" {
  name                              = "sttestbedarchive"
  resource_group_name               = azurerm_resource_group.main.name
  location                          = azurerm_resource_group.main.location
  account_tier                      = "Standard"
  account_replication_type          = "LRS"
  https_traffic_only_enabled        = true
  min_tls_version                   = "TLS1_2"
  infrastructure_encryption_enabled = true
  public_network_access_enabled     = false
  allow_nested_items_to_be_public   = false
}

resource "azurerm_storage_container" "records" {
  name                  = "records"
  storage_account_id    = azurerm_storage_account.archive.id
  container_access_type = "private"
}
