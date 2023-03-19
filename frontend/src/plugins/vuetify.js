// Vuetify
import * as directives from "vuetify/directives";
import * as components from "vuetify/components";
import {createVuetify} from "vuetify";

// Styles
import "vuetify/styles";
import "@mdi/font/css/materialdesignicons.css";

const vuetify = createVuetify({
    components,
    directives,
    display: {
        mobileBreakpoint: "sm",
        thresholds: {
            xs: 0,
            sm: 340,
            md: 540,
            lg: 800,
            xl: 1280,
        },
    },
});

export default vuetify;
