#!/usr/bin/env python
# coding: utf-8

# In[5]:


import xml.etree.ElementTree as ET
import requests


url = "https://dblp.org/pid/155/5140.xml"
tree = ET.ElementTree(ET.fromstring(requests.get(url).content))


num_publicacoes = 0
for elem in tree.iter("title"):
    num_publicacoes += 1
print("Numero de publicações:", num_publicacoes)


coautores = {}
for elem in tree.iter("author"):
    coautores[elem.text] = coautores.get(elem.text, 0) + 1
print("Coautores:")
for autor, num_pub in coautores.items():
    print(f"{autor}: {num_pub}")


veiculos_publicacao = set()
for elem in tree.iter("journal"):
    veiculos_publicacao.add(elem.text)
for elem in tree.iter("booktitle"):
    veiculos_publicacao.add(elem.text)
print("Veiculos de publicação:", veiculos_publicacao)


# In[ ]:





# In[ ]:




