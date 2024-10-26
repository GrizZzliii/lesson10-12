Feature: Cleaning program selection

  Scenario: User selects a cleaning program
    Given the user is on the room dashboard
    When the user selects a cleaning program
    Then the selected cleaning program should be active