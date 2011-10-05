require_recipe "apt"
require_recipe "mysql"
require_recipe "mysql::server"
require_recipe "apache2"
require_recipe "apache2::mod_wsgi"
# require_recipe "apache2::#{node[:django][:web_server]}"
require_recipe "git"
require_recipe "memcached"
require_recipe "python"

# disable default website
execute "disable-default-site" do
    command "sudo a2dissite default"
    notifies :restart, resources(:service => "apache2")
end

apache_module "wsgi" do
  enable true
end

# Install required packages
%w{python-mysqldb python-memcache python-imaging}.each do |pkg|
  package pkg do
    action :install
  end
end

# TODO: parametrize all these execute commands
execute "create-app-db" do
    command "mysql -uroot -p#{node[:mysql][:server_root_password]} -e 'CREATE DATABASE IF NOT EXISTS salesevents'"
end


# Install app requirements
execute "install-app-reqs" do
    command "sudo pip install -r requirements.txt"
    cwd "/vagrant"
end

# Sync db
execute "sync-db" do
    cwd "/vagrant/salesevents"
    command "python manage.py syncdb --noinput"
end

# Init static directory
directory "/vagrant/salesevents/static" do
  mode "0755"
  action :create
end

execute "app-collect-static" do
    cwd "/vagrant/salesevents"
    command "python manage.py collectstatic --noinput"
end

# Run dev server
#execute "run-dev-server" do
#    cwd "/vagrant/salesevents"
#    command "python manage.py runserver 0.0.0.0:8081 &"
#end

# Add application site configuration
web_app "application" do
    template "application.conf.erb"
    notifies :restart, resources(:service => "apache2")
end

