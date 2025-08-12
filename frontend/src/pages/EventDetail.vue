<template>
  <div class="event-detail-page">
    <div v-if="loading" class="loading-skeleton">
      <div class="skeleton-image pulse"></div>
      <div class="skeleton-content">
        <div class="skeleton-line pulse" style="width: 70%"></div>
        <div class="skeleton-line pulse" style="width: 40%"></div>
        <div
          class="skeleton-line pulse"
          style="width: 90%; margin-top: 2rem"
        ></div>
        <div class="skeleton-line pulse" style="width: 85%"></div>
        <div class="skeleton-button pulse"></div>
      </div>
    </div>

    <div v-if="event && !loading" class="detail-grid">
      <div class="event-image-container">
        <img :src="event.image" :alt="event.title" class="event-image" />
      </div>

      <div class="event-info-container">
        <h1 class="event-title">
          <span>{{ event.title }}</span>
        </h1>

        <div class="info-blocks">
          <div class="info-block">
            <span class="icon">📅</span>
            <div>
              <p class="info-label">Date & Time</p>
              <p class="info-data">{{ formatDate(event.date) }}</p>
            </div>
          </div>
          <div class="info-block">
            <span class="icon">📍</span>
            <div>
              <p class="info-label">Location</p>
              <p class="info-data">{{ event.location }}</p>
            </div>
          </div>
        </div>

        <div class="description-section">
          <h2 class="section-title">About this event</h2>
          <p>{{ event.description }}</p>
        </div>

        <div class="artists-section">
          <h2 class="section-title">Line-up</h2>
          <p class="info-data">{{ event.artists.join(", ") }}</p>
        </div>

        <div class="registration-section">
          <p class="price">€{{ event.price.toFixed(2) }}</p>
          <router-link
            :to="`/events/${event.id}/register`"
            class="register-button"
          >
            Register Now
          </router-link>
        </div>
      </div>
    </div>

    <div v-if="error" class="error-message">
      <h2>🕺 Event Not Found 💃</h2>
      <p>Sorry, we couldn't find the event you're looking for.</p>
      <router-link to="/" class="register-button">Back to Home</router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "EventDetail",
  props: ["id"],
  data() {
    return {
      event: null,
      loading: true,
      error: false,
    };
  },
  async created() {
    try {
      // ✅ Use a relative path, just like in home.vue.
      // This is crucial for builds and proxies.
      const res = await axios.get(`/api/events/${this.id}`);
      this.event = res.data;
    } catch (err) {
      console.error("Failed to fetch event details:", err);
      this.error = true;
    } finally {
      this.loading = false;
    }
  },
  methods: {
    formatDate(dateString) {
      const options = {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        hour12: false,
      };
      return new Date(dateString).toLocaleString("en-US", options);
    },
  },
};
</script>

<style scoped>
/* Inherit pulse animation from home.vue or define it here if needed */
@keyframes pulse {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}
.pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

.event-detail-page {
  min-height: 100vh;
  padding: 4rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

/* --- Loading Skeleton --- */
.loading-skeleton {
  display: grid;
  gap: 2.5rem;
}
.skeleton-image {
  width: 100%;
  aspect-ratio: 3 / 2;
  background-color: var(--bg-secondary);
  border-radius: 0.75rem;
}
.skeleton-line {
  height: 1.5rem;
  background-color: var(--bg-secondary);
  border-radius: 0.5rem;
  margin-bottom: 1rem;
}
.skeleton-button {
  height: 3rem;
  width: 100%;
  background-color: var(--bg-secondary);
  border-radius: 0.5rem;
  margin-top: 2rem;
}

/* --- Main Detail Grid --- */
.detail-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2.5rem; /* 40px */
}

/* --- Left Column: Image --- */
.event-image-container {
  width: 100%;
}
.event-image {
  width: 100%;
  height: auto;
  aspect-ratio: 3 / 2;
  object-fit: cover;
  border-radius: 0.75rem; /* 12px */
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1),
    0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

/* --- Right Column: Info --- */
.event-info-container {
  display: flex;
  flex-direction: column;
}

.event-title {
  font-size: 2.25rem; /* 36px */
  font-weight: 900;
  letter-spacing: -0.05em;
  margin-bottom: 1.5rem;
  line-height: 1.1;
}
.event-title span {
  background-image: linear-gradient(to bottom right, #f472b6, #8b5cf6, #22d3ee);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.info-blocks {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-bottom: 2.5rem;
}
.info-block {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.icon {
  font-size: 1.5rem;
}
.info-label {
  font-size: 0.875rem; /* 14px */
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.info-data {
  font-size: 1rem; /* 16px */
  font-weight: 500;
}

.section-title {
  font-size: 1.25rem; /* 20px */
  font-weight: 700;
  margin-bottom: 0.75rem;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 0.5rem;
}
.description-section,
.artists-section {
  margin-bottom: 2rem;
}
.description-section p {
  color: var(--text-secondary);
  line-height: 1.6;
}

.registration-section {
  margin-top: auto; /* Pushes this block to the bottom */
  padding-top: 1rem;
  border-top: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}
.price {
  font-size: 2rem;
  font-weight: 900;
  color: transparent;
  background-image: linear-gradient(to bottom right, #f472b6, #8b5cf6, #22d3ee);
  -webkit-background-clip: text;
  background-clip: text;
}
.register-button {
  display: inline-block;
  text-align: center;
  font-weight: 700;
  color: #fff;
  background-image: linear-gradient(to right, #8b5cf6, #f472b6);
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  flex-grow: 1;
}
.register-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 15px -3px rgba(139, 92, 246, 0.3),
    0 4px 6px -2px rgba(244, 114, 182, 0.2);
}

.error-message {
  text-align: center;
  padding: 5rem 1rem;
}
.error-message h2 {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 1rem;
}
.error-message p {
  color: var(--text-secondary);
  margin-bottom: 2rem;
}

/* --- Responsive Layout --- */
@media (min-width: 768px) {
  /* md breakpoint */
  .event-detail-page {
    padding: 4rem;
  }
  .detail-grid,
  .loading-skeleton {
    grid-template-columns: 1fr 1fr; /* Two equal columns */
  }
  .event-title {
    font-size: 3rem; /* 48px */
  }
  .register-button {
    flex-grow: 0;
  }
}
</style>
