<template>
  <div>
    <FormManuscriptsSearch
      @getItems="getManuscripts"
      :manuscriptsSearchData="manuscriptsSearchData"
      :search="$route.query.search"
      :fund__title="$route.query.fund__title"
      :fund__library="$route.query.fund__library"
      :y__year__gte="$route.query.y__year__gte"
      :y__year__lt="$route.query.y__year__lt"
      @update:search="replaceRouterQuery( {search: $event})"
      @update:fund__title="replaceRouterQuery({fund__title: $event})"
      @update:fund__library="replaceRouterQuery({fund__library: $event})"
      @update:y__year__gte="replaceRouterQuery( {y__year__gte: $event})"
      @update:y__year__lt="replaceRouterQuery(  {y__year__lt: $event})"
    />
    <NumItems :numItems="manuscripts.total" />
    <ContainerManuscripts :manuscripts="manuscripts.items" />
  </div>
</template>

<script>


import { api } from "@/services/api";
import ContainerManuscripts from "@/components/manuscript/manuscripts/ContainerManuscripts.vue";
import { replaceRouterQuery, scroll } from "@/utils/common";
import FormManuscriptsSearch from "@/components/manuscript/manuscripts_search/FormManuscriptsSearch.vue";
import NumItems from "@/components/common/NumItems.vue";


export default {
  components: {
    NumItems,
    FormManuscriptsSearch,
    ContainerManuscripts
  },
  props: {
    manuscriptsSearchData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      manuscripts: {
        type: Object,
        required: true
      },
      page: {
        type: Number,
        required: true
      }
    };
  },
  computed: {
    apiGetManuscripts() {
      return api.getManuscripts({
          page: this.page,
          search: this.$route.query.search,
          fund__title: this.$route.query.fund__title,
          fund__library: this.$route.query.fund__library,
          y__year__gte: this.$route.query.y__year__gte,
          y__year__lt: this.$route.query.y__year__lt
        }
      );
    }
  },
  watch: {
    "$route.query": function(newVal, oldVal) {
      this.getManuscripts();
    }
  },
  beforeMount() {
    this.getManuscripts();
  },
  mounted() {
    scroll(this.getManuscriptsPage);
  },
  methods: {
    replaceRouterQuery,
    getManuscriptsPage() {
      this.page += 1;
      this.apiGetManuscripts.then((response) => (this.manuscripts.items = this.manuscripts.items?.concat(response.data.items)));
    },
    getManuscripts() {
      this.page = 1;
      this.apiGetManuscripts.then((response) => (this.manuscripts = response.data));
    }
  }
};
</script>



