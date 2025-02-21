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

  Example of Ansible Script:

![image](https://github.com/user-attachments/assets/640bc7a8-d38a-414e-9b1d-da94297019dc)

![image](https://github.com/user-attachments/assets/4005496d-03f0-45e2-bde5-a92496f27fd4)

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

### Example of Jenkins Pipeline with dependencies, systemd service file and configuring nginx as a reverse proxy
#### Make sure to give root pivileges to Jenkins user - mine was editing the visudo file

#### Step 1: Clone Repo:

![image](https://github.com/user-attachments/assets/b39af79f-0211-4e9e-b3f9-ca0d293e527f)

#### Step 2: Install Dependencies:

![image](https://github.com/user-attachments/assets/a80e70fa-578f-41b9-89ed-bed47f569db6)

#### Step 4: Creating SystemD file for Flask:
#### Also give the right permissions and execution rights to the folder to be accessed and used by root and nginx server

![image](https://github.com/user-attachments/assets/c9d2dd4c-57d2-45ce-8be9-b270e6a8ae07)

#### Step 5: Configuring nginx to receive requests and pass requests to flask app (reverse proxy):

![image](https://github.com/user-attachments/assets/180e69f6-71fa-4db4-ad2c-f729f592bad6)

## Lineup of app:
- Client requests http on port 80 due to nginx config
- Nginx receives requests and displays static content and any complex requests go to Gunicorn
- Gunicorn (WSGI server)  receives and uses worker processes to pass requests to flask app
- Flask app processes and executes databases queries, api calls and prepares response
- Flask uses Gunicorn to send response back to nginx
- Nginx receives the response and forwards the response to client
