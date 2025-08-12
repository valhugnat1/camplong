<template>
  <div class="register-page">
    <div v-if="loading" class="loading-message">
      <div class="pulse">🕺 Loading... 💃</div>
    </div>

    <div v-if="event && !loading" class="form-container">
      <!-- Event Header -->
      <div class="event-header">
        <p class="header-subtitle">You are registering for</p>
        <h1 class="header-title">
          <span>{{ event.title }}</span>
        </h1>
      </div>

      <!-- Registration Form -->
      <form @submit.prevent="register">
        <div class="form-group">
          <label for="name" class="form-label">Full Name</label>
          <input
            id="name"
            v-model="name"
            type="text"
            class="form-input"
            placeholder="e.g., Jean Dupont"
            required
            :disabled="submitting"
          />
        </div>

        <div class="form-group">
          <label for="email" class="form-label">Email Address</label>
          <input
            id="email"
            v-model="email"
            type="email"
            class="form-input"
            placeholder="you@example.com"
            required
            :disabled="submitting"
          />
        </div>

        <!-- Submission Error Message -->
        <div v-if="error" class="error-message">
          {{ error }}
        </div>

        <button type="submit" class="submit-button" :disabled="submitting">
          <!-- Show spinner when submitting -->
          <div v-if="submitting" class="spinner"></div>
          <!-- Show text otherwise -->
          <span v-else
            >Confirm Registration (€{{ event.price.toFixed(2) }})</span
          >
        </button>
      </form>
    </div>

    <div v-if="fetchError" class="loading-message">
      <p>Could not find the event.</p>
      <router-link
        to="/"
        class="submit-button"
        style="text-decoration: none; margin-top: 1rem"
        >Back to Home</router-link
      >
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Register",
  props: ["id"],
  data() {
    return {
      event: null,
      name: "",
      email: "",
      loading: true,
      submitting: false,
      error: null, // For submission errors
      fetchError: false, // For initial data fetch errors
    };
  },
  async created() {
    try {
      // ✅ Fetch event data to display info like title and price
      const res = await axios.get(`/api/events/${this.id}`);
      this.event = res.data;
    } catch (err) {
      console.error("Failed to fetch event for registration:", err);
      this.fetchError = true;
    } finally {
      this.loading = false;
    }
  },
  methods: {
    async register() {
      this.submitting = true;
      this.error = null;
      try {
        // ✅ Use a relative path for the API call
        await axios.post(`/api/events/${this.id}/register`, {
          name: this.name,
          email: this.email,
        });
        // On success, redirect to the confirmation page
        this.$router.push({ name: "Confirmation" });
      } catch (err) {
        console.error("Registration failed:", err);
        this.error = "Registration failed. Please try again later.";
      } finally {
        this.submitting = false;
      }
    },
  },
};
</script>

<style scoped>
.register-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.form-container {
  width: 100%;
  max-width: 480px;
  background-color: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 0.75rem;
  padding: 2.5rem;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}

/* --- Event Header --- */
.event-header {
  text-align: center;
  margin-bottom: 2.5rem;
}
.header-subtitle {
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-size: 0.875rem;
}
.header-title {
  font-size: 2.25rem;
  font-weight: 900;
  letter-spacing: -0.05em;
  line-height: 1.1;
  margin-top: 0.25rem;
}
.header-title span {
  background-image: linear-gradient(to bottom right, #f472b6, #8b5cf6, #22d3ee);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

/* --- Form Elements --- */
.form-group {
  margin-bottom: 1.5rem;
}
.form-label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #e5e7eb; /* gray-200 */
}
.form-input {
  width: 100%;
  background-color: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 0.5rem;
  padding: 0.75rem 1rem;
  color: white;
  font-size: 1rem;
  transition: border-color 0.3s, box-shadow 0.3s;
}
.form-input::placeholder {
  color: #9ca3af; /* gray-400 */
}
.form-input:focus {
  outline: none;
  border-color: #8b5cf6; /* purple-500 */
  box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.3);
}
.form-input:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* --- Button & Messages --- */
.submit-button {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1.5rem;
  border: none;
  color: white;
  font-weight: 700;
  font-size: 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  background: linear-gradient(90deg, #be185d, #7e22ce);
  transition: all 0.3s ease;
}
.submit-button:hover:not(:disabled) {
  transform: scale(1.02);
  box-shadow: 0 0 20px rgba(236, 72, 153, 0.5);
}
.submit-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error-message {
  color: #fca5a5; /* red-300 */
  background-color: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
  padding: 0.75rem;
  border-radius: 0.5rem;
  text-align: center;
  margin-bottom: 1.5rem;
}

.loading-message {
  text-align: center;
  color: var(--text-secondary);
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

.spinner {
  border: 3px solid rgba(255, 255, 255, 0.3);
  border-top: 3px solid white;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  animation: spin 1s linear infinite;
}
@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
