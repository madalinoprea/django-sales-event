# Installation

## Vagrant installation
 * Install Vagrant: http://vagrantup.com/docs/getting-started/index.html
    - If you already have Ruby only this is required: gem install vagrant
{{{
# Create vm (we took me 195.632511 seconds without downloading base image)
vagrant up
# Init admin super user
vagrant ssh
cd /vagrant/salesevents
./manage.py createsuperuser --username admin --email youremail@gmail.com 
# Done:
# Go to http://localhost/ (if you already have a webserver in host change port forwarding setup
# in Vagrant file and run: vagrant reload
}}}

 * Manual steps (that need to be corrected - automatically install django db)
 {{{
     ./manage.py createsuperuser --username admin --email madalinoprea@gmail.com
 }}}
 * Automatically this is done:
    - apache2, mod_wsgi, mysql, django and other python packages (PIL, memcached, mysql) are installed
    - application site configuration is enabled in apache
    - application db installed
    - site is availble at http://localhost/

# Opened things
 * Implement shipping methods
 * Implement item reservation
 * Implement search (haystack)
 * Implement checkout with Cybersource (Simpler Order API)
 * Implement API
