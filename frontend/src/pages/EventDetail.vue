<template>
  <div v-if="event" class="p-6">
    <img :src="event.image" class="w-full max-w-2xl mb-4 rounded-lg" />
    <h1 class="text-3xl font-bold">{{ event.title }}</h1>
    <p class="text-gray-600">
      {{ new Date(event.date).toLocaleString() }} - {{ event.location }}
    </p>
    <p class="mt-4">{{ event.description }}</p>
    <p class="mt-2 font-semibold">Artists: {{ event.artists.join(", ") }}</p>
    <p class="mt-2 font-bold">Price: €{{ event.price }}</p>

    <router-link
      :to="`/events/${event.id}/register`"
      class="mt-4 inline-block bg-blue-500 text-white px-4 py-2 rounded"
    >
      Register Now
    </router-link>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["id"],
  data() {
    return { event: null };
  },
  async created() {
    const res = await axios.get(`http://127.0.0.1:8000/api/events/${this.id}`);
    this.event = res.data;
  },
};
</script>
