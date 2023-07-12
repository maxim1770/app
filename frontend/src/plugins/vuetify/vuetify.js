import * as directives from "vuetify/directives";
import * as components from "vuetify/components";
import { createVuetify } from "vuetify";
import { mdi } from "vuetify/iconsets/mdi";
import colors from "vuetify/lib/util/colors";

import "vuetify/styles";
import "@mdi/font/css/materialdesignicons.css";
import { customSVGs } from "@/plugins/vuetify/custom_svgs/customSvgs";

const myCustomLightTheme = {
  dark: false,
  colors: {
    background: "#FFFFFF",
    surface: "#FFFFFF",
    primary: colors.red.darken3,
    "primary-darken-1": colors.red.darken1,
    secondary: colors.red.lighten3,
    "secondary-darken-1": colors.red.lighten1,
    error: "#B00020",
    info: "#2196F3",
    success: "#4CAF50",
    warning: "#FB8C00"
  }
};


const vuetify = createVuetify({
  components, directives, display: {
    mobileBreakpoint: "sm", thresholds: {
      xs: 0, sm: 340, md: 540, lg: 800, xl: 1280
    }
  },
  // theme: {
  //   defaultTheme: "light"  // dark
  // }
  theme: {
    defaultTheme: "myCustomLightTheme",
    themes: {
      myCustomLightTheme
    }
  },
  defaults: {
    VChip: {
      variant: "outlined"
    },
    VChipGroup: {
      variant: "outlined"
    },
  },
  icons: {
    defaultSet: "mdi",
    sets: {
      mdi,
      custom: customSVGs,
    },
  },
});



export default vuetify;
