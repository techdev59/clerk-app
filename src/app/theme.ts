// UI Imports
import { createTheme } from "@mui/material/styles";

export const theme = createTheme({
  typography: {
    allVariants: {
      fontFamily: "inherit",
    },
  },
  components: {
    MuiOutlinedInput: {
      styleOverrides: {
        root: {
          "& .MuiOutlinedInput-input": {
            padding: "10px",
          },
          "& .MuiOutlinedInput-notchedOutline": {
            border: `1px solid #6F6B6B`,
          },
          "&.Mui-focused": {
            "& .MuiOutlinedInput-notchedOutline": {
              border: `2px solid black`,
            },
          },
        },
      },
    },
    MuiInputLabel: {
      styleOverrides: {
        root: {
          color: "black!important",
          "&.Mui-focused": {
            fontWeight: "bold",
          },
          "&.MuiFormLabel-filled": {
            fontWeight: "bold",
          },
        },
      },
    },
  },
});
