import React from "react";
import { withStyles } from "@material-ui/core/styles";
import Menu from "@material-ui/core/Menu";
import MenuItem from "@material-ui/core/MenuItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import GitHubIcon from "@material-ui/icons/GitHub";
import CodeIcon from "@material-ui/icons/Code";
import IconButton from "@material-ui/core/IconButton";

const StyledMenu = withStyles({
  paper: {
    border: "1px solid #d3d4d5",
  },
})((props) => (
  <Menu
    elevation={0}
    getContentAnchorEl={null}
    anchorOrigin={{
      vertical: "bottom",
      horizontal: "center",
    }}
    transformOrigin={{
      vertical: "top",
      horizontal: "center",
    }}
    {...props}
  />
));

const StyledMenuItem = withStyles((theme) => ({
  root: {
    "&:focus": {
      backgroundColor: theme.palette.primary.main,
      "& .MuiListItemIcon-root, & .MuiListItemText-primary": {
        color: theme.palette.common.white,
      },
    },
  },
}))(MenuItem);

export default function DeveloperMenu() {
  const [anchorEl, setAnchorEl] = React.useState(null);

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <div>
      <IconButton
        edge="start"
        color="inherit"
        aria-label="menu"
        onClick={handleClick}
      >
        <CodeIcon />
      </IconButton>
      <StyledMenu
        id="customized-menu"
        anchorEl={anchorEl}
        keepMounted
        open={Boolean(anchorEl)}
        onClose={handleClose}
      >
        <StyledMenuItem>
          <ListItemIcon >
            <GitHubIcon fontSize="small"/>
          </ListItemIcon>
          <ListItemText primary="Randald V" onClick={() => window.open("https://github.com/Baxi19")}/>
        </StyledMenuItem>
        <StyledMenuItem>
          <ListItemIcon>
            <GitHubIcon fontSize="small" />
          </ListItemIcon>
          <ListItemText primary="Jazmine E" onClick={() => window.open("https://github.com/JazmineEP")}/>
        </StyledMenuItem>
        <StyledMenuItem>
          <ListItemIcon>
            <GitHubIcon fontSize="small" />
          </ListItemIcon>
          <ListItemText primary="Kevin D" onClick={() => window.open("https://github.com/Kevin-DCA")}/>
        </StyledMenuItem>
      </StyledMenu>
    </div>
  );
}
