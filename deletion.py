# -*- coding: utf-8 -*-
import fileinput
import re

#for line in fileinput.input('sektorler.json', inplace=True):
    
    #print(line.replace("\\r\\n                                           ", ""))
    #print(re.sub(r'\s\d+', "", line))

for line in fileinput.input('iller.json', inplace=True):
    
     #print(re.sub(r"\\r\\n\s+", " ",line))
     #print(re.sub(r"\s\(\d+\)", "",line))
     #print(re.sub(r"\(", "",line))
     print(re.sub(r"\)", "",line))
 
for line in fileinput.input('job.json', inplace=True):
    
     #print(re.sub(r"\\r\\n\s+", " ",line))
     #print(re.sub(r"\s\(\d+\)", "",line))
     #print(re.sub(r"\(", "",line))
     #
     print(line.replace("\u00a0(", ""))
 
