import AOS from "aos";

import "aos/dist/aos.css";

export default ({ app }) => {
  AOS.init({ disable: "phone" }); // eslint-disable-line new-cap
};
