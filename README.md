# habit-tracker
## TODO

- habit class as OOP  ✅
- define habit ✅
- periodicity habit ✅
- task can be completed at any point in time ✅
- break the habit functionality : 
  - each task has to be checked of once during defined period
  - if missed user breaks habit
- streak of x periods functionality:
  - achieved by checking of the habit a certain number of times (e.g for one/two weeks)
- habits are stored ✅ and can be analyzed 
- user gets answers to following questions: 
  - what’s my longest habit streak? 
  - What's the list of my current daily habits? 
  - With which habits did I struggle most last month?
  
### needed components:
- habit class with methods to:
  - add habit ✅
  - modify habit✅
  - delete habit✅
- analytics module:
- database✅

### Acceptance criteria
  - Python 3.7 or later ✅
  - installation and run instructions (README.md)
  - Documentation in code with docstrings
  - weekly and daily habits ✅
  - 5 predefined habits (at least one weekly/daily)
  - document how new habits can be added and completed (instruction manual)
  - each predefined habit should have example tracking data of 4 weeks
  - Testing (text fixture with the help of sample data)!
  - Storing data with JSON or SQLite ✅
  - analytics module:
    - allows user to analyze habits
    - implemented with functional programming paradigm
    - minimum requirements: 
      - return a list of all currently tracked habits, ✅
      - return a list of all habits with the same periodicity,
      - return the longest run streak of all defined habits,
      - and return the longest run streak for a given habit.
  - clean API with CLI tool for user to create, delete and analyze habits; can be done with: ✅
    - e.g. fire or click
    - built in input command to create interactive menu
    - tkinter (GUI)
    - flask or django
  - unit test suite: 
    - validity of habit tracking components
    - analytics module
    - with pytest or unittest

## User Stories

1 create, delete, modify and complete habits
2 differentiate between weekly and daily habits
3 know if i break the habit
4 analyze existing data of habits to get overview
5 see all existing habits at a glance
6 see all habits when I leave the app and come back later to keep using app over time

## Features

1 Button for each functionality 
  - Add new habit underneath table
  - modify, delete, complete button next to existing habit
2 Different table for weekly and daily habit
3 Track how often habit has been checked (7/week or 1/week otherwise broke habit)
4 Button on main page under tables to get to analytics module:
  - return the longest run streak of all defined habits,
  Button next to habit:
  - and return the longest run streak for a given habit.
5 Table on main page with all habits (point 2)
6 Database which saves currently existing habits


### Last status
- analytics functionality has to be done. 
- implemented separate weekly and daily table that can be used
- basic functionality stands
- streak functionality next 
- datetime relativedelta module could be used to track multiple days https://dateutil.readthedocs.io/en/stable/relativedelta.html#examples
- most functionality could test be done with prompts
- unit test have to be done last
- for the break the habit functionality I need the streak (compare with last date if checked) ✅
