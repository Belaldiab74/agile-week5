Feature: Report a campus maintenance issue
  As a student
  I want to report a fault on campus
  So that the maintenance team can find it and arrange a repair

  Scenario: Submit a complete maintenance report
    Given a student is signed in to the campus maintenance portal
    When the student submits a report for "Engineering Building, Room 204" with the description "The ceiling light does not work"
    Then one maintenance ticket is created with status "Open"
    And the student sees its ticket reference

  Scenario: Refuse a report with no location
    Given a student is signed in to the campus maintenance portal
    When the student submits a report with description "The ceiling light does not work" and leaves the location blank
    Then the student sees "Location is required"
    And no maintenance ticket is created

  Scenario: Retry after the confirmation is lost
    Given a student's maintenance report already created an open ticket
    And the student did not receive the confirmation
    When the portal retries the same submission using the original request identifier
    Then the student sees the existing ticket reference
    And no second maintenance ticket is created
