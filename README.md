# tokenizer
tokenizer

Powód dlaczego wybrałem użycie regex jakos oposób tokenizacji ciągów znaków jest dość prosty.
Użycie regex'a skraca czas wymagany na stworzenie logiki przerabiania ciągu znaków na tokeny.

Funkcja przyjmuje jako argument ciąg znaków i próbuje znaleźć wszystkie elementy, które wpasowują
się do podanego wzorca. Lista wzorców przetwarzana jest przez filtr klasyfikujący znaleziony wzorzec.

Nie jest to sposób bez wad bo mogą zdarzyś się elementy, które nie wpasują sie we wzorzec i zostanie
zaklasyfikowany błędnie. Problemem jest też fakt, że w przypadku dodania kolejego wzorca 
wydłuży się czas wyszukiwania.
