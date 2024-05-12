# Tokenizer

Powód, dlaczego wybrałem użycie wyrażeń regularnych jako sposobu tokenizacji ciągów znaków, jest dość prosty. Użycie wyrażeń regularnych skraca czas wymagany na stworzenie logiki przekształcania ciągu znaków na tokeny.

Funkcja przyjmuje jako argument ciąg znaków i próbuje znaleźć wszystkie elementy, które wpasowują się do podanego wzorca. Lista wzorców jest przetwarzana przez filtr klasyfikujący znalezione wzorce.

Nie jest to sposób bez wad, ponieważ mogą zdarzyć się elementy, które nie wpasują się w wzorzec i zostaną zaklasyfikowane błędnie. Problemem jest także fakt, że w przypadku dodania kolejnego wzorca należy dodać kolejny warunek oraz wydłuża się czas na przeszukanie takeigo tekstu.
