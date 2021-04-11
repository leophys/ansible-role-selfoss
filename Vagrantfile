# This guide is optimized for Vagrant 1.7 and above.
# Although versions 1.6.x should behave very similarly, it is recommended
# to upgrade instead of disabling the requirement below.
Vagrant.require_version ">= 1.7.0"

Vagrant.configure(2) do |config|

  config.vm.box = "debian/bullseye64"

  config.vm.define "debiantest" do |m|
    m.vm.hostname = "debiantest"
    m.vm.network :private_network, ip: "192.168.123.2", libvirt__dhcp_enabled: false
    m.vm.synced_folder ".", "/vagrant", disabled: true
  end
  # Disable the new default behavior introduced in Vagrant 1.7, to
  # ensure that all Vagrant machines will use the same SSH key pair.
  # See https://github.com/mitchellh/vagrant/issues/5005
  config.ssh.insert_key = false

  config.vm.provider :libvirt do |lv|
    lv.cpus = 2
    lv.memory = 1024
  end

  config.vm.provision "ansible" do |ansible|
    ansible.become = true
    ansible.verbose = "v"
    ansible.playbook = "playbook.yml"
    ansible.inventory_path = "inventory"
  end
end
