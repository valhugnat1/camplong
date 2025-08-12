import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueDevTools from "vite-plugin-vue-devtools";

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), vueDevTools()],
  base: "/app/",
  server: {
    proxy: {
      // Proxying requests starting with /api
      "/api": {
        target: "http://127.0.0.1:8000", // Your backend server
        changeOrigin: true, // Needed for virtual hosted sites
        // The rewrite is not needed if your backend API endpoints
        // already start with /api (which they do in your case)
        // rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
