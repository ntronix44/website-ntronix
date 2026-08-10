/**
 * app-download.js — Static APK Download (no secrets, no GitHub API)
 * =================================================================
 * Simply points all .apk-download links to the static APK file on the
 * server. No PAT, no private repo access, no CORS issues.
 * =================================================================
 */
(function () {
  'use strict';

  // GitHub Releases direct download — no redirect, triggers save-as
  // URL: https://github.com/ntronix44/website-ntronix/releases/download/v1.2.0/Ntronix-App-v1.2.0.apk
  const APK_PATH = 'https://github.com/ntronix44/website-ntronix/releases/download/v1.2.0/Ntronix-App-v1.2.0.apk';
  const APK_VERSION = '1.2.0';
  const APK_FILENAME = 'Ntronix-App-v1.2.0.apk';

  function updateAllLinks() {
    const links = document.querySelectorAll('.apk-download');
    if (!links.length) return;

    links.forEach(function (link) {
      link.href = APK_PATH;
      link.setAttribute('download', APK_FILENAME);
      link.style.pointerEvents = '';
      link.style.opacity = '';

      const versionEl = link.querySelector('[data-apk="version"]');
      if (versionEl) versionEl.textContent = APK_VERSION;

      const fallbackEl = link.querySelector('[data-apk="fallback"]');
      if (fallbackEl) fallbackEl.textContent = 'Download v' + APK_VERSION;

      const loadingEl = link.querySelector('[data-apk="loading"]');
      if (loadingEl) loadingEl.style.display = 'none';

      const dynamicEl = link.querySelector('[data-apk="dynamic"]');
      if (dynamicEl) dynamicEl.style.display = 'none';
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateAllLinks);
  } else {
    updateAllLinks();
  }
})();
