Feature: Schedule configuration

  Scenario: User configures a cleaning schedule
    Given the user is on the cleaning program page
    When the user sets a cleaning schedule
    Then the schedule should be saved successfully