<template>
    <div class="container flex justify-center items-center min-h-screen">
        <form class="flex flex-col gap-8 w-[100%] sm:w-[530px] p-5 bg-white rounded-md shadow-md" action="">

            <h1 class="text-center text-4xl ">Login</h1>

            <div class="flex flex-col gap-5">
                <button class="flex justify-center items-center p-2 rounded-md w-[100%] gap-5 border-[2px] border-black">
                    <img :src="google" alt="">
                    Continue with Google
                </button>
                <button class="flex justify-center items-center p-2 rounded-md w-[100%] gap-5 border-[2px] border-black">
                    <img :src="facebook" alt="">
                    Continue with Facebook
                </button>
            </div>

            <div class="flex justify-center items-center relative">
                <span class="absolute border-[1px] border-black w-[100%] h-0"></span>
                <b class="relative bg-white px-6 text-md">OR</b>
            </div>

            <div class="flex flex-col gap-3">
                <label ref="name" class="flex-grow-[1]" for="">
                    <p>Your name</p>
                    <div class="shadow-md border-[1px] border-stone-400 w-[100%] rounded-md p-2">
                        <input @keypress="removeError('name')" v-model="name" class="outline-none w-full" type="text"
                            name="">
                    </div>
                </label>

                <label ref="username" class="flex-grow-[1]" for="">
                    <p>Username</p>
                    <div class="shadow-md border-[1px] border-stone-400 w-[100%] rounded-md p-2">
                        <input @keypress="removeError('username')" v-model="username" class="outline-none w-full"
                            type="text" name="">
                    </div>
                </label>
                <label ref="email" class="flex-grow-[1]" for="">
                    <p>Email</p>
                    <div class="shadow-md border-[1px] border-stone-400 w-[100%] rounded-md p-2">
                        <input @keypress="removeError('email')" v-model="email" class="outline-none w-full" type="email"
                            name="">
                    </div>
                </label>
                <label ref="password" class="" for="">
                    <p>Your password</p>
                    <div class="flex shadow-md border-[1px] border-stone-400 w-[100%] rounded-md p-2">
                        <input @keypress="removeError('password')" v-model="password"
                            class="outline-none flex-grow-[2] w-full" :type="password_show ? 'text' : 'password'" name="">
                        <button @click="() => password_show = !password_show" type="button">
                            <Icon v-if="password_show" size="24px" name="mdi:eye-outline" />
                            <Icon v-else size="24px" name="mdi:eye-off-outline" />
                        </button>
                    </div>
                </label>
            </div>

            <button @click="submitForm"
                class="relative cursor-pointer bg-indigo-500 py-3 text-center text-white w-[100%] rounded-md hover:opacity-75 transition">
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
                Sign up
            </button>
            <p class="text-center">
                Already signed up?
                <NuxtLink to="/signup" class="text-indigo-500">Go to sign up.</NuxtLink>
            </p>
        </form>
    </div>

    <MessageBox />

    <div class="bg" :style="{ background: `url(${bg})` }"></div>
</template>

<script>
import google from '~/assets/images/google.svg'
import facebook from '~/assets/images/facebook.svg'
import bg from '~/assets/images/bg.svg'
import http from '~/services/http/init'
import { useMessageStore } from '~/stores/message'
import { useCong, } from '~/stores/cong'
import { Secret } from '~/utils/secret'

export default {
    data() {
        return {
            bg,
            google,
            facebook,
            password_show: false,
            name: '',
            username: '',
            email: '',
            password: '',
            store: useMessageStore()
        }
    },
    methods: {
        removeError(item) {
            this.$refs[item].classList.remove('error')
        },
        formValid() {
            let status = false

            if (!this.name) {
                this.$refs.name.classList.add('error')
                status = false
            } else status = true
            if (!this.username) {
                this.$refs.username.classList.add('error')
                status = false
            } else status = true
            if (!this.email) {
                this.$refs.email.classList.add('error')
                status = false
            } else status = true
            if (!this.password) {
                this.$refs.password.classList.add('error')
                status = false
            } else status = true

            return status
        },

        async submitForm(e) {
            e.preventDefault()

            if (!this.formValid()) return

            const messageStore = useMessageStore()
            const congStore = useCong()


            let button = e.target
            button.setAttribute('disabled', true)
            button.classList.add('load')

            const data = {
                name: this.name,
                email: this.email,
                key: this.username,
                secret: this.password,
            };
            const headers = {
                Key: this.username,
                Sign: Secret("GET", "/myself", "", this.password),
            };
            await http
                .get(
                    "/myself",
                    {
                        headers: headers,
                    },
                    data
                )
                .then((response) => {
                    window.localStorage.setItem("user", JSON.stringify(response.data.data));
                    this.$router.push("/");

                    congStore.setValue(true)

                    messageStore.addMessage(
                        {
                            head: 'Succes',
                            body: "you succesfully Login"
                        }
                    )
                })
                .catch((error) => {
                    messageStore.addMessage(
                        {
                            head: 'Succes',
                            body: error.response.data.message
                        }
                    )
                });

            button.removeAttribute('disabled', false)
            button.classList.remove('load')
        }
    },
    setup() {
        definePageMeta({
            layout: false,
        })
    }
}

</script>

<style scoped>
.loading {
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    border-radius: 16px;
    display: none;
    @apply bg-indigo-500;
}

.load .loading {
    display: flex;
    cursor: not-allowed;
}

.error div {
    border: 1px solid red;
}

load .error div input {
    color: #f00;
}
</style>