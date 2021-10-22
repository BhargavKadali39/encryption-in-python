# encryption-in-python
basic encryption in python

Firstly to encrypt any given data we need some logic of how to pack and unpack the data, so here we use below steps to encrypt the data.

* Take input from the user as string and remove all the whitespace's from it.
* Store the length of the string without whitespace's in variable L.
* Find the root value of the var L.
* Using ceil and floor fun find it's upper and lower values and assign them as rows and column's.
* Check if rows * cols >= l
* If the above condition gets satisfied then choose the one with the minimum area in rows/cols.
EX: if L = 8
its square root is 2, 3, so re assign the values as 3, 3.
i.e 2 * 3 = 6 which is less than L so use max value for both as 3, 3.

* use the lower value as row and higher value as cols.

Below is the sample output of given program: 

    Enter data to encrypt: cloud there is one unifying theme to remember cloud capabilities software infrastructure andplatformare delivered as a service
    
    csgeasraad
    lotmpoanra
    onhbafsdes
    ueeebttpda
    dumriwrles
    tneclauale
    hitlirctir
    efootetfvv
    ryruiiuoei
    eiedenrrrc
    inmcsfemee
