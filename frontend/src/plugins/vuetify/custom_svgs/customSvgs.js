import { h } from "vue";
import VelikijPrazdnik from "@/plugins/vuetify/custom_svgs/tipikon_svgs/VelikijPrazdnik.vue";
import SrednijPrazdnikVsenoschnoeBdenie
  from "@/plugins/vuetify/custom_svgs/tipikon_svgs/SrednijPrazdnikVsenoschnoeBdenie.vue";
import SrednijPrazdnik from "@/plugins/vuetify/custom_svgs/tipikon_svgs/SrednijPrazdnik.vue";
import MalyjPrazdnikSlavoslovnajaSluzhba
  from "@/plugins/vuetify/custom_svgs/tipikon_svgs/MalyjPrazdnikSlavoslovnajaSluzhba.vue";
import MalyjPrazdnik from "@/plugins/vuetify/custom_svgs/tipikon_svgs/MalyjPrazdnik.vue";
import OrthodoxCross from "@/plugins/vuetify/custom_svgs/common_custom_svgs/OrthodoxCross.vue";
import tg from "@/plugins/vuetify/custom_svgs/common_custom_svgs/tg.vue";


const customSvgNameToComponent = {
  VelikijPrazdnik,
  SrednijPrazdnikVsenoschnoeBdenie,
  SrednijPrazdnik,
  MalyjPrazdnikSlavoslovnajaSluzhba,
  MalyjPrazdnik,
  OrthodoxCross,
  tg
};

const customSVGs = {
  component: (props) => h(customSvgNameToComponent[props.icon])
};

export { customSVGs /* aliases */ };