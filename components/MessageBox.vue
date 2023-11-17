<template>
    <section class="fixed left-[-340px] flex flex-col-reverse gap-3 bottom-0 z-50 p-3 w-[320px] h-screen">
        <Message v-for="message, index in messages.messages" :message="message" :index="index" />
    </section>
</template>

<script>
import { useMessageStore } from '~/stores/message'

export default {
    data() {
        return {
            messages: useMessageStore()
        }
    }
}
</script>

<style lang="scss" scoped></style>