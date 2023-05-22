#!/bin/bash

# Vérification des paramètres
if [[ $# -ne 5 ]]; then
  echo "Usage: $0 <hostname> <interface> <ip_address> <gateway_address> <dns_address>"
  exit 1
fi

# Assignation des variables
HOSTNAME=$1
INTERFACE=$2
IP_ADDRESS=$3
GATEWAY_ADDRESS=$4
DNS_ADDRESS=$5

# Étape 1 : Affectation du nom de l'hôte
hostnamectl set-hostname $HOSTNAME
if [[ $? -ne 0 ]]; then
  echo "Erreur lors de l'affectation du nom de l'hôte."
  exit 1
fi

# Étape 2 : Vérification de l'existence de l'interface réseau
if ! ip link show $INTERFACE &> /dev/null; then
  echo "Interface réseau $INTERFACE introuvable."
  exit 1
fi

# Étape 3 : Désactivation de la carte réseau
ip link set $INTERFACE down
if [[ $? -ne 0 ]]; then
  echo "Erreur lors de la désactivation de l'interface réseau $INTERFACE."
  exit 1
fi

# Étape 4 : Modification de l'adresse de la carte réseau
ip addr flush dev $INTERFACE
ip addr add $IP_ADDRESS dev $INTERFACE
if [[ $? -ne 0 ]]; then
  echo "Erreur lors de la modification de l'adresse de l'interface réseau $INTERFACE."
  exit 1
fi

# Étape 5 : Activation de l'interface réseau
ip link set $INTERFACE up
if [[ $? -ne 0 ]]; then
  echo "Erreur lors de l'activation de l'interface réseau $INTERFACE."
  exit 1
fi

# Activation du service réseau si nécessaire
systemctl is-active --quiet network || systemctl start network

# Étape 6 : Modification de l'adresse du DNS
echo "nameserver $DNS_ADDRESS" > /etc/resolv.conf
if [[ $? -ne 0 ]]; then
  echo "Erreur lors de la modification de l'adresse du DNS."
  exit 1
fi

# Étape 7 : Test de connexion au réseau
if ! ping -c 1 $GATEWAY_ADDRESS &> /dev/null; then
  echo "Impossible de se connecter à la passerelle $GATEWAY_ADDRESS."
  exit 1
fi

echo "Configuration de la machine terminée avec succès."
exit 0
