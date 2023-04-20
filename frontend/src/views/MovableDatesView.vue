<template>
    <MovableDatesPage :movableDates='movableDates' v-if='movableDates[0]'/>
</template>

<script>
import {api} from "@/api";
import MovableDatesPage from "@/components/MovableDatesPage.vue";

export default {
    components: {MovableDatesPage},

    data() {
        return {
            movableDates: {
                type: Object,
                required: true,
            },
        };
    },
    mounted() {
        api
            .getMovableDates()
            .then((response) => (this.movableDates = response.data));
    },
};
</script>
