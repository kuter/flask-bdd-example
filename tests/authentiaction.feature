# language: en

Feature: Login View
    As a user
    I want to log in

Background:
    Given authentication system

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

Scenario: Authentication with table example
    When I visit login page
    And I enter <login> into the login input
    And I enter <password> into the password input
    And I click submit button
    Then I should see <result>

    | login | password  | result        |
    | foo   | bar       | Logged in     |
    | hello | world     | Login Failed  |
