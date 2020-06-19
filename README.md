# top-flopStoxx
This file scrapes the stock market and returns the top 5 and bottom 5 stocks.
Finally its writes the result into a.txt file

### Data Source:
https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=20735&TIME_SPAN=INTRADAY

#### Libaries used:
* from selenium import webdriver
* import time
* import pandas as pd

## The results looks similar to this:

## BEST PERFORMER Dax Today
Index | Name | Change | Price 
------------ | -------------|-------------|-------------
|0|                        BASF|   +1,89 %|     54,01
|1|            COVESTRO AG O.N.|   +1,61 %|     33,48
|2|                  Vonovia SE|   +1,25 %|     55,14
|3|       Infineon Technologies|   +0,92 %|    20,315
|4|              Münchener Rück|   +0,70 %|    228,70

## WORST PERFORMER DAX Today
Index | Name | Change | Price 
------------ | -------------|-------------|-------------
|25|               Volkswagen VZ|   -1,16 %|    132,58
|26|               DEUTSCHE BANK|   -2,05 %|     8,263
|27|                   HENKEL Vz|   -2,98 %|     82,62
|28|          DEUTSCHE LUFTHANSA|   -4,01 %|     9,868
|29|                    WIRECARD|  -61,82 %|     39,90

## BEST PERFORMER SMI Today
Index | Name | Change | Price 
------------ | -------------|-------------|-------------
|0|                  SWISSCOM N|   +1,28 %|    499,90
|1|                    Givaudan|   +1,20 %|  3.461,00
|2|                Swatch Group|   +1,20 %|    194,30
|3|                       SGS N|   +0,87 %|  2.312,00
|4|                     Sika AG|   +0,68 %|    184,30

## WORST PERFORMER SMI Today
Index | Name | Change | Price 
------------ | -------------|-------------|-------------
|15|               LafargeHolcim|   -0,60 %|     41,65
|16|                    ROCHE GS|   -0,62 %|    337,45
|17|                   LONZA GRP|   -0,69 %|    491,60
|18|             Swiss Life Hldg|   -0,73 %|    355,40
|19|                      Nestle|   -1,00 %|    106,84
