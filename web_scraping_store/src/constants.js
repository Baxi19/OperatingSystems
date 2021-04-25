import axios from "axios";
import { createMuiTheme } from "@material-ui/core/styles";

export const theme = createMuiTheme({
  typography: {
    fontFamily: "Segoe UI Symbol",
  },
  palette: {
    primary: {
      light: "#8eafff",
      main: "#5680e9",
      dark: "#0054b6",
      contrastText: "#fff",
    },
    info: {
      light: "#bb8eff",
      main: "#8860d0",
      dark: "#56349e",
      contrastText: "#fff",
    },
    success: {
      light: "#69e747",
      dark: "#008300",
      main: "#28B401",
      contrastText: "#fff",
    },
    secondary: {
      light: "#b7ffff",
      main: "#84ceeb",
      dark: "#519db9",
      contrastText: "#fff",
    },
    background: {
      paper: "#FCFCFC",
      default: "#FCFCFC",
    },
    error: {
      light: "#FFCDD2",
      dark: "#D32F2F",
      main: "#F44336",
      contrastText: "#fff",
    },
    warning: {
      light: "#FFECB3",
      dark: "#FFA000",
      main: "#FFC107",
      contrastText: "#fff",
    },
  },
 
});
export const axiosconf = () => {
  axios.defaults.headers.common["Access-Control-Allow-Methods"] =
    "GET,PUT,POST,DELETE,PATCH,OPTIONS";
  axios.defaults.headers.common["Access-Control-Allow-Credentials"] = true;
  axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";
  axios.defaults.baseURL = process.env.REACT_APP_API_URL; //URL OF API
  return axios;
};

