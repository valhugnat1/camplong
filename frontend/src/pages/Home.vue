<template>
  <div class="home-page">
    <div class="hero-section">
      <h1 class="hero-title">
        <span>NIGHTS TO REMEMBER</span>
      </h1>
      <p class="hero-subtitle">
        Discover the most exclusive tech, house, and techno parties. Your next
        unforgettable experience is just a click away.
      </p>
    </div>

    <div v-if="events.length > 0" class="events-grid">
      <EventCard v-for="event in events" :key="event.id" :event="event" />
    </div>

    <div v-else class="loading-message">
      <div class="pulse">🕺 Loading events... 💃</div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import EventCard from "../components/EventCard.vue";

export default {
  name: "Home",
  components: { EventCard },
  data() {
    return {
      events: [],
    };
  },
  async created() {
    try {
      // ✅ Use a relative path. This works for both dev and prod.
      const res = await axios.get("/api/events");
      this.events = res.data;
    } catch (error) {
      console.log("Failed to fetch events:", error);
      console.error("Failed to fetch events:", error);
    }
  },
};
</script>

<style scoped>
.home-page {
  min-height: 100vh;
  padding-top: 4rem; /* 64px */
  padding-bottom: 4rem; /* 64px */
}

.hero-section {
  text-align: center;
  margin-bottom: 4rem; /* 64px */
}

.hero-title {
  font-size: 3rem; /* 48px */
  font-weight: 900;
  letter-spacing: -0.05em;
  margin-bottom: 1rem;
}

.hero-title span {
  background-image: linear-gradient(to bottom right, #f472b6, #8b5cf6, #22d3ee);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.hero-subtitle {
  font-size: 1.125rem; /* 18px */
  color: var(--text-secondary);
  max-width: 42rem; /* 672px */
  margin-left: auto;
  margin-right: auto;
}

.events-grid {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: 2.5rem; /* 40px */
}

.loading-message {
  text-align: center;
  color: var(--text-secondary);
  padding: 5rem 0;
  font-size: 1.5rem;
}

.pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

/* Responsive Grid Columns */
@media (min-width: 768px) {
  /* md breakpoint */
  .events-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .hero-title {
    font-size: 4.5rem; /* 72px */
  }
  .hero-subtitle {
    font-size: 1.25rem; /* 20px */
  }
}

@media (min-width: 1024px) {
  /* lg breakpoint */
  .events-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
</style>
