import { defineStore } from "pinia";

export const useMessageStore = defineStore("messages", () => {
  const messages = ref([]);
  function addMessage(value) {
    messages.value.push(value);
  }
  function deleteMessage(index) {
    messages.value.splice(index, 1);
  }
  function clear() {
    messages.value = [];
  }
  return {
    messages,
    addMessage,
    deleteMessage,
    clear,
  };
});
