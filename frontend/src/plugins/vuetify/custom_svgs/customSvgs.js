import { h } from "vue";
import VelikijPrazdnik from "@/plugins/vuetify/custom_svgs/tipikon_svgs/VelikijPrazdnik.vue";
import SrednijPrazdnik from "@/plugins/vuetify/custom_svgs/tipikon_svgs/SrednijPrazdnik.vue";
import MalyjPrazdnik from "@/plugins/vuetify/custom_svgs/tipikon_svgs/MalyjPrazdnik.vue";


const customSvgNameToComponent = {
  VelikijPrazdnik, SrednijPrazdnik, MalyjPrazdnik
};

const customSVGs = {
  component: (props) => h(customSvgNameToComponent[props.icon])
};

export { customSVGs /* aliases */ };