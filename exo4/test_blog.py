import unittest

from blog import get_web_page_infos

class TestWebPageInfos(unittest.TestCase):
  def test_gameblog_title(self):
    """Vérifie que le titre de la page contient 'Gameblog.fr'."""
    title, _ = get_web_page_infos('https://www.gameblog.fr')
    self.assertIn('Gameblog.fr', title)

  def test_gameblog_rss_link(self):
    """Vérifie que la fonction trouve bien un lien RSS sur gameblog.fr."""
    _, rss_link = get_web_page_infos('https://www.gameblog.fr')
    self.assertIsNotNone(rss_link)
    self.assertTrue('rss' in rss_link)

if __name__ == '__main__': unittest.main()
