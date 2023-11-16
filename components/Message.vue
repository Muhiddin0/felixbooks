<template>
    <div ref="message" class="relative w-[300px] bg-white rounded-sm border-l-4 p-4 shadow-md border-indigo-500 text-black"
        role="alert">
        <p class="font-bold">{{ message.head }}</p>
        <p>{{ message.body }}</p>
        <span class="timer absolute left-0 bottom-0 w-[100%] h-1 bg-indigo-500 block"></span>
    </div>
</template>

<script>

export default {
    mounted() {
        setTimeout(() => {
            this.$refs.message.remove()
        }, 3000)
    },
    props: ['message', 'index']
}
</script>

<style scoped>
.timer {
    animation: timer 3s 1 linear;
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