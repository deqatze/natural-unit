# natural-unit
natural units are units based on **physics constants**, in this case:
| |constant name|dimension|equation|
|----|- |---------|--------|
|c|speed of light in vacuum|m/s|E=mc^2
|h|Planck constant|Js| E=h v
|G|gravitatonal constant|Nm^2/kg^2|F=G⋅m1⋅m2/r^2
|kB|Boltzmann constant|J/K|PV=n⋅kB⋅T
|e0|permittivity of free space|F/m|F=k⋅q1⋅q2/4π⋅e0⋅r^2
|K|luminous efficacy radiation of frequency 540×10^12 Hz|lm/W|K=683

c, h, kB and K are SI defining constants

# how to use this?
you need to import in python cmd
```python
>>>from units import *
```
then you can convert SI units to natural units by using '/'
```python
>>>20/m    #imput:metre
4.936625400978168e+35 #output:natural length
```
convert natural units to SI units using '*'
```python
>>>5*s     #input:natural time
6.756925391423419e-43  #output:second
```

## supported units
|symbol|name|quantity|
|-|-|-|
|m|metre|length
|s|second|time
|kg|kilogram|mass
|K|kelvin|temperature
|C|coulomb|electric charge
|A|ampere|electric current
|lm|lumen|luminous flux
|Hz|hertz|frequency
|N|newton|force
|Pa|pascal|pressure
|J|joule|energy
|W|watt|power
|V|volt|voltage
|ohm|ohm|resistance
|F|farad|capacitance
|Wb|weber|magnetic flux
|T|tesla|magnetic induction
|H|henry|inductance
|lx|lux|illuminance
