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
                            <button class="text-red-500">Logout</button>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </nav>
    <header>
        <div class="container flex flex-wrap gap-5 justify-between items-center">
            <div class="flex-grow-[1] md:flex-grow-[0] flex flex-col justify-center items-center">
                <h1 class="text-3xl text-white text-center">You’ve got <b class="text-indigo-500">7 book</b></h1>
                <p class="text-white text-center">Your task today</p>
            </div>
            <div class="flex flex-col sm:flex-row justify-center items-center gap-3 flex-grow-[1] lg:flex-grow-[0]">
                <input class="p-3 outline-none bg-white shadow-md rounded-md w-[100%] sm:w-[320px]"
                    placeholder="Enter your name" type="text">
                <button class="py-3 px-6 rounded-md whitespace-nowrap bg-indigo-500 text-white">
                    <Icon name="material-symbols:add" />
                    Create a book
                </button>
            </div>
        </div>
    </header>
    <slot />
</template>

<script>
import logo from '~/assets/images/logo.svg'
import avatar from '~/assets/images/avatar.svg'

export default {
    data() {
        return {
            logo,
            avatar
        }
    },
    methods: {
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