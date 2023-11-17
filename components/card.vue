<template>
    <div ref="card"
        class="flex flex-col justify-center items-center gap-3 p-5 w-[100%] xsm:w-[300px] bg-white rounded-md shadow-md">
        <img height="200px" class="w-[150px] rounded-md" :src="item.book.image" alt="">
        <b class="text-xl text-center">{{ item.book.title }}</b>
        <p>{{ item.book.author }}</p>

        <div class="flex flex-wrap gap-3 justify-between">
            <button @click="(e) => deleteBook(e, item.book.id)"
                class="relative p-2 border-indigo-500 border-[1px] rounded-md text-indigo-500">
                Remove
                <span class="loading">
                    <svg aria-hidden="true" class="w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
                        viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                            fill="currentColor" />
                        <path
                            d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                            fill="currentFill" />
                    </svg>
                </span>
            </button>
            <p class="flex justify-center items-center px-4  text-white bg-indigo-500 rounded-md">{{ item.book.pages }}
                pages</p>
        </div>
    </div>
</template>
<script>
import http from '~/services/http/init';
import { useMessageStore } from '~/stores/message';
import { useBook } from '~/stores/books';

export default {
    data() {
        return {
            user: ''
        }
    },
    beforeMount() {
        if (process.client) {
            var user = JSON.parse(window.localStorage.getItem('user'))
            this.user = user
        }
    },
    methods: {

        async refreshBooks() {

            const bookStore = useBook()

            const headers = {
                Key: this.user.key,
                Sign: Secret("GET", "/books", "", this.user.secret),
            };
            const response = await http.get("/books", { headers: headers })
            let data = response.data.data
            if (data) {
                bookStore.setBook(data)
            }
        },

        async deleteBook(e, id) {

            let button = e.target
            button.setAttribute('disabled', true)
            button.classList.add('loadmini')

            const messageStore = useMessageStore()

            let headers = {
                Key: this.user.key,
                Sign: Secret("DELETE", "/books/" + id, "", this.user.secret),
            };

            try {
                const response = await http.delete("/books/" + id, { headers: headers });
                messageStore.addMessage({
                    head: 'Succes',
                    body: "This Book remove your library"
                })
                this.refreshBooks()

            } catch {
                messageStore.addMessage({
                    head: 'Succes',
                    body: "This Book remove your library"
                })
            }

            button.removeAttribute('disabled', true)
            button.classList.remove('loadmini')

        },
        async addBook(e, id) {

            let button = e.target
            button.setAttribute('disabled', true)
            button.classList.add('loadmini')

            let data = JSON.stringify({
                isbn: id,
            });
            const messageStore = useMessageStore()

            let headers = {
                Key: this.user.key,
                Sign: Secret("POST", "/books", data, this.user.secret),
                "Content-Type": "application/json",
            };


            try {
                const result = await http.post("/books", data, { headers: headers })
                messageStore.addMessage({
                    head: 'Succesfuly',
                    body: "Book succesfully add your library"
                })
            } catch {
                messageStore.addMessage({
                    head: 'Faill',
                    body: "This Book alred add your library"
                })
            }

            button.removeAttribute('disabled', true)
            button.classList.remove('loadmini')
        }
    },
    props: ['item', 'index']
}
</script>

<style lang="scss" scoped></style>