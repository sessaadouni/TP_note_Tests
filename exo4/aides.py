from bs4 import BeautifulSoup
import requests

def exemple_demo_beautifulsoup():
   kernel_org_homepage = requests.get('http://kernel.org', allow_redirects=True)
   contents = BeautifulSoup(kernel_org_homepage.text, 'html.parser')
   resources_on_page = contents.find_all('link')
   for resource in resources_on_page:
     # on affiche l'attribut "href" qui indique le lien à suivre vers la ressource
     resource_type = resource.get('type')
     resource_rel = ','.join(resource.get('rel'))
     resource_target = resource.get('href')
     print(f"Ressource de type {resource_type} avec rel = {resource_rel} et cible {resource_target}")

if __name__ == '__main__':
  exemple_demo_beautifulsoup()