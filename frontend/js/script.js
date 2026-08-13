const API_BASE_URL = "https://ngo-cms-fsbh.onrender.com/api";

// Load Banners
async function loadBanners() {
    try {
        const response = await fetch(`${API_BASE_URL}/banners/`);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        console.log("Banners API response:", data);

        const container = document.getElementById("banner-container");

        if (!container) {
            return;
        }

        // Support both normal DRF response and paginated DRF response
        const banners = Array.isArray(data)
            ? data
            : (data.results || []);

        if (banners.length === 0) {
            container.innerHTML = `
                <div class="col-12 text-center">
                    <p>No banners available.</p>
                </div>
            `;
            return;
        }

        const banner = banners[0];

        // Support image_url or image field
        let imageUrl = banner.image_url || banner.image || "";

        // If Django returns a relative image path, attach backend URL
        if (imageUrl && imageUrl.startsWith("/")) {
            imageUrl = API_BASE_URL.replace("/api", "") + imageUrl;
        }

        container.innerHTML = `
            <div class="col-md-6 text-center">
                <img
                    src="${imageUrl}"
                    alt="${banner.title || "NGO Banner"}"
                    class="img-fluid rounded shadow"
                    style="max-height: 400px; width: 100%; object-fit: cover;"
                    onerror="this.style.display='none';"
                >
            </div>

            <div class="col-md-6 text-center text-md-start mt-4 mt-md-0">
                <h1 class="display-5 fw-bold">
                    ${banner.title || ""}
                </h1>

                <p class="lead">
                    ${banner.description || ""}
                </p>

                <a href="donate.html" class="btn btn-success">
                    Donate Now
                </a>
            </div>
        `;

    } catch (error) {
        console.error("Error loading banners:", error);

        const container = document.getElementById("banner-container");

        if (container) {
            container.innerHTML = `
                <div class="col-12 text-center">
                    <p>Unable to load banner.</p>
                    <small>${error.message}</small>
                </div>
            `;
        }
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
    loadAboutUs();
});

// Load About Us
async function loadAboutUs() {
    try {
        const response = await fetch(`${API_BASE_URL}/about-us/`);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        console.log("About Us:", data);

        // Our Story
        const storyElement = document.getElementById("our-story");
        if (storyElement && data.our_story) {
            storyElement.textContent = data.our_story.content;
        }

        // Core Values
        const valuesElement = document.getElementById("core-values");
        if (valuesElement && data.core_values) {
            valuesElement.innerHTML = data.core_values.map(value =>
                `<li>${value.value}</li>`
            ).join("");
        }

        // Programs
        const programsElement = document.getElementById("programs");
        if (programsElement && data.programs) {
            programsElement.innerHTML = data.programs.map(program =>
                `<div class="card mb-3">
                    <div class="card-body">
                        <h4>${program.name}</h4>
                        <p>${program.description || ""}</p>
                    </div>
                </div>`
            ).join("");
        }

        // Team Members
        const teamElement = document.getElementById("team-members");
        if (teamElement && data.team_members) {
            teamElement.innerHTML = data.team_members.map(member =>
                `<div class="card mb-3">
                    <div class="card-body">
                        <h4>${member.name}</h4>
                        <p>${member.role}</p>
                    </div>
                </div>`
            ).join("");
        }

    } catch (error) {
        console.error("Error loading About Us:", error);

        const storyElement = document.getElementById("our-story");
        if (storyElement) {
            storyElement.textContent = "Unable to load About Us information.";
        }
    }
}