# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 23:48:05 2016

@author: USER
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 23:44:47 2016

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import re
f = open("hvd.aiml",'r').read()

aiml_dic = {}
m = re.findall ( '<category>(.*?)</srai></template></category>', f, re.DOTALL)
print(m[0])

for c in m:
    pattern = re.findall( '<pattern>(.*?)</pattern>', f, re.DOTALL)
    template = re.findall( '<template>(.*?)</template>', f, re.DOTALL)
    that = re.findall( '<that>(.*?)</that>', f, re.DOTALL)
    main_pattern = re.findall( '<srai>(.*?)</srai>', f, re.DOTALL)
    aiml_dic[pattern[0]] = {}
    aiml_dic[pattern[0]]["template"] = template
    aiml_dic[pattern[0]]["that"] = that
    aiml_dic[pattern[0]]["srai"] = []
    

all_categories = re.findall('<category>(.*?)</category>',f,re.DOTALL)
for cat in all_categories:
    srai = re.findall('<srai>(.*?)</srai>',f,re.DOTALL)
    if srai:
        additional_pattern = re.findall('<category><pattern>(.*?)</pattern><template>',f,re.DOTALL)
    aiml_dic[srai[0]]["srai"] = additional_pattern
    