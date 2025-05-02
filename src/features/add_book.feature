@wip

  Feature: Lägga till bok

    Scenario: Lägga till bok, både titel och författare ifyllda
      Given Jag navigerar till webbsidan "Läslistan"
      When Jag klickar på knappen "Lägg till bok"
      Then Jag klickar på fältet "Titel" och lägger till en boktitel
      And Jag klickar på fältet "Författare" och lägger till bokens författare
      And Jag klickar på knappen "Lägg till ny bok"
      And jag klickar på knappen "Katalog"
      And jag verifierar att boken finns med som jag precis skapade

    Scenario: Lägga till bok, endast titel ifylld
      Given Jag navigerar till webbsidan "Läslistan"
      When Jag klickar på knappen "Lägg till bok"
      Then Jag klickar på fältet "Titel" och lägger till en boktitel
      And Det ska inte gå att klicka på knappen "Lägg till ny bok"

    Scenario: Lägga till bok, endast titel ifylld
      Given Jag navigerar till webbsidan "Läslistan"
      When Jag klickar på knappen "Lägg till bok"
      Then Jag klickar på fältet "Författare" och lägger till bokens författare
      And Det ska inte gå att klicka på knappen "Lägg till ny bok"