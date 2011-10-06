# Installation

## Vagrant installation
 * Install Vagrant: http://vagrantup.com/docs/getting-started/index.html
    - If you already have Ruby only this is required: gem install vagrant

```bash
    # Create vm (we took me 195.632511 seconds without downloading base image)
    vagrant up

    # Init admin super user
    vagrant ssh
    cd /vagrant/salesevents
    ./manage.py createsuperuser --username admin --email youremail@gmail.com
```
 * You're done. Go to http://localhost:8080/
 
 * Automatically this is done:
    - apache2, mod_wsgi, mysql, django and other python packages (PIL, memcached, mysql) are installed
    - application site configuration is enabled in apache
    - application db is installed
    - site is available at http://localhost:8080/
    - plus extra goodies offered by vagrant: folder sharing, port forwarding

## Using Django developer server
To use Django developer server you'll have to start it by hand. Port forwarding is setup automatically.

 * Start dev server

```bash
    vagrant ssh
    cd /vagrant/salesevents
    ./manage runserver 0.0.0.0:8000
```
 * Go to: http://localhost:8000/ (Is a different port)


# Opened things
 * Implement shipping methods
 * Implement item reservation
 * Implement search (haystack)
 * Implement checkout with Cybersource (Simpler Order API) - maybe
 * Implement API
