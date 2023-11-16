import { defineStore } from "pinia";

export const useSearchBook = defineStore("searchbook", () => {
  const book = ref({
    status: "notsearch",
  });
  function setBook(value) {
    book.value = value;
  }
  function unsetBook() {
    book.value = {
      status: "notsearch",
    };
  }
  return {
    book,
    setBook,
    unsetBook,
  };
});
