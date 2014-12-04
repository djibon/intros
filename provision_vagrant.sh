#!/bin/bash
echo "I am setting things up within Vagrant..."
apt-get update
echo "Installing postgres and mysql because you might have a different preference than I do"
debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password password password'
debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password_again password password'
apt-get install -y libmysqlclient-dev mysql-server-5.5 postgresql python-dev python-pip screen vim-nox zsh git-core
mysqladmin -u root --password=password create intros
mysql -u root --password=password -e "GRANT ALL ON intros.* TO 'intros'@'localhost' IDENTIFIED BY 'intros';"
cd /vagrant
./provision.sh
date > /etc/vagrant_provisioned_at
echo "deb http://www.rabbitmq.com/debian/ testing main" >> /etc/apt/sources.list
wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
sudo apt-key add rabbitmq-signing-key-public.asc
apt-get install -y rabbitmq-server
