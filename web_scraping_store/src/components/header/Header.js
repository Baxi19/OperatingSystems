import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import IconButton from "@material-ui/core/IconButton";
import SportsEsportsIcon from '@material-ui/icons/SportsEsports';
import { useDispatch } from "react-redux";
import { getGamesInfoActions } from "../../redux/gamesDuck";
import DeveloperMenu from '../developer_menu/DeveloperMenu';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },

}));

const Header = () => {
  const classes = useStyles();
  const dispatch = useDispatch();

  const getGamesInfo = () => {
    console.log("Update list from header")
    dispatch(getGamesInfoActions());
  };

  return (
    <>
      <AppBar >
        <Toolbar>
          <IconButton
            edge="start"
            className={classes.menuButton}
            color="inherit"
            aria-label="menu"
            onClick={() => getGamesInfo()}
          >
            <SportsEsportsIcon />
          </IconButton>
          <Typography variant="h6" className={classes.title}>
            PS5 Games
          </Typography>
          <DeveloperMenu />
        </Toolbar>
      </AppBar>
    </>
  );
};

export default Header;
