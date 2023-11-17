<template>
    <div ref="message"
        class="message relative w-[300px] bg-white rounded-sm border-l-4 p-4 shadow-md border-indigo-500 text-black"
        role="alert">
        <p class="font-bold">{{ message.head }}</p>
        <p>{{ message.body }}</p>
        <span class="timer absolute left-0 bottom-0 w-[100%] h-1 bg-indigo-500 block"></span>
    </div>
</template>

<script>
import { useMessageStore } from '~/stores/message'

export default {
    mounted() {
        const messageStore = useMessageStore()
        setTimeout(() => {
            this.$refs.message.remove()
            let index = this.$props.index
            messageStore.deleteMessage(index)
            console.log(messageStore.messages);
        }, 3000);
    },
    props: ['message', 'index']
}
</script>

<style scoped>
.message {
    position: relative;
    left: 0px;
    animation: loader 3.4s cubic-bezier(0, 1.4, 0.99, 1.13) 1;
}


@keyframes loader {
    0% {
        left: 0px;
    }

    10% {
        left: 340px;
    }

    90% {
        left: 340px;
    }

    100% {
        left: 0px;
    }
}

.timer {
    animation: timer 3s 1 linear;
    width: 0%;
}

@keyframes timer {
    0% {
        width: 100%;
    }

    100% {
        width: 0%;
    }
}
</style>