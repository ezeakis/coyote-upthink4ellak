# coyote-upthink4ellak

**Ιδέα**

Η ιδέα μας είναι να φτιάξουμε μία Ζώνη Βοήθειας. Μία ζώνη την οποία θα φοράνε τυφλοί άνθρωποι και θα τους ειδοποιεί όταν πλησιάζουν σε κάποιο έπιπλο για να μην χτυπήσουν.

**Ιστορία**

Οι ημερομηνίες με τις δραστηριότητες μπορούν να βρεθούν στο αρχείο history.md

**Υλικά**

1. Ζώνη
2. [Αισθητήρα υπερήχων](https://grobotronics.com/ultrasonic-sensor-sr04.html) 2.5 euros
3. [Buzzer](https://grobotronics.com/buzzer-5v.html?sl=en) 0.4 euros
4. [Raspberry Pi Zero with headers](https://nettop.gr/index.php/component/virtuemart/raspberry-pi-zero-w-with-headers.html?Itemid=1678) 14.70 euros
5. [SD Card](https://grobotronics.com/microsdhc-16gb-class-10-sandisk-ultra-sdsquar-sdsquar-016g-gn6ma.html) 8.90 euros
6. [Θήκη μπαταριών 3 ΑΑΑ](https://grobotronics.com/battery-holder-3xa-with-wires.html) 0.60 euros
7. [Micro USB Adaptor](https://grobotronics.com/usb-micro-to-jack-female-5.5x2.1.html?sl=en) 1.20 euros
8. [Jumper Wires Female to Male](https://grobotronics.com/jumper-wires-15cm-female-to-male-pack-of-10.html) 1.80 euros το σετ
9. [Breadboard](https://grobotronics.com/breadboard-mini-white.html) 1.60 euros
10. [Αντίσταση 220 Ohm](https://grobotronics.com/carbon-1-4w-5-220ohm.html) 0.01 euros
11. [Αντίσταση 330 Ohm](https://grobotronics.com/carbon-1-4w-5-330ohm.html) 0.01 euros
12. [3 μπαταρίες 1.5V AAA](https://grobotronics.com/battery-varta-alkaline-longlife-lr61-1.5v-aaa-4pack.html) 2.20 euros το σετ των τεσσάρων

Σύνολο: 33.92 euros

**Λεπτομέρειες Υλοποίησης**
Στον φάκελο **Συνδεσμολογία** υπάρχει το αρχείο **Συνδεσμολογία.md** το οποίο περιγράφει το πως γίνονται οι συνδέσεις ενώ οι φωτογραφίες **Αισθητήρας 1.jpg** και **Αισθητήρας 2.jpg** απεικονίζουν τη συνδεσμολογία ειδικά για τον αισθητήρα.

Το αρχείο **main.py** περιέχει τον κώδικα της λύσης. Το αρχείο θα τοποθετηθεί σε φάκελο στο Raspberry Pi και θα εκτελείται ως εξής:
**python main.py**
