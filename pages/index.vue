<template>
    <!-- searching -->
    <section v-if="searchbook.book.status == 'found'">
        <div class="container flex flex-wrap justify-around gap-5">
            <CardSearch :item="item" :key="index" v-for="item, index in searchbook.book.items" />
        </div>
    </section>
    <section v-else-if="searchbook.book.status == 'notfound'">
        <div class="container flex flex-col gap-1 justify-center items-center min-h-[60vh]">
            <h1 class="text-4xl text-indigo-500 font-[cursive] text-center">Book not found</h1>
            <img class="w-[450px]" src="~/assets/images/notresult.svg" alt="">
        </div>
    </section>

    <!-- loading books -->
    <Loading v-if="loading_books" />
    <section v-else-if="books.books.length && searchbook.book.status == 'notsearch'">
        <div class="container flex flex-wrap justify-around items-center gap-5">
            <Card :item="item" v-for="item, index in books.books" />
        </div>
    </section>
    <EmptyUserBooks v-else-if="!books.books.values.length && searchbook.book.status == 'notsearch'" />

    <!-- messages -->
    <div class="fixed flex flex-col gap-3 bottom-0 z-50 p-3 w-[320px] " v-for="message, index in store.messages">
        <Message :message="message" :index="index" />
    </div>


    <!-- congratulations -->
    <cong v-if="cong.status" />

    <!-- bg image -->
    <div class="bg" :style="{ background: `url(${bg})` }"></div>
</template>

<script>
import bg from '~/assets/images/bg.svg'
import { useMessageStore } from '~/stores/message'
import { useCong } from '~/stores/cong'
import { useSearchBook } from '~/stores/searchBook'
import { useBook } from '~/stores/books'
import http from '~/services/http/init'

export default {
    async beforeCreate() {
        if (process.client) {
            const bookStore = useBook()
            let user = JSON.parse(window.localStorage.getItem('user'))

            if (!user) {
                this.$router.push('signup/')
                return
            }

            const headers = {
                Key: user.key,
                Sign: Secret("GET", "/books", "", user.secret),
            };
            const response = await http.get("/books", { headers: headers })
            let data = response.data.data
            if (data) {
                bookStore.setBook(data)
            }
            this.loading_books = false
        }
    },
    data() {
        return {
            bg,
            store: useMessageStore(),
            cong: useCong(),
            searchbook: useSearchBook(),
            books: useBook(),
            loading_books: true
        }
    }
}
</script>

<style></style>