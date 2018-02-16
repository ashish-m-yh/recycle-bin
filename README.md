# Goal

Provide a platform for consumers and producers of industrial waste to recycle waste, resulting in minimum pollution 

# Requirement

* Organization/Company registration

* Company login

* Company edit profile

* Company to specify generated and consumed wastes

* Search for waste

# Design

## Application Stack

* Python 2.x
* Flask
* Mysql
* Foundation UI framework

## Database design

### industry

Typical industries under which manufacturing industries can be categorized

### organization

Organization is company which registers on the platform and can login to connect with other waste producers

### waste_master

Master list of different kinds of wastes

### industry_waste

Mapping of industry and waste generated

### org_waste_gen

Contains details of organization waste generated (quantity and unit)

### org_waste_req

Contains details of organization waste required (quantity and unit)

## Flask Models
