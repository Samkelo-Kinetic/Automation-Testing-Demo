@login
Feature: Login

  Scenario: successful login
    Given the login page is open
     When the user logs with username "Admin" and password "admin123"
