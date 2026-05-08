// Peakboard Guru i18n
// Translations for UI strings (blog post content stays in original language).
(function () {
  'use strict';

  var STORAGE_KEY = 'pbg-lang';
  var DEFAULT_LANG = 'en';
  var SUPPORTED = ['en', 'de'];

  var TRANSLATIONS = {
    // Header / Search
    'header.search.placeholder': {
      en: 'Search...',
      de: 'Suchen...'
    },
    'header.search.aria': {
      en: 'Search',
      de: 'Suchen'
    },
    'header.lang.aria': {
      en: 'Switch language',
      de: 'Sprache wechseln'
    },

    // Footer
    'footer.about.text': {
      en: "The Guru shows you how to build the hottest Peakboard apps on the planet. No theory lectures, no 47-page whitepapers - just real projects you can steal, learn from, and actually use. May your dashboards always be real-time and your data sources never timeout.",
      de: "Der Guru zeigt dir, wie du die heißesten Peakboard-Apps des Planeten baust. Keine Theorie-Vorträge, keine 47-seitigen Whitepapers - nur echte Projekte, die du klauen, von denen du lernen und die du tatsächlich nutzen kannst. Mögen deine Dashboards stets in Echtzeit sein und deine Datenquellen niemals einen Timeout haben."
    },
    'footer.quicklinks': {
      en: 'Quick Links',
      de: 'Schnelllinks'
    },
    'footer.about': {
      en: 'About',
      de: 'Über'
    },
    'footer.search': {
      en: 'Search',
      de: 'Suche'
    },
    'footer.legal': {
      en: 'Legal Notice',
      de: 'Impressum'
    },
    'footer.youtube': {
      en: 'YouTube',
      de: 'YouTube'
    },
    'footer.reddit': {
      en: 'Reddit',
      de: 'Reddit'
    },
    'footer.designer': {
      en: 'Peakboard Designer',
      de: 'Peakboard Designer'
    },
    'footer.copyright.suffix': {
      en: 'All rights reserved.',
      de: 'Alle Rechte vorbehalten.'
    },

    // Home page
    'home.hero.title': {
      en: "Welcome to the Guru's Dashboard Dojo",
      de: 'Willkommen im Dashboard-Dojo des Gurus'
    },
    'home.hero.p1.before': {
      en: 'Looking for ready-made Peakboard projects you can download, take apart, remix, and make your own? You\'ve come to the right place - and it\'s completely free if you grab the',
      de: 'Du suchst fertige Peakboard-Projekte zum Herunterladen, Auseinandernehmen, Remixen und Anpassen? Du bist hier richtig - und es ist komplett kostenlos, wenn du dir die'
    },
    'home.hero.p1.link': {
      en: 'Community Edition of Peakboard Designer',
      de: 'Community Edition des Peakboard Designers'
    },
    'home.hero.p1.after': {
      en: '.',
      de: 'holst.'
    },
    'home.hero.p2': {
      en: 'You\'ll find dashboards for <strong>production</strong>, <strong>logistics</strong>, <strong>restaurants</strong>, <strong>hotels</strong>, <strong>personal use</strong>, and things that fall squarely into the <em>"why not?"</em> category. Whether it\'s a shopfloor monitor or a craft-beer brewing tracker - grab what you need and make it yours.',
      de: 'Du findest hier Dashboards für <strong>Produktion</strong>, <strong>Logistik</strong>, <strong>Restaurants</strong>, <strong>Hotels</strong>, den <strong>privaten Gebrauch</strong> und Dinge, die ganz klar in die Kategorie <em>"Warum eigentlich nicht?"</em> fallen. Ob Shopfloor-Monitor oder Craft-Beer-Brau-Tracker - schnapp dir, was du brauchst, und mach es dir zu eigen.'
    },
    'home.hero.p3': {
      en: 'No fine print, no strings attached, no obligation to subscribe to yet another newsletter. Just download and go.',
      de: 'Kein Kleingedrucktes, keine Hintertüren, keine Pflicht, noch einen weiteren Newsletter zu abonnieren. Einfach herunterladen und loslegen.'
    },
    'home.allArticles': {
      en: 'All Articles',
      de: 'Alle Artikel'
    },

    // Article card
    'card.readArticle': {
      en: 'Read Article →',
      de: 'Artikel lesen →'
    },

    // Post layout
    'post.publishedIn': {
      en: 'Published in',
      de: 'Veröffentlicht in'
    },
    'post.uncategorized': {
      en: 'Uncategorized',
      de: 'Ohne Kategorie'
    },
    'post.read': {
      en: 'read',
      de: 'Lesezeit'
    },
    'post.copyLink': {
      en: 'Copy link',
      de: 'Link kopieren'
    },
    'post.copyLink.alert': {
      en: 'Link copied to clipboard!',
      de: 'Link in die Zwischenablage kopiert!'
    },
    'post.resources': {
      en: 'Resources',
      de: 'Ressourcen'
    },
    'post.keepReading': {
      en: 'Keep Reading',
      de: 'Weiterlesen'
    },
    'post.previous': {
      en: '← Previous Article',
      de: '← Vorheriger Artikel'
    },
    'post.next': {
      en: 'Next Article →',
      de: 'Nächster Artikel →'
    },
    'post.relatedLinks': {
      en: 'Related Links',
      de: 'Verwandte Links'
    },
    'post.aiPromptHeader': {
      en: 'AI-generated project',
      de: 'KI-generiertes Projekt'
    },
    'post.aiPromptIntro': {
      en: 'This project was created entirely with AI. The exact prompt used:',
      de: 'Dieses Projekt wurde vollständig mit KI erstellt. Der verwendete Prompt:'
    },

    // Archive layout
    'archive.title': {
      en: 'Article Archive',
      de: 'Artikel-Archiv'
    },

    // Sidemenu
    'sidemenu.home': {
      en: 'Home',
      de: 'Startseite'
    },
    'sidemenu.about': {
      en: 'About',
      de: 'Über'
    },
    'sidemenu.archive': {
      en: 'Archive',
      de: 'Archiv'
    },

    // Search page
    'search.title': {
      en: 'Search Articles',
      de: 'Artikel suchen'
    },
    'search.placeholder': {
      en: 'Type to search articles...',
      de: 'Tippen, um Artikel zu suchen...'
    },
    'search.readMore': {
      en: 'Read More',
      de: 'Weiterlesen'
    },
    'search.noResults': {
      en: 'No results found for',
      de: 'Keine Ergebnisse gefunden für'
    },

    // About / Impressum hero
    'about.hero.title': {
      en: 'About This Blog',
      de: 'Über dieses Blog'
    },
    'about.hero.subtitle': {
      en: "Peakboard Guru - The hottest apps on the planet",
      de: 'Peakboard Guru - Die heißesten Apps des Planeten'
    },
    'impressum.hero.title': {
      en: 'Legal Notice',
      de: 'Impressum'
    },
    'impressum.hero.subtitle': {
      en: 'Impressum according to German law',
      de: 'Impressum nach deutschem Recht'
    }
  };

  function getStoredLang() {
    try {
      var v = localStorage.getItem(STORAGE_KEY);
      if (v && SUPPORTED.indexOf(v) !== -1) return v;
    } catch (e) { /* ignore */ }
    return null;
  }

  function detectLang() {
    var stored = getStoredLang();
    if (stored) return stored;
    var nav = (navigator.language || navigator.userLanguage || '').toLowerCase();
    if (nav.indexOf('de') === 0) return 'de';
    return DEFAULT_LANG;
  }

  function setStoredLang(lang) {
    try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) { /* ignore */ }
  }

  function translate(key, lang) {
    var entry = TRANSLATIONS[key];
    if (!entry) return null;
    return entry[lang] != null ? entry[lang] : entry[DEFAULT_LANG];
  }

  function applyTranslations(lang) {
    // Text content
    var nodes = document.querySelectorAll('[data-i18n]');
    nodes.forEach(function (el) {
      var key = el.getAttribute('data-i18n');
      var val = translate(key, lang);
      if (val == null) return;
      if (el.hasAttribute('data-i18n-html')) {
        el.innerHTML = val;
      } else {
        el.textContent = val;
      }
    });

    // Attribute translations: data-i18n-attr="placeholder:search.placeholder,title:post.copyLink"
    var attrNodes = document.querySelectorAll('[data-i18n-attr]');
    attrNodes.forEach(function (el) {
      var spec = el.getAttribute('data-i18n-attr');
      spec.split(',').forEach(function (pair) {
        var parts = pair.split(':');
        if (parts.length !== 2) return;
        var attr = parts[0].trim();
        var key = parts[1].trim();
        var val = translate(key, lang);
        if (val != null) el.setAttribute(attr, val);
      });
    });

    // Whole-block language sections (e.g. translated markdown content)
    var blocks = document.querySelectorAll('[data-lang]');
    blocks.forEach(function (el) {
      el.style.display = (el.getAttribute('data-lang') === lang) ? '' : 'none';
    });

    // Document <html lang="">
    document.documentElement.setAttribute('lang', lang);

    // Update toggle button label
    var btnLabel = document.querySelector('[data-lang-current]');
    if (btnLabel) btnLabel.textContent = lang.toUpperCase();
  }

  function setLang(lang) {
    if (SUPPORTED.indexOf(lang) === -1) lang = DEFAULT_LANG;
    setStoredLang(lang);
    window.PBG_LANG = lang;
    applyTranslations(lang);
    document.dispatchEvent(new CustomEvent('pbg:langchange', { detail: { lang: lang } }));
  }

  function toggleLang() {
    setLang(window.PBG_LANG === 'de' ? 'en' : 'de');
  }

  // Public API
  window.PBG_I18N = {
    t: function (key) { return translate(key, window.PBG_LANG || DEFAULT_LANG); },
    setLang: setLang,
    toggleLang: toggleLang,
    getLang: function () { return window.PBG_LANG || DEFAULT_LANG; },
    apply: function () { applyTranslations(window.PBG_LANG || DEFAULT_LANG); }
  };

  // Initial setup: set window.PBG_LANG immediately so inline scripts can read it
  window.PBG_LANG = detectLang();

  function init() {
    applyTranslations(window.PBG_LANG);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
