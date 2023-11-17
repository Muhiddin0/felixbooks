import { useMessageStore } from "~/stores/message";
export default defineNuxtRouteMiddleware((to, from) => {
  const messageStore = useMessageStore();
  messageStore.clear();
});
