<template>
    <div>
        <CyclePage :cycle='movableDates[0]'/>
        <CyclePage :cycle='movableDates[1]'/>
        <CycleNum3Page :cycle='movableDates[2]'/>
    </div>
</template>

<script>

import CyclePage from "@/components/CyclePage.vue";
import CycleNum3Page from "@/components/CycleNum3Page.vue";

export default {

    components: {CyclePage, CycleNum3Page},

    props: {
        movableDates: {
            type: Object,
            required: true,
        },
    },
}
</script>

