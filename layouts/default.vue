<template>
    <nav>
        <div class="container flex flex-wrap gap-4 justify-between">
            <div class="flex flex-wrap gap-12 flex-grow-[1]">
                <NuxtLink class="flex gap-3 justify-center items-center" to="/">
                    <img :src="logo" alt="">
                    <b class="flex gap-1">
                        <span class=" text-indigo-500">Books</span>
                        <span class="text-white">List</span>
                    </b>
                </NuxtLink>
                <div ref="search"
                    class="search-box md:left-0 left-[5%] flex absolute -top-12 md:top-0 md:relative text-black bg-white md:bg-transparent p-2 rounded-md md:rounded-none text z-20 gap-2 w-[90%] md:w-[300px] border-b-[2px] border-white">
                    <input class=" text-black md:text-white flex-grow-[1] bg-transparent border-0 outline-none"
                        placeholder="Search for any training you want " type="text">
                    <button>
                        <Icon size="24px" class="text-black md:text-white" name="ic:round-search" />
                    </button>
                    <button class="flex justify-center items-center md:hidden" @click="searchChnage">
                        <Icon size="24px" class="text-black md:text-white" name="material-symbols:close-rounded" />
                    </button>
                </div>
            </div>
            <div class="flex flex-wrap gap-4">
                <button @click="searchChnage"
                    class="flex md:hidden justify-center items-center w-[40px] h-[40px] bg-white rounded-full">
                    <Icon size="24px" class="text-black mg:text-white" name="ic:round-search" />
                </button>
                <button class="relative flex justify-center items-center w-[40px] h-[40px] bg-white rounded-full">
                    <Icon size="24px" name="material-symbols-light:notifications-outline-sharp" />
                    <span class="absolute top-2 right-2 w-2 h-2 bg-red-500 rounded-full"></span>
                </button>
                <div class="profile-icon">
                    <img :src="avatar" alt="">
                    <ul class="absolute -bottom-10 right-0 bg-white shadow-lg p-2 rounded-md hidden">
                        <li>
                            <button @click="logout" class="text-red-500">Logout</button>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </nav>
    <header>
        <div class="container flex flex-wrap gap-5 justify-between items-center">
            <div class="flex-grow-[1] md:flex-grow-[0] flex flex-col justify-center items-center">
                <h1 class="text-3xl text-white text-center">You’ve got <b class="text-indigo-500">{{ books.books.length }}
                        book</b></h1>
                <p class="text-white text-center">Your task today</p>
            </div>
            <div class="flex flex-col sm:flex-row justify-center items-center gap-3 flex-grow-[1] lg:flex-grow-[0]">
                <label ref="isbn-label" class="p-3 bg-white shadow-md rounded-md" for="">
                    <input @keydown="" ref="isbn" v-model="isbn" class=" outline-none  w-[100%] sm:w-[320px]"
                        placeholder="Enter isbn" type="text">
                    <button @click="clearSearch()" :style="`visibility: ${!isbn ? 'hidden' : 'visible'};`">
                        <Icon size="24px" name="material-symbols-light:cancel-outline" />
                    </button>
                </label>
                <button @click="searchBook" ref="searchbtn"
                    class="relative flex gap-2 justify-center items-center py-3 px-6 rounded-md whitespace-nowrap bg-indigo-500 text-white">
                    <Icon size="24px" name="ic:round-search" />
                    <span>
                        Search book
                    </span>

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
            </div>
        </div>
    </header>
    <slot />
</template>

<script>
import logo from '~/assets/images/logo.svg'
import avatar from '~/assets/images/avatar.svg'
import axios from 'axios'
import { useSearchBook } from '~/stores/searchBook'
import { useBook } from '~/stores/books'

export default {
    data() {
        return {
            isbn: '',
            logo,
            avatar,
            books: useBook(),
        }
    },
    methods: {
        enterSearch() {
            let e = this.$refs.searchbtn
            this.searchBook(e)
        },
        clearSearch() {
            const searchBookStore = useSearchBook()

            this.isbn = ''
            searchBookStore.unsetBook()

        },
        logout() {
            if (process.client) {
                window.localStorage.removeItem('user')
                this.$router.push('signup/')
            }
        },
        async searchBook(e) {
            // formating
            if (!this.isbn) {
                this.$refs['isbn-label'].style = "border: 2px solid red; "
                return
            }
            let button = e.target
            button.setAttribute('disabled', true)
            button.classList.add('load')

            // store
            const searchBookStore = useSearchBook()

            // requesting
            let url = 'https://www.dbooks.org/api/search/' + this.isbn;
            const response = await axios.get(url)
            let data = response.data.books

            console.log(data);

            if (data) {
                searchBookStore.setBook({
                    status: 'found',
                    items: data
                })
            } else {
                searchBookStore.setBook({
                    status: 'notfound'
                })
            }

            console.log(searchBookStore.book);

            // un disabled
            button.removeAttribute('disabled', true)
            button.classList.remove('load')

        },
        searchChnage() {
            let el = this.$refs.search
            el.classList.toggle('active')
        }
    }
}
</script>

<style>
.profile-icon {
    padding: 2px;
    width: 40px;
    height: 40px;
    background: lightgray 50% / cover no-repeat;
    border-radius: 60px;
    border: 2px solid #FD648E;
    background: var(--gradient, conic-gradient(from 180deg at 50% 50%, #FD648E 0deg, #884CB2 178.1249964237213deg, #FD648E 360deg));
    backdrop-filter: blur(15px);
}

.profile-icon:hover ul {
    display: block;
}

.profile-icon img {
    width: 100%;
    height: 100%;
    border-radius: 60px;
}

.search-box {
    transition: 0.3s top;
}

.active {
    top: 13px;
}
</style>