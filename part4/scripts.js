// Helper functions

function getCookie(name) {
  const cookies = document.cookie.split('; ');
  for (const c of cookies) {
    const [key, value] = c.split('=');
    if (key === name) return value;
  }
  return null;
}

function setCookie(name, value, days = 1) {
  const d = new Date();
  d.setTime(d.getTime() + days * 24 * 60 * 60 * 1000);
  document.cookie = `${name}=${value}; path=/; expires=${d.toUTCString()}`;
}

// Mock login (for testing purposes)
async function loginUser(email, password) {
  // Fake API - for testing only
  /*if (email === "user@example.com" && password === "password123") {
    return { access_token: "mock-jwt-token-12345" };
  } else {
    throw new Error("Invalid credentials");
  }*/
  async function loginUser(email, password) {
  const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ email, password })
  });

  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.message || 'Login failed');
  }

  const data = await response.json();
  return { access_token: data.token };
}

}

// Check if token exists
function isAuthenticated() {
  return getCookie('token') !== null;
}

// Show or hide the login link based on auth status
function toggleLoginLink() {
  const loginLink = document.getElementById('login-link');
  if (!loginLink) return;
  if (isAuthenticated()) loginLink.style.display = 'none';
  else loginLink.style.display = 'inline';
}

function showUserEmail() {
  const email = localStorage.getItem('userEmail');
  const emailElement = document.getElementById('user-email');
  if (email && emailElement) {
    emailElement.textContent = `مرحباً، ${email}`;
  }
}

// Login handling - set up the login form
function setupLoginForm() {
  const form = document.getElementById('login-form');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = form.email.value.trim();
    const password = form.password.value;

    try {
      const data = await loginUser(email, password);
      setCookie('token', data.access_token, 1);
      localStorage.setItem('userEmail', email);
      window.location.href = 'index.html';
    } catch (err) {
      document.getElementById('error-msg').textContent = 'Incorrect email or password';
    }
  });
}

// Fetch places list - mock data (for testing)
async function fetchPlaces(token) {
  // Test data - replace this with actual API request
  return [
    { id: 1, name: "Beautiful Apartment", price: 30, description: "A wonderful apartment in the city center." },
    { id: 2, name: "Luxury Villa", price: 90, description: "A spacious villa with a large garden." },
    { id: 3, name: "Small Room", price: 15, description: "A convenient room for short stays." },
  ];
}

// Display places on the page with filter support
async function displayPlaces() {
  const placesList = document.getElementById('places-list');
  if (!placesList) return;

  const token = getCookie('token');
  const places = await fetchPlaces(token);

  function renderPlaces(filteredPlaces) {
    placesList.innerHTML = '';
    filteredPlaces.forEach(place => {
      const card = document.createElement('div');
      card.classList.add('place-card');
      card.innerHTML = `
        <h3>${place.name}</h3>
        <p>Price: ${place.price} SAR / night</p>
        <p>${place.description}</p>
        <a href="place.html?id=${place.id}" class="details-button">View Details</a>
      `;
      placesList.appendChild(card);
    });
  }

  renderPlaces(places);

  // Price filter
  const filter = document.getElementById('price-filter');
  if (filter) {
    filter.addEventListener('change', (e) => {
      const val = e.target.value;
      if (val === 'all') {
        renderPlaces(places);
      } else {
        const filtered = places.filter(p => p.price <= Number(val));
        renderPlaces(filtered);
      }
    });
  }
}

// Fetch place details (mock)
async function fetchPlaceDetails(placeId, token) {
  // Test data
  const places = await fetchPlaces(token);
  const place = places.find(p => p.id === Number(placeId));
  if (!place) return null;

  // Mock reviews data
  const reviews = [
    { user: "Mohammed", comment: "Very nice place", rating: 5 },
    { user: "Sara", comment: "My stay was excellent", rating: 4 }
  ];

  return { ...place, reviews };
}

// Display place details and reviews
async function displayPlaceDetails() {
  const placeDetailsSection = document.getElementById('place-details');
  const reviewsList = document.getElementById('reviews-list');
  const addReviewSection = document.getElementById('add-review-section');

  if (!placeDetailsSection || !reviewsList) return;

  const urlParams = new URLSearchParams(window.location.search);
  const placeId = urlParams.get('id');
  if (!placeId) return;

  const token = getCookie('token');
  toggleLoginLink();

  const place = await fetchPlaceDetails(placeId, token);
  if (!place) {
    placeDetailsSection.innerHTML = "<p>Place not found</p>";
    return;
  }

  placeDetailsSection.innerHTML = `
    <h2>${place.name}</h2>
    <p>Price: ${place.price} SAR / night</p>
    <p>${place.description}</p>
  `;

  reviewsList.innerHTML = '';
  if (place.reviews && place.reviews.length > 0) {
    place.reviews.forEach(r => {
      const reviewCard = document.createElement('div');
      reviewCard.classList.add('review-card');
      reviewCard.innerHTML = `
        <h4>${r.user}</h4>
        <p>Rating: ${r.rating} / 5</p>
        <p>${r.comment}</p>
      `;
      reviewsList.appendChild(reviewCard);
    });
  } else {
    reviewsList.innerHTML = "<p>No reviews yet.</p>";
  }

  if (token) {
    addReviewSection.style.display = 'block';
  } else {
    addReviewSection.style.display = 'none';
  }
}

// Submit a new review (mock)
async function submitReview(token, placeId, reviewText) {
  // Replace this with real API request
  // This is just a simulation
  return { success: true };
}

// Set up review form
function setupReviewForm() {
  const form = document.getElementById('review-form');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const token = getCookie('token');
    if (!token) {
      alert('You must be logged in to submit a review');
      window.location.href = 'index.html';
      return;
    }

    const urlParams = new URLSearchParams(window.location.search);
    const placeId = urlParams.get('id');
    const reviewText = form['review-text'].value.trim();

    if (!reviewText) return alert('Please write a review');

    try {
      const response = await submitReview(token, placeId, reviewText);
      if (response.success) {
        alert('Review submitted successfully');
        form.reset();
        displayPlaceDetails(); // Refresh the page to show the new review
      } else {
        alert('Failed to submit review');
      }
    } catch {
      alert('An error occurred while submitting the review');
    }
  });
}

// When the page loads
document.addEventListener('DOMContentLoaded', () => {
  toggleLoginLink();
  showUserEmail();
  setupLoginForm();
  displayPlaces();
  displayPlaceDetails();
  setupReviewForm();
});
