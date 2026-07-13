## Inventory service

## Objective
This service is in changer of any inventory-related operations, from reading, writing, updating, storing, reviewing, etc.

## Underlying mechanism
This is a multi-stage docker-based service. It uses uv internally as a package manager in the builder stage of the image to create the virtual env and a **system-managed** python 3.13 version in the second build stage of the image to point the python path to this virtual env which already has all the dependencies installed on it to run the application inside the container. 
