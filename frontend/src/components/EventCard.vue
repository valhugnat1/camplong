<template>
  <!-- The entire card is now a link to the event's detail page -->
  <router-link
    :to="{ name: 'EventDetail', params: { id: event.id } }"
    class="event-card"
  >
    <div class="card-inner">
      <div class="card-image-wrapper">
        <img :src="event.image" :alt="event.title" class="card-image" />
        <div class="card-price">{{ formattedPrice }}</div>
      </div>

      <div class="card-content">
        <h2 class="card-title">{{ event.title }}</h2>

        <div class="card-info">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="card-icon"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
            />
          </svg>
          <span>{{ formattedDate }}</span>
        </div>

        <div class="card-info">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="card-icon"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
            />
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
            />
          </svg>
          <span>{{ event.location }}</span>
        </div>

        <div class="card-artists">
          <h3 class="artists-title">Line-up</h3>
          <div class="artists-tags">
            <span
              v-for="artist in event.artists"
              :key="artist"
              class="artist-tag"
            >
              {{ artist }}
            </span>
          </div>
        </div>

        <!-- This is now a div styled to look like a button, providing a visual cue -->
        <div class="card-button-wrapper">
          <div class="booking-button">
            <span>Book Your Spot</span>
          </div>
        </div>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: "EventCard",
  props: {
    event: { type: Object, required: true },
  },
  computed: {
    formattedDate() {
      if (!this.event.date) return "";
      const date = new Date(this.event.date);
      // Using 'en-GB' for a more standard DD/MM/YYYY format that is common in Europe
      const options = {
        year: "numeric",
        month: "short",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        hour12: false,
      };
      return new Intl.DateTimeFormat("en-GB", options)
        .format(date)
        .replace(",", " at");
    },
    formattedPrice() {
      return new Intl.NumberFormat("fr-FR", {
        style: "currency",
        currency: "EUR",
      }).format(this.event.price);
    },
  },
};
</script>

<style scoped>
/* ✅ The root element is now a link, so we remove default link styles */
.event-card {
  position: relative;
  padding: 2px; /* Space for the gradient border */
  transition: all 0.3s ease-in-out;
  display: block; /* Ensures the link takes up the full space */
  text-decoration: none; /* Removes underline from link */
  color: inherit; /* Inherits text color */
}

/* The animated gradient border on hover */
.event-card::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 0.8rem;
  background: linear-gradient(120deg, var(--glow-color-1), var(--glow-color-2));
  opacity: 0;
  transition: opacity 0.4s ease-in-out;
  z-index: -1;
}

.event-card:hover {
  transform: translateY(-8px);
}

.event-card:hover::before {
  opacity: 1;
  filter: blur(5px);
}

.card-inner {
  background-color: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(12px);
  border-radius: 0.75rem; /* 12px */
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  height: 100%;
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease-in-out;
}

/* Card Image */
.card-image-wrapper {
  position: relative;
  overflow: hidden;
}

.card-image {
  width: 100%;
  height: 12rem; /* 192px */
  object-fit: cover;
  transition: transform 0.5s ease-in-out;
}

.event-card:hover .card-image {
  transform: scale(1.1);
}

.card-price {
  position: absolute;
  top: 0;
  right: 0;
  margin: 0.75rem; /* 12px */
  padding: 0.25rem 0.75rem;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: white;
  font-size: 0.875rem; /* 14px */
  font-weight: 700;
  border-radius: 9999px;
}

/* Card Content */
.card-content {
  padding: 1.25rem; /* 20px */
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.card-title {
  font-size: 1.5rem; /* 24px */
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #f3f4f6; /* gray-100 */
  transition: color 0.3s;
  /* Truncate text */
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.event-card:hover .card-title {
  color: white;
}

.card-info {
  display: flex;
  align-items: center;
  color: var(--text-secondary);
  font-size: 0.875rem;
  margin-bottom: 0.5rem;
}

.card-info:last-of-type {
  margin-bottom: 1rem;
}

.card-icon {
  height: 1rem; /* 16px */
  width: 1rem;
  margin-right: 0.5rem;
  color: #22d3ee; /* cyan-400 */
}

/* Artists Section */
.card-artists {
  margin-bottom: 1.25rem;
}
.artists-title {
  font-weight: 600;
  color: #e5e7eb; /* gray-200 */
  margin-bottom: 0.5rem;
}
.artists-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.artist-tag {
  padding: 0.25rem 0.75rem;
  background-color: rgba(34, 211, 238, 0.1);
  color: #67e8f9; /* cyan-300 */
  font-size: 0.75rem; /* 12px */
  font-weight: 500;
  border-radius: 9999px;
  border: 1px solid rgba(34, 211, 238, 0.2);
}

/* Button */
.card-button-wrapper {
  margin-top: auto; /* Pushes button to the bottom */
}

/* ✅ This is now a div, but it keeps the button styles for a consistent look */
.booking-button {
  width: 100%;
  padding: 12px 24px;
  text-align: center;
  border: none;
  color: white;
  font-weight: 700;
  border-radius: 0.5rem;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  background: linear-gradient(90deg, #be185d, #7e22ce);
  transition: all 0.3s ease;
  z-index: 1;
}

.booking-button::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.3),
    transparent
  );
  transition: left 0.5s ease;
  z-index: -1;
}

.event-card:hover .booking-button {
  transform: scale(1.05);
  box-shadow: 0 0 15px rgba(236, 72, 153, 0.6), 0 0 15px rgba(139, 92, 246, 0.6);
}

.event-card:hover .booking-button::before {
  left: 100%;
}
</style>
