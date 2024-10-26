Feature: Room selection

  Scenario: User selects a room for cleaning
    Given the user is logged in
    When the user selects a room from the list
    Then the selected room should be displayed in the dashboard