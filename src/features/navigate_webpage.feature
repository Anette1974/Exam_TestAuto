@nav


  Feature: Navigera på webbsidan

    Scenario: Navigera till de olika sidorna "Lägg till bok", "Mina böcker" och "Katalog"
      Given Jag navigerar till webbsidan "Läslistan"
      When jag klickar på knappen "Lägg till bok"
      Then ska knappen "Lägg till bok" ändra färg och inte gå att klicka på
      And jag klickar på knappen "Mina böcker"
      And ska knappen "Mina böcker" ändra färg och inte gå att klicka på
      And jag klickar på knappen "Katalog"
      And ska knappen "Katalog" ändra färg och inte gå att klicka på