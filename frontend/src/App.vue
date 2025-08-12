<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div class="app-wrapper">
    <header class="app-header">
      <div class="header-container">
        <RouterLink to="/" class="brand-logo">
          <span class="brand-gradient-text">🎟️ Camplong Events</span>
        </RouterLink>
        <nav class="main-nav">
          <RouterLink to="/" class="nav-link">Home</RouterLink>
        </nav>
      </div>
    </header>

    <main class="main-content">
      <RouterView />
    </main>

    <footer class="app-footer">
      <p>
        &copy; {{ new Date().getFullYear() }} Camplong Events. All rights
        reserved.
      </p>
    </footer>
  </div>
</template>

<style>
/* Import the font for the whole application */
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;900&display=swap");

/* Define global CSS variables for colors */
:root {
  --glow-color-1: #ec4899; /* pink */
  --glow-color-2: #8b5cf6; /* violet */
  --text-primary: #f8fafc;
  --text-secondary: #9ca3af;
  --background-dark: #0c0a09;
}

/* Global body styles */
body {
  margin: 0;
  font-family: "Poppins", sans-serif;
  background-color: var(--background-dark);
  background-image: radial-gradient(
      circle at 25% 30%,
      rgba(236, 72, 153, 0.1),
      rgba(236, 72, 153, 0) 40%
    ),
    radial-gradient(
      circle at 75% 70%,
      rgba(139, 92, 246, 0.1),
      rgba(139, 92, 246, 0) 40%
    );
  color: var(--text-primary);
}

.app-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Header Styles */
.app-header {
  position: sticky;
  top: 0;
  z-index: 50;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid #27272a;
}

.header-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand-logo {
  font-size: 1.5rem; /* 24px */
  font-weight: 700;
  letter-spacing: 0.05em;
  text-decoration: none;
}

.brand-gradient-text {
  background-image: linear-gradient(
    to right,
    var(--glow-color-1),
    var(--glow-color-2),
    #22d3ee
  );
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.main-nav {
  display: flex;
  gap: 1.5rem; /* 24px */
}

/* Navigation Link Styles */
.nav-link {
  color: #d1d5db; /* gray-300 */
  text-decoration: none;
  position: relative;
  transition: all 0.3s;
}

.nav-link:hover {
  color: white;
  text-shadow: 0 0 5px var(--glow-color-1), 0 0 10px var(--glow-color-1);
}

.nav-link::after {
  content: "";
  position: absolute;
  width: 100%;
  transform: scaleX(0);
  height: 2px;
  bottom: -4px;
  left: 0;
  background: linear-gradient(90deg, var(--glow-color-1), var(--glow-color-2));
  transform-origin: bottom right;
  transition: transform 0.3s ease-out;
}

.nav-link:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}

/* Main Content and Footer */
.main-content {
  max-width: 1280px;
  width: 100%;
  margin: 0 auto;
  padding: 1.5rem;
  box-sizing: border-box;
  flex-grow: 1;
}

.app-footer {
  text-align: center;
  padding: 1.5rem;
  color: #6b7280; /* gray-500 */
  font-size: 0.875rem; /* 14px */
}
</style>
