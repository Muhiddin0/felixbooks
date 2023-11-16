<template>
    <section>
        <div class="container flex flex-wrap justify-around items-center gap-5">
            <Card />
            <Card />
            <Card />
            <Card />
            <Card />
            <Card />
            <Card />
            <Card />
            <Card />
        </div>
    </section>
    <canvas id="my-canvas"></canvas>
    <div class="fixed flex flex-col gap-3 bottom-0 z-50 p-3 w-[320px] " v-for="message, index in store.messages">
        <Message :message="message" :index="index" />
    </div>

    <cong v-if="cong.status" />

    <div class="bg" :style="{ background: `url(${bg})` }"></div>
</template>

<script>
import bg from '~/assets/images/bg.svg'
import { useMessageStore } from '~/stores/message'
import { useCong } from '~/stores/cong'


export default {
    methods: {
        start() {
            // this.$confetti.start();
            console.log(this.$confetti);
        }
    },
    data() {
        return {
            bg,
            store: useMessageStore(),
            cong: useCong()
        }
    }
}
</script>

<style></style>