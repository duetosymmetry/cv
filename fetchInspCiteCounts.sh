#!/bin/bash

curl "http://old.inspirehep.net/search?ln=en&ln=en&p=exactauthor%3AL.C.Stein.2&of=hlxu&action_search=Search&sf=earliestdate&so=d&rm=&rg=250&sc=0" | gsed -n -e "s/;%%<br \/>  %/: /g" -e "s/.*CITATION = \(.*\) counted.*/\1/gp" > citeCounts.txt
