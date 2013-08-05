# -*- mode: ruby -*-
# vi: set ft=ruby :

BASE_BOX = ENV['BI_VAGRANT_BOX'] || 'precise64'
VAGRANT_BOX_URL = ENV['BI_VAGRANT_URl'] || "http://files.vagrantup.com/#{BASE_BOX}.box"
CHEF_PATH = ENV['BI_CHEF_PATH'] || '~/.kitchen'		#path to the believe chef-repo
USER = ENV['BI_CHEF_USER'] || ENV['USER']
CLIENT = "croydev"
PROJECT = "restorrent"



Vagrant::Config.run do |config|

  config.vm.define :web do |web_config|
    web_config.vm.box = BASE_BOX
    web_config.vm.box_url = VAGRANT_BOX_URL
    web_config.vm.host_name = "dev.believe.in"
    #web_config.ssh.private_key_path = "~/.ssh/id_rsa"

    # Do not Change - Folder shareing
    web_config.vm.share_folder("v-root", "/home/vagrant/www/#{PROJECT}", ".", :nfs => true, :create => true)
    web_config.vm.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/v-root", "1"]

    web_config.vm.network :hostonly, "192.168.100.101"
    web_config.vm.forward_port 9000, 8080

    web_config.provision :shell,
        :inline => "mkdir -p /home/vagrant/data"

    web_config.vm.provision :chef_solo do |chef|

      chef.node_name = "#{USER}-vagrant-#{PROJECT}"
      chef.cookbooks_path = ["#{CHEF_PATH}/cookbooks"]
      chef.roles_path = "#{CHEF_PATH}/roles/"
      chef.data_bags_path = "#{CHEF_PATH}/data_bags/"
      chef.run_list = [
      	"apt",
      	"runit",
      	"python",
      	"postgresql::contrib",
      	"postgresql::server",
      	"postgresql::client",
      	"believein-base",
      	"believein-base::directories",
      	"nginx::source",
      	"redis",
      	"redis::source",
      	"believein-platform",
      ]
      chef.provisioning_path = "/etc/chef"
      chef.log_level = :debug
      chef.json = {
      	:base => {
      		:user => "vagrant",
      		:group => "vagrant"
      	},
        :elasticsearch => {},
      	:believein_platform => {
      		:python => {
      			:create_venv => "true",
      			:virtual_env_name => "croydev-restorrent",
      			:virtual_env_dir => "/home/vagrant/data/python-virtualenvs/",
      		},
      	},
      	:authorization => {
      		:sudo => {
      			:groups => ["admin", "sysadmin"],
      			:users => ["vagrant"],
      			:passwordless => true
      		}
      	},
        :nginx => {
            :default_site_enabled => false,
            :source => {
                :modules => ["http_gzip_static_module", "http_ssl_module"],
            },
            :init_style => "upstart",
            :version => "1.3.15"
        },
      	:postgresql => {
      		:users => [
      			{
      				:username  => "root",
      				:password  => "root",
      				:superuser => true,
      				:createdb  => true,
      				:login     => true
      			}
      		],
      		:databases => [
      			{
      				:name => "restorrent",
      				:owner  => "root",
      				:template  => "template0",
      				:encoding  => "utf8",
      				:locale => "en_US.UTF8",
      			},
      		]
      	}
      }
    end
  end

end
