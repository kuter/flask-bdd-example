# language: en

Feature: Login View
    As a user
    I want to log in

Scenario: Successul path
    Given existing user "foo" with password "bar"
    When I visit login page
    And I enter "foo" into the "login" input
    And I enter "bar" into the "password" input
    And I click submit button
    Then I should see "Logged in"

Scenario: Invalid login
    When I visit login page
    And I enter "hello" into the "login" input
    And I enter "world" into the "password" input
    And I click submit button
    Then I should see "Login Failed"
