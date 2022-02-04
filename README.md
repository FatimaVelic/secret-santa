# Secret Santa Generator 

## Overview
Secret Santa project is created with intention to mimic a group game of the same name. There are several versions of the game but this project
is designed to follow the basic concept of it. The project is intended to be used as fun activity for an office team and number of participants is not limited. 
Refer to *Secret Santa - documentation.docx* file for more details.

## Objectives
Web application randomly matches registered users into pairs and lists them for gift giving process. If there is an uneven number of participants,
the person without pair is listed separately. Upon login, regular participants (Employees) are informed of who their match is while Administrators 
can see and reset Santa’s list and view, create and delete users from both groups. 

Matching pairs algorithm works on following rules:
-	No person can be assigned to itself (there’s no x-x pair)
-	Once matched, the pair won’t appear more than once on the list. 
-	Person can be sorted into only one pair. (if x is matched to y, nor x nor y cannot be matched to z)

## Quick start

To get this project running, set up Python development environment and install dependencies from `requirements.txt` by running

`pip install -r requirements.txt`

Before starting, access Django Admin dashboard by enabling superuser and create groups *Administrators* and *Employees* (names are case sensitive).
