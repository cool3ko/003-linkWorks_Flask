document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/service')  // assuming you have an endpoint /api/service
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');
            content.innerHTML = `<p>Service Name: ${data.name}</p>`;
        })
        .catch(error => console.error('Error:', error));
});
