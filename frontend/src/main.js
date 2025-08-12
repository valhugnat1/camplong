// src/main.js

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// Add this line to import your new CSS file
import "./assets/main.css"; // Adjust the path if you saved it elsewhere

const app = createApp(App);

app.use(router);

app.mount("#app");
