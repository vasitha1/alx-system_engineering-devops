# SE Foundations - Web Server Project  

## Overview  
This project is part of the SE Foundations course, with an average score of **94.28%**. The main objective is to configure a web server using Nginx and automate server tasks through Bash scripting.  

## Project Details  
- **Project Start Date**: January 13, 2025, 5:00 AM  
- **Project End Date**: January 15, 2025, 5:00 AM  
- **Checker Release**: January 13, 2025, 5:00 PM  
- **Auto Review Launch**: At the project deadline  

## Concepts Covered  
- Understanding child processes and their roles in web servers.  
- Configuring a web server according to specified requirements.  
- Automating server configurations using Bash scripts.  

## Background Context  
This project involves configuring a web server and writing Bash scripts to automate tasks without human intervention. The focus is on efficiency and the ability to manage multiple servers effectively.  

### Key Tasks  
1. **Transfer a File to the Server**:  
   - Write a Bash script that accepts four parameters:  
     - Path to the file  
     - Server IP  
     - Username for SCP  
     - Path to the SSH private key  
   - Ensure strict host key checking is disabled.  

2. **Install Nginx Web Server**:  
   - Create a Bash script to install Nginx, configure it to listen on port 80, and return "Hello World!" on the root page.  

3. **Setup a Domain Name**:  
   - Register a .tech domain and configure DNS records to point to the server's IP address.  

4. **Implement Redirection**:  
   - Configure Nginx to redirect `/redirect_me` to a specified URL with a 301 status code.  

5. **Custom 404 Page**:  
   - Set up a custom 404 error page that displays "Ceci n'est pas une page".  

## Learning Objectives  
By the end of this project, you should be able to explain:  
- The main role of a web server.  
- The concept of child processes.  
- The relationship between parent and child processes in web servers.  
- Main HTTP request types.  
- The role of DNS and different DNS record types (A, CNAME, TXT, MX).  

## Requirements  
- All scripts must be executable and pass Shellcheck (version 0.3.7).  
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.  
- A `README.md` file is mandatory at the root of the project folder.  
- All files should end with a new line.  

## Resources  
- [How the web works](https://www.example.com)  
- [Nginx Documentation](https://nginx.org/en/docs/)  
- [Child Process Concept](https://www.example.com)  
- [HTTP Requests](https://www.example.com)  
- [Logs Files on Linux](https://www.example.com)  

## Repository Structure  
