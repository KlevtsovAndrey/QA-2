Feature: steps

Scenario: Creating and checking new task
 Given Create and check new task "http://qa-assignment.oblakogroup.ru/board/:Klevtsov_Andrey-BBD"

Scenario: Creating an empty task
  Given Create an empty task "http://qa-assignment.oblakogroup.ru/board/:Klevtsov_Andrey-BBD"

Scenario: Creating new category
  Given Creating new category "http://qa-assignment.oblakogroup.ru/board/:Klevtsov_Andrey-BBD"

Scenario: Validating checkbox
  Given Validating checkbox "http://qa-assignment.oblakogroup.ru/board/:Klevtsov_Andrey-BBD"
