import { defineStore } from "pinia";

export const useBook = defineStore("book", () => {
  const books = ref([]);
  function setBook(value) {
    books.value = value;
  }
  function unsetBook(index) {
    books.value.slice(index, 1);
  }

  return {
    books,
    setBook,
    unsetBook,
  };
});
