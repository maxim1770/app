<template>
  <span
    v-if="manuscript?.fund"
  >
    <ListItemFund :manuscript="manuscript" />
    <ListItemNebFund :neb_url="manuscript?.neb_url" />
  </span>
  <ListItemLlsUrl
    v-else
    :manuscript_url="manuscript?.url"
  />
</template>

<script>


import ListItemFund from "@/components/manuscript/fund/_ListItemFund.vue";
import ListItemNebFund from "@/components/manuscript/fund/_ListItemNebFund.vue";
import ListItemLlsUrl from "@/components/manuscript/fund/_ListItemLlsUrl.vue";


export default {
  components: { ListItemLlsUrl, ListItemFund, ListItemNebFund },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  }
};

</script>



