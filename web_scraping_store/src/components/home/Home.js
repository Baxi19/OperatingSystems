import React, { useEffect, useState } from "react";
import Header from "../header/Header";
import CardGames from "../card_games/CardGames";
import { useDispatch, useSelector } from "react-redux";
import { getGamesInfoActions } from "../../redux/gamesDuck";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";

const Home = () => {
  const classes = useStyles();
  const dispatch = useDispatch();
  const listGames = useSelector((store) => store.games.array);

  const [games, setGames] = useState(useSelector((store) => store.games.array));

  const getGamesInfo = () => {
    dispatch(getGamesInfoActions());
    setTimeout("", 2000);
    setGames(listGames);
  };

  useEffect(() => {
    setGames([]);
    getGamesInfo();
  }, [games]);

  return (
    <>
      <Header />
      <div className={classes.root}>
        <Grid
          container
          spacing={3}
        >
          <Grid 
              container 
              item xs 
              spacing={1}
            >
            {listGames && 
              listGames.map((item, i) => 
                <CardGames key={i} item={item}/> 
            )}
          </Grid>
        </Grid>
      </div>
    </>
  );
};

const useStyles = makeStyles((theme) => ({
  root: {
    marginTop: "80px",
    align: "center",
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: "center",
    color: theme.palette.text.secondary,
  },
}));

export default Home;
