let allApps = [];

// Load apps on page load
document.addEventListener('DOMContentLoaded', () => {
    loadApps();
    setupSearch();
});

// Fetch and display apps
async function loadApps() {
    try {
        const response = await fetch('apps.json');
        allApps = await response.json();
        displayApps(allApps);
    } catch (error) {
        console.error('Error loading apps:', error);
        document.getElementById('appsGrid').innerHTML = '<p>Error loading apps</p>';
    }
}

// Display apps in grid
function displayApps(apps) {
    const appsGrid = document.getElementById('appsGrid');
    appsGrid.innerHTML = '';

    if (apps.length === 0) {
        appsGrid.innerHTML = '<p style="grid-column: 1/-1; text-align: center; color: white; font-size: 18px;">No apps found</p>';
        return;
    }

    apps.forEach(app => {
        const appCard = document.createElement('div');
        appCard.className = 'app-card';

        // Format price: $0 becomes "Free"
        const priceText = app.price === 0 ? 'Free' : `$${app.price}`;
        const priceClass = app.price === 0 ? 'free' : '';

        appCard.innerHTML = `
            <div class="app-icon">${app.icon}</div>
            <div class="app-info">
                <div class="app-name">${app.name}</div>
                <div class="app-description">${app.description}</div>
                <div class="app-footer">
                    <span class="app-price ${priceClass}">${priceText}</span>
                    <button class="download-btn" onclick="downloadApp('${app.name}')">Download</button>
                </div>
            </div>
        `;

        appsGrid.appendChild(appCard);
    });
}

// Search functionality
function setupSearch() {
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        const filtered = allApps.filter(app =>
            app.name.toLowerCase().includes(query) ||
            app.description.toLowerCase().includes(query)
        );
        displayApps(filtered);
    });
}

// Download handler
function downloadApp(appName) {
    alert(`Starting download of ${appName}...`);
    // You can replace this with actual download logic later
    console.log(`Download started for: ${appName}`);
}
