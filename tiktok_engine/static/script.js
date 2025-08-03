function validateForm() {
    const profileUrl = document.querySelector('input[name="profile_url"]').value;
    const videoUrl = document.querySelector('input[name="video_url"]').value;
    const urlPattern = /^https:\/\/www\.tiktok\.com\/.+$/;
    if (!urlPattern.test(profileUrl)) {
        alert('URL do perfil inválida!');
        return false;
    }
    if (videoUrl && !urlPattern.test(videoUrl)) {
        alert('URL do vídeo inválida!');
        return false;
    }
    return true;
}

function refreshReports() {
    fetch('/')
        .then(response => response.text())
        .then(html => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            document.querySelector('.container').innerHTML = doc.querySelector('.container').innerHTML;
            document.querySelector('form[action="/start"]').addEventListener('submit', function(event) {
                if (!validateForm()) event.preventDefault();
            });
        });
}

document.querySelector('form[action="/start"]').addEventListener('submit', function(event) {
    if (!validateForm()) event.preventDefault();
    document.querySelector('.status').textContent = 'Iniciando...';
    setTimeout(() => {
        document.querySelector('.status').textContent = 'Concluído!';
        refreshReports();
    }, 30000);
});

setInterval(refreshReports, 180000);
