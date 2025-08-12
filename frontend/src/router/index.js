import { createRouter, createWebHistory } from "vue-router";

// --- Route Components ---
// Components are now lazy-loaded using dynamic imports.
// This means the code for a page is only downloaded by the browser when it's
// actually visited, leading to a faster initial app load time.
const Home = () => import("../pages/Home.vue");
const EventDetail = () => import("../pages/EventDetail.vue");
const Register = () => import("../pages/Register.vue");
const Confirmation = () => import("../pages/Confirmation.vue");

// --- Route Definitions ---
const routes = [
  {
    path: "/",
    name: "Home", // ✅ Naming routes is a best practice
    component: Home,
  },
  {
    path: "/events/:id",
    name: "EventDetail", // Makes programmatic navigation easier (e.g., router.push({ name: 'EventDetail' }))
    component: EventDetail,
    props: true,
  },
  {
    path: "/events/:id/register",
    name: "Register",
    component: Register,
    props: true,
  },
  {
    path: "/confirmation",
    name: "Confirmation",
    component: Confirmation,
  },
];

// --- Router Instance ---
const router = createRouter({
  history: createWebHistory("/app/"), // Base path for the app
  routes,

  // ✅ This function handles scroll position on navigation.
  // It ensures that the user is scrolled to the top of the new page.
  scrollBehavior(to, from, savedPosition) {
    // If the user is going back/forward, use their saved scroll position
    if (savedPosition) {
      return savedPosition;
    }
    // Otherwise, scroll to the top of the page
    return { top: 0, behavior: "smooth" };
  },
});

export default router;
