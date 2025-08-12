import { createRouter, createWebHistory } from "vue-router";
import Home from "../pages/Home.vue";
import EventDetail from "../pages/EventDetail.vue";
import Register from "../pages/Register.vue";
import Confirmation from "../pages/Confirmation.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/events/:id", component: EventDetail, props: true },
  { path: "/events/:id/register", component: Register, props: true },
  { path: "/confirmation", component: Confirmation },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
