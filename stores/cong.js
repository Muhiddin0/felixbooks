import { defineStore } from "pinia";

export const useCong = defineStore("cong", () => {
  const status = ref(false);
  function setValue(value) {
    status.value = value;
  }
  return {
    status,
    setValue,
  };
});
