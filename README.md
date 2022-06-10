# Skroutz Plus Savings Estimate

Ένα απλό script γραμμένο σε python ώστε να υπολογίσουμε τα κέρδη μας χρησιμοποιώντας την συνδρομή Skroutz Plus.

- Υπολογισμός των μεταφορικών που έχουμε γλυτώσει με την ΝΕΑ συνδρομή των 17 ευρώ.
(Πλήθος αντικειμένων που είναι από και άνω των 20 ευρώ επί 3 ευρώ για μεταφορικά, μείων τα 17 ευρώ της συνδρομής)
- Υπολογισμός των μεταφορικών που έχουμε γλυτώσει με την ΝΕΑ συνδρομή των 20 ευρώ.
(Πλήθος αντικειμένων που είναι από και άνω των 20 ευρώ επί 3 ευρώ για μεταφορικά, μείων τα 20 ευρώ της συνδρομής)
- Υπολογισμός (πρόχειρη εκτίμηση) των μεταφορικών που έχουμε γλυτώσει με την ΑΡΧΙΚΗ συνδρομή των 17 ευρώ. 
(Συνολικό κόστος αντικειμένων επί 3 ευρώ για μεταφορικά, μείων τα 17 ευρώ της συνδρομής)

    (Στις νέες συνδρομές παραλείπτω τις περιπτώσεις του να βάλουμε αντικείμενα από ίδιο κατάστημα για να φτάσουμε τα 20 ευρώ. Πιάνω την χειρότερη περίπτωση.)

## Εγκατάσταση
Μια σύγχρονη έκδοση Python(3.5+).

Τον Chrome εγκατεστημένο με κλειστά τα tabs του.

```sh
pip install selenium
pip install webdriver_manager
```
ή
```sh
pip install -r requirements.txt
```
Τέλος για να ξεκινήσει
```sh
python skroutz_plus.py
```

Το script κάνει χρήση του selenium στον προσωπικό μας Chrome ώστε να κάνει bypass το block της google για login.
Για καλύτερο αποτέλεσμα, πριν τρέξουμε το script, είμαστε logged in στο skroutz στον chrome.
Τρέχουμε το script, κάνουμε login στο παράθυρο που θα ανοίξει (εάν είστε ήδη logged in θα ξεκινήσει μόνο του) και όταν βλέπουμε την αρχική των παραγγελιών το scrape ξεκινάει.

Τέλος θα μας εμφανιστούν τα εξής νούμερα:

```sh
(Παράδειγμα του λογαριασμού μου)

Total orders found : 32
Total items checked : 71
Items equal/over 20 Euros : 15

With the (NEW) 17 Euros subscription you would earn in shipping : 28 Euros
With the (NEW) 20 Euros subscription you would earn in shipping : 25 Euros

Rough estimate of the (OLD) 17 Euros subscription :
(Total items * 3 euros shipping)
Total spent : 1307.8100000000006
Shipping earned : 196
```
