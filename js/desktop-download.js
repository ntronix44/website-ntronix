(function () {
    'use strict';

    var VERSION_PATTERN = /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/;
    var RELEASE_BASE = 'https://github.com/ntronix44/website-ntronix/releases/';

    function validateRelease(data) {
        if (!data || typeof data !== 'object' || Array.isArray(data)) {
            return null;
        }

        var version = data.version;
        if (typeof version !== 'string' || !VERSION_PATTERN.test(version)) {
            return null;
        }

        var tag = 'v' + version;
        var expectedInstallerUrl = RELEASE_BASE + 'download/' + tag + '/Volta-Engineer-Setup-' + version + '.exe';
        var expectedReleaseNotesUrl = RELEASE_BASE + 'tag/' + tag;

        if (data.tag !== tag ||
            data.installerUrl !== expectedInstallerUrl ||
            data.releaseNotesUrl !== expectedReleaseNotesUrl) {
            return null;
        }

        return {
            version: version,
            installerUrl: expectedInstallerUrl
        };
    }

    function setUnavailable(link, versionElement, status) {
        link.removeAttribute('href');
        link.setAttribute('aria-disabled', 'true');
        link.setAttribute('tabindex', '-1');
        link.classList.add('opacity-50', 'pointer-events-none');
        versionElement.textContent = '';
        versionElement.classList.add('hidden');
        status.hidden = false;
    }

    async function loadDesktopRelease() {
        var link = document.getElementById('windows-download-link');
        var versionElement = document.getElementById('windows-version');
        var status = document.getElementById('windows-download-status');

        if (!link || !versionElement || !status) {
            return;
        }

        link.addEventListener('click', function (event) {
            if (link.getAttribute('aria-disabled') === 'true' || !link.hasAttribute('href')) {
                event.preventDefault();
                return;
            }

            if (typeof window.trackDownload === 'function') {
                window.trackDownload('windows');
            }
        });

        try {
            var manifestUrl = new URL('./volta-desktop-release.json', window.location.href);
            if (manifestUrl.origin !== window.location.origin) {
                throw new Error('Release manifest must be same-origin.');
            }

            var response = await fetch(manifestUrl.href, {
                cache: 'no-store',
                mode: 'same-origin',
                redirect: 'error'
            });
            if (!response.ok) {
                throw new Error('Release manifest request failed.');
            }

            var release = validateRelease(await response.json());
            if (!release) {
                throw new Error('Release manifest is invalid.');
            }

            link.href = release.installerUrl;
            link.removeAttribute('aria-disabled');
            link.removeAttribute('tabindex');
            link.classList.remove('opacity-50', 'pointer-events-none');
            versionElement.textContent = 'v' + release.version;
            versionElement.classList.remove('hidden');
            status.hidden = true;
        } catch (error) {
            setUnavailable(link, versionElement, status);
        }
    }

    loadDesktopRelease();
})();
