# GeminiFlaskAppWithAnsible

This project is a Flask-based web application that integrates the Gemini API. It is deployed using Gunicorn as a WSGI server and Nginx as a reverse proxy. Jenkins automates the build and deployment process from GitHub, while Ansible Playbooks are used to pre-install and configure required services across different VMs.

## Technologies Used
- **Flask** – Web framework for Python  
- **Gunicorn** – WSGI HTTP server for running the Flask app  
- **Nginx** – Reverse proxy to handle requests  
- **Jenkins** – Automates deployment from GitHub  
- **MySQL** – Database management  
- **Ansible** – Configuration management and automation  
- **Google Gemini API** – AI-powered API integration  

## Overall Steps Taken
### Created Flask App with Gemini Integration, Shows Disk,Network,Memory Usage of System
### Used Ansible to install NGINX (web server for hosting) on Virtual Machine(VM) 1 and another VM with SQL Server
##### Can be done without ansible
- `yum install nginx`
- `yum install mysql-server`
##### Need to configure mysql 

### System Installations on VM that has NGINX
##### Can be written in Jenkins pipeline too
- `yum install python3 python3-pip`
- `pip install google`
- `pip3 install -U google-generativeai`
- `pip3 install python-dotenv`
- `pip3 install psutil`
- `pip3 flask gunicorn`
  
### Created a Systemd Service File for Flask App
### Configure Nginx as a Reverse Proxy for Flask Application
