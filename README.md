# Exam_TestAuto

GitHub repository för att köra programmet finns på: https://github.com/Anette1974/Exam_TestAuto.git

Installera Behave, Playwright och Python 3.11

Jag har ett test för att se om webbsidan laddas samt att det går att trycka på de tre navigeringsknapparna.
Jag har testat att det går att favoritmarkera en bok och att den därefter är synlig på Mina böcker sidan.
Jag har slutligen testat att det går att lägga till en bok om båda fälten är ifyllda samt 
att det inte går att trycka på knappen Lägg till ny bok om information saknas i något av fälten.


För att köra alla tester, skriv behave .\src\ i terminalfönstret i PyCharm.

Om du endast vill köra några av testerna, använd nedanstående taggar:
Smoke test för att se om webbsidan är live: behave --tags="@smoke" .\src\
För att se om navigeringsknapparna fungerar: behave --tags="@nav" .\src\
Tester för att se om favoritmarkering av böcker fungerar: behave --tags="@fav" .\src\
Tester för att se om det går att lägga till en bok: behave --tags="@add" .\src\
