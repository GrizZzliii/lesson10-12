Feature: View cleaning statistics

  Scenario: User views cleaning statistics
    Given the user is on the dashboard
    When the user clicks on the statistics button
    Then the cleaning statistics should be displayed