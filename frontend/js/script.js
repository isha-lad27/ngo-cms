const API_BASE_URL = "http://127.0.0.1:8000/api";

// Load Banners
async function loadBanners() {
    try {
        const response = await fetch(`${API_BASE_URL}/banners/`);
        const banners = await response.json();

        console.log("Banners:", banners);
    } catch (error) {
        console.error("Error loading banners:", error);
    }
}

// Load Vision and Mission
async function loadVisionMission() {
    try {
        const response = await fetch(`${API_BASE_URL}/vision-mission/`);
        const data = await response.json();

        console.log("Vision & Mission:", data);
    } catch (error) {
        console.error("Error loading vision & mission:", error);
    }
}

// Load Statistics
async function loadStatistics() {
    try {
        const response = await fetch(`${API_BASE_URL}/statistics/`);
        const statistics = await response.json();

        console.log("Statistics:", statistics);
    } catch (error) {
        console.error("Error loading statistics:", error);
    }
}

// Load Initiatives
async function loadInitiatives() {
    try {
        const response = await fetch(`${API_BASE_URL}/initiatives/`);
        const initiatives = await response.json();

        console.log("Initiatives:", initiatives);
    } catch (error) {
        console.error("Error loading initiatives:", error);
    }
}

// Run all API functions when page loads
document.addEventListener("DOMContentLoaded", function () {
    loadBanners();
    loadVisionMission();
    loadStatistics();
    loadInitiatives();
});