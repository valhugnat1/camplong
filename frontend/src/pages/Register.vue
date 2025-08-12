<template>
  <div class="p-6 max-w-lg mx-auto">
    <h1 class="text-2xl font-bold mb-4">Register for Event</h1>
    <form @submit.prevent="register">
      <div class="mb-4">
        <label class="block font-semibold">Name</label>
        <input v-model="name" class="border p-2 w-full rounded" required />
      </div>
      <div class="mb-4">
        <label class="block font-semibold">Email</label>
        <input
          v-model="email"
          type="email"
          class="border p-2 w-full rounded"
          required
        />
      </div>
      <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">
        Confirm Registration
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["id"],
  data() {
    return { name: "", email: "" };
  },
  methods: {
    async register() {
      await axios.post(`http://127.0.0.1:8000/api/events/${this.id}/register`, {
        name: this.name,
        email: this.email,
      });
      this.$router.push("/confirmation");
    },
  },
};
</script>
