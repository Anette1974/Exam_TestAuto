@fav
  Feature: Hantera favoriter

    Scenario: Favoritmarkera böcker
      Given Jag navigerar till webbsidan "Läslistan"
      When jag är på sidan "Katalog"
      Then jag hovrar över en bok
      Then Ser jag att raden med boken ändrar färg och att det visas ett hjärta i början av raden
      Then Klickar jag på hjärtat för att favoritmärka vald bok
      Then navigerar jag till sidan "Mina böcker"
      Then kontrollerar jag att min senast favoritmarkerad bok finns i listan
