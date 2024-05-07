from bs4 import BeautifulSoup
import requests

from typing import Tuple, Optional

def get_web_page_infos(url: str) -> Tuple[str, Optional[str]]:
  """Extrait le titre d'une page web et le lien de son flux RSS si disponible.

  Args:
    url (str): L'URL de la page web à analyser.

  Returns:
    Tuple[str, Optional[str]]: Un tuple contenant le titre de la page et le lien RSS (si disponible).
  """
  response = requests.get(url, allow_redirects=True)
  soup = BeautifulSoup(response.text, 'html.parser')

  title = soup.title.text if soup.title else "Titre non trouvé"
  rss_link = None

  links = soup.find_all('link', rel='alternate', type='application/rss+xml')
  if links: rss_link = links[0].get('href')

  return title, rss_link